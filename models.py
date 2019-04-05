#from smartninja_nosql.odm import Model#Simulierte Datenbank in Form eines ODM
from utils import get_mongo_db


class User():#Simulierte Tabelle User
    def __init__(self, name, email, secret_number, **kwargs):
        self.name = name
        self.email = email
        self.secret_number = secret_number

        super().__init__(**kwargs)

    @classmethod
    def get_collection(cls):
        db = get_mongo_db()
        return db[cls.__name__]
