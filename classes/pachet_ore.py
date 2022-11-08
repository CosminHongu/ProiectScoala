from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

# Pachete 30 ore
# Un singur pachet la cursant / Nu poate sa cumpere alte pachete
#  30 ore obligatorii
#  Pachete de o ora / {multiple pachete}

class PachetOre(Base):
    __tablename__ = 'pachet_ore'
    #MANY TO MANY
    # Se creaza automat o tabela ajutatoare pentru manytomany relatii in care se
    # populeaza cu relatiile dintre clasa parinte si cea copil
    instructor_pachet_ore_relationship = Table('instructor_pachet_ore_relationship', Base.metadata,
                                    Column('instructor_id', Integer, ForeignKey('instructor.id')),
                                    Column('pachet_ore_id', Integer, ForeignKey('pachet_ore.id')),

                                    )

    id = Column(Integer, primary_key=True)
    durata = Column(Integer, nullable=False)
    pret = Column(Integer, nullable=False)
    #Definirea relatiiei manytomany si atribuirea tabelei ajutatoare eg: secondary="tabela_ajutatoare".
    instructor = relationship('Instructor', secondary=instructor_pachet_ore_relationship)

    #Initializare getters si setters.
    def __init__(self, durata, pret):
        self.durata = durata
        self.pret = pret