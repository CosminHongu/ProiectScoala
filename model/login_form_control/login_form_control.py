from PyQt5 import QtWidgets
from PyQt5 import QtCore
from base import Session
from sqlalchemy import select

from cont import Cont
from personal import Personal
from instructor import Instructor
from sediu import Sediu
from address import Address
from cursant import Cursant
from vehicul import Vehicul
from pachet_ore import PachetOre
from personal_administrativ import PersonalAdministrativ

from base import Session
from cont import Cont
from views.login_form_view import Ui_Form
from model.user_form_control.user_form_control import ContWindow


class LoginWndow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.new_window = None
        self.ui_loginForm = Ui_Form()
        self.ui_loginForm.setupUi(self)

        self.ui_loginForm.login_button.clicked.connect(self.login_check)

    def login_check(self):
        username = self.ui_loginForm.username_input.text()
        password = self.ui_loginForm.password_input.text()
        session = Session()
        try:
            query = session.query(Cont).filter(Cont.user == username, Cont.parola == password)
            count = 0

        except Exception as e:
            print(e)
        session.commit()
        session.close()