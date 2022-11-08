from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

class Vehicul(Base):
    __tablename__ = 'vehicul'

    id = Column(Integer, primary_key=True)
    marca = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    anFabricatie = Column(String(4), nullable=False)
    cutie_de_viteze= Column(String(100), nullable=False)
    numar_de_inmatriculare= Column(String(10), nullable=False)

    # Atributul back-populates este folosit pentru ca engine-ul sa intelelaga
    # ca este o relatie si sa populeze automat clasa copil cand clasa parinte este creata.
    instructor = relationship("Instructor", back_populates="vehicul", uselist = False)

    @validates("anFabricatie")
    def validate_anFabricatie(self, key, anFabricatie):
        if len(str(anFabricatie)) != 4:
            raise ValueError("Anul fabricatiei nu este corect!")
        return anFabricatie

    @validates("numar_de_inmatriculare")
    def validate_numar_de_inmatriculare(self, key, numar_de_inmatriculare):
            if len(str(numar_de_inmatriculare)) != 7:
                raise ValueError("Numarul de inmatriculare nu este corect!")
            return numar_de_inmatriculare

        # setare getters & setters

    def __init__(self, marca, model, anFabricatie, cutie_de_viteze, numar_de_inmatriculare):
        self.marca = marca
        self.model = model
        self.anFabricatie = anFabricatie
        self.cutie_de_viteze = cutie_de_viteze
        self.numar_de_inmatriculare = numar_de_inmatriculare
