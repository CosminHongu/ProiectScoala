from base import Session, Base, engine
from cont import Cont
from cursant import Cursant
from instructor import Instructor
from pachet_ore import PachetOre

from personal import Personal
from personal_administrativ import PersonalAdministrativ
from sediu import Sediu
from address import Address
from vehicul import Vehicul


def adaugare_instructor(instructor, cont, vehicul, personal):
    instructor.cont = cont
    instructor.vehicul = vehicul
    instructor.personal = personal
    return instructor

def adaugare_personal_administrativ(personal_adm, cont, personal):
    personal_adm.cont = cont
    personal_adm.personal = personal

    return personal_adm

def create_all():
    session = Session()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

