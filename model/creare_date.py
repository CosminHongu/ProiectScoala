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

    # Creare cont pentru instructori
    instructor_cont1 = Cont("user_inst1", "parola1", 1)
    instructor_cont2 = Cont("user_inst2", "parola2", 1)
    instructor_cont3 = Cont("user_inst3", "parola3", 1)

    # Creare instructori respectivi | Cont instructor, Vehicul, Personal respectiv
    instructor1 = adaugare_instructor(Instructor(), instructor_cont1, vehicul1, personal1)
    instructor2 = adaugare_instructor(Instructor(), instructor_cont2, vehicul2, personal2)
    instructor3 = adaugare_instructor(Instructor(), instructor_cont3, vehicul3, personal3)

 #Creare pachet_ore
pachet_ore1 = PachetOre(30)
pachet_ore2 = PachetOre(15)
pachet_ore1.instructor_id = 1
pachet_ore2.instructor_id = 2

#Creare Cursant:
cursant1 = Cursant("Popescu", "Marius", "10/10/2001" )
cursant.cont = Cont("user1", "parola1", 0)

