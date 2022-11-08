from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class PersonalAdministrativ(Base):
    __tablename__ = 'personaladministrativ'

    #Atributul back-populates este folosit pentru ca engine-ul sa intelelaga
    #ca este o relatie si sa populeze automat clasa copil cand clasa parinte este creata.

    id = Column(Integer, primary_key=True)
    personal = relationship("Personal", back_populates="personaladministrativ")
    personal_id = Column(Integer, ForeignKey("personal.id"))
    cont = relationship("Cont", back_populates="personaladministrativ")
    cont_id = Column(Integer, ForeignKey("cont.id"))