from smartninja_nosql.odm import Model#Simulierte Datenbank in Form eines ODM


class User(Model):#Simulierte Tabelle User
    def __init__(self, name, email, secret_number, **kwargs):
        self.name = name
        self.email = email
        self.secret_number = secret_number

        super().__init__(**kwargs)
