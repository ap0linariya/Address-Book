from flask_sqlalchemy import SQLAlchemy

#экземпляр Flask-SQLAlchemy для взаимодействий с базой данных
db = SQLAlchemy()

#Модель сущности Пользователи для определения и обработки данных
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) #уникальное значение поля
    full_name = db.Column(db.String())
    avatar = db.Column(db.String())
    gender = db.Column(db.String())
    birthday = db.Column(db.String())
    address = db.Column(db.String())
    #Связаные модели телефонов и эл. адресов
    number_phones = db.relationship('PhoneModel', backref='user', cascade='all, delete-orphan', passive_deletes=True)
    emails = db.relationship('EmailModel', backref='user', cascade='all, delete-orphan', passive_deletes=True)

    def __init__(self, id, full_name, avatar, gender, birthday, address):
        self.id = id
        self.full_name = full_name
        self.avatar = avatar
        self.gender = gender
        self.birthday = birthday
        self.address = address

    def __repr__(self):
        return f""

#Модель сущности Телефоны для определения и обработки данных
class PhoneModel(db.Model):
    __tablename__ = 'number_phones'

    id = db.Column(db.Integer, primary_key=True) #уникальное значение поля
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')) #связь с моделью Пользователи
    type_phone = db.Column(db.String())
    number = db.Column(db.String())

    def __init__(self, id, user_id, type_phone, number):
        self.id = id
        self.user_id = user_id
        self.type_phone = type_phone
        self.number = number

    def __repr__(self):
        return f""

#Модель сущности Эл. адреса для определения и обработки данных
class EmailModel(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)#уникальное значение поля
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')) #связь с моделью Пользователи
    type_email = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, user_id, type_email, email):
        self.id = id
        self.user_id = user_id
        self.type_email = type_email
        self.email = email

    def __repr__(self):
        return f""