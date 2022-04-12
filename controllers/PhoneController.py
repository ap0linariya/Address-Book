from flask import Blueprint, request

from models import PhoneModel, db

#разделение кода
phone_bp = Blueprint('phone_bp', __name__)


#Вывод информации о выбранном по id номере телефона
def read():
    id = request.args.get('id')
    number_phone = PhoneModel.query.get(id)
    results = {
        "id": number_phone.id,
        "user_id": number_phone.user_id,
        "type_phone": number_phone.type_phone,
        "number": number_phone.number
    }
    return {"message": "success", "number_phone": results}


#Создание нового номера телефона
def create():
    if request.is_json:
        data = request.get_json()
        new_phone = PhoneModel(**data)
        db.session.add(new_phone)
        db.session.commit()
        return {"message": f"Number phone {new_phone.number} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


#Фильтрация номеров телефона по id пользователя и сортировка по выбранному параметру
def show():
    user_id = request.args.get('user_id')
    order_by = request.args.get('order_by')
    order_type = request.args.get('order_type')
    if order_type == 'asc' or order_type == None:
        type = db.asc
    elif order_type == 'desc':
        type = db.desc
    else:
        return {"error": f"Incorrect order_type '{order_type}'"}

    if order_by == 'id' or order_by == None:
        number_phones = PhoneModel.query.filter(PhoneModel.user_id == user_id).order_by(type(PhoneModel.id))
    elif order_by == 'user_id':
        number_phones = PhoneModel.query.filter(PhoneModel.user_id == user_id).order_by(type(PhoneModel.user_id))
    elif order_by == 'type_phone':
        number_phones = PhoneModel.query.filter(PhoneModel.user_id == user_id).order_by(type(PhoneModel.type_phone))
    elif order_by == 'number':
        number_phones = PhoneModel.query.filter(PhoneModel.user_id == user_id).order_by(type(PhoneModel.number))
    else:
        return {"error": f"Incorrect order_by '{order_by}'"}

    results = [
        {
            "id": number_phone.id,
            "user_id": number_phone.user_id,
            "type_phone": number_phone.type_phone,
            "number": number_phone.number,
        } for number_phone in number_phones]

    return {"number_phones": results, "message": "success"}


#Редактирование выбранного по id номера телефона
def update():
    data = request.get_json()
    number_phone = PhoneModel.query.get_or_404(data['id'])

    number_phone.user_id = data['user_id']
    number_phone.type_phone = data['type_phone']
    number_phone.number = data['number']

    db.session.add(number_phone)
    db.session.commit()
    return {"message": f"Number phone  {number_phone.number} successfully updated"}


#Удаление выбранного по id номера телефона
def delete():
    id = request.args.get('id')
    number_phone = PhoneModel.query.get_or_404(id)
    db.session.delete(number_phone)
    db.session.commit()

    return {"message": f"Number phone  {number_phone.number} successfully deleted."}

