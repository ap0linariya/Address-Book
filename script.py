import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#создание приложения Flask
app = Flask(__name__)
#подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2009@localhost:5432/mydb'
#экземпляр Flask-SQLAlchemy для взаимодействий с базой данных
db = SQLAlchemy(app)
#экземпляр Flask-Migrate для обработки миграций
migrate = Migrate(app, db)

#Модель сущности Пользователи для определения и обработки данных
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) #уникальное значение поля
    full_name = db.Column(db.String(64))
    avatar = db.Column(db.String())
    gender = db.Column(db.String())
    birthday = db.Column(db.String())
    address = db.Column(db.String())
    # Связаные модели телефонов и эл. адресов
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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete = 'CASCADE')) #связь с моделью Пользователи
    type_phone = db.Column(db.String())
    number = db.Column(db.String())

    def __init__(self, id, user_id, type_phone, number):
        self.id = id
        self.user_id = user_id
        self.type_phone = type_phone
        self.number = number

    def __repr__(self):
        return f""


#Модель сущности Эл. почты для определения и обработки данных
class EmailModel(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True) #уникальное значение поля
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete = 'CASCADE')) #связь с моделью Пользователи
    type_email = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, user_id, type_email, email):
        self.id = id
        self.user_id = user_id
        self.type_email = type_email
        self.email = email

    def __repr__(self):
        return f""

#кортеж ФИО, путь к файлу аватара на сервере, пол
full_name = [["Иванов Иван Иванович","http://127.0.0.1:500/api/v1/photo_Ivanov","м"],
             ["Захаров Константин Федорович","http://127.0.0.1:500/api/v1/photo_Zaharov","м"],
             ["Лаптина Анна Юрьевна","http://127.0.0.1:500/api/v1/photo_Laptina","ж"],
             ["Сергеев Петр Георгиевич","http://127.0.0.1:500/api/v1/photo_Sergeev", "м"],
             ["Павленко Анастасия Петровна","http://127.0.0.1:500/api/v1/photo_Pavlenko","ж"],
             ["Игнатенко Степан Львович","http://127.0.0.1:500/api/v1/photo_Ignatenko", "м"],
             ["Косых Елезавета Анатольевна","http://127.0.0.1:500/api/v1/photo_Kosyh","ж"],
             ["Кудрин Тимофей Игоревич","http://127.0.0.1:500/api/v1/photo_Kudrin", "м"],
             ["Кисилев Антон Юрьевич","http://127.0.0.1:500/api/v1/photo_Kisilev", "м"],
             ["Щербенко  Мирослава Андреевна","http://127.0.0.1:500/api/v1/photo_Shcherbenko", "м"]]

#кортеж дата рождения
birthday = ["2000.01.29", "1996.09.06", "1998.05.23", "2001.11.30", "1989.10.04", "1994.02.08", "1984.02.29",
            "1985.07.19", "1991.03.14", "1990.04.05"]

#кортеж адрес
address = ["Кирова 5", "Саянская 69б", "Кутузовская 13", "Кишиневская 5", "Кольцевая 98", "Сиренева 12",
           "Забайкальска 35", "Забайкальская 12", "Курчатова 100", "Советская 26"]

#кортеж мобильный номер телефона
mobile = ["89233345678", "89056748912", "89081234554", "89567891211", "89459093888", "89675007890", "89231234509",
          "89231207890", "89093886778", "89913013411"]
#кортеж городской номер телефона
landline = ["793-888", "967-500", "231-234", "207-890", "938-678", "991-301", "333-485", "567-912", "123-554", "891-211"]

#кортеж личная эл. почта
personal = ["mymail@gmail.com", "wnhborq@outlook.com", "vubx0t@mail.ru", "gq@yandex.ru", "wrts90puk@yandex.ru",
            "yxunv@gmail.com", "kaft93x@outlook.com", "f245n@outlook.com", "u7yhwf1vb@mail.ru", "jirbold@gmail.com"]
#кортеж рабочая эл. почта
work = ["3vmtdo1@outlook.com", "9k15qr2h@gmail.com", "r3p4mgf5@yandex.ru", "r0o6f92@gmail.com", "xiuq5olft@gmail.com",
        "3xkgmsd9t@gmail.com", "jxqme@gmail.com", "t3m6u8v@gmail.com", "uakvj8p9d@yandex.ru", "mek975vcx@gmail.com"]

#создание рандомных пользователей с городским и мобильным номером телефона, с личной и рабочей почтой
for i in range(1, 100):
    name, avatar, gender = random.choice(full_name)

    #экземпляр Пользователя
    new_user = UserModel(i, name, avatar, gender, random.choice(birthday), random.choice(address))

    #экземпляр Телефона
    mobile_phone = PhoneModel(i*2-1, i, "mobile", random.choice(mobile))
    landline_phone = PhoneModel(i*2, i, "landline", random.choice(landline))

    #экземпляр Эл. почты
    personal_email = EmailModel(i*2-1, i, "personal", random.choice(personal))
    work_email = EmailModel(i*2, i, "work", random.choice(work))

    #создание сеанса БД и добавление новых элементов
    db.session.add(new_user)

    db.session.add(mobile_phone)
    db.session.add(landline_phone)

    db.session.add(personal_email)
    db.session.add(work_email)

    #сохранение изменений в БД
    db.session.commit()