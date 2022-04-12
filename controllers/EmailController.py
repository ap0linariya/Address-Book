from flask import Blueprint, request

from models import EmailModel, db

#разделение кода
email_bp = Blueprint('email_bp', __name__)


#Вывод информации о выбранном по id эл. адресе
def read():
    id = request.args.get('id')
    email = EmailModel.query.get(id)

    results = {
        "id": email.id,
        "user_id": email.user_id,
        "type_phone": email.type_email,
        "number": email.email
    }
    return {"message": "success", "email": results}


#Создание нового эл. адреса
def create():
    if request.is_json:
        data = request.get_json()
        new_email = EmailModel(**data)
        db.session.add(new_email)
        db.session.commit()
        return {"message": f"Email {new_email.email} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


# Фильтрация эл. адресов по id пользователя и сортировка по выбранному параметру
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
        emails = EmailModel.query.filter(EmailModel.user_id == user_id).order_by(type(EmailModel.id))
    elif order_by == 'user_id':
        emails = EmailModel.query.filter(EmailModel.user_id == user_id).order_by(type(EmailModel.user_id))
    elif order_by == 'type_email':
        emails = EmailModel.query.filter(EmailModel.user_id == user_id).order_by(type(EmailModel.type_email))
    elif order_by == 'email':
        emails = EmailModel.query.filter(EmailModel.user_id == user_id).order_by(type(EmailModel.email))
    else:
        return {"error": f"Incorrect order_by '{order_by}'"}

    results = [
        {
            "id": email.id,
            "user_id": email.user_id,
            "type_phone": email.type_email,
            "number": email.email,
        } for email in emails]

    return {"number_phones": results, "message": "success"}

#Редактирование выбранного по id эл. адреса
def update():
    data = request.get_json()
    email = EmailModel.query.get(data['id'])

    email.user_id = data['user_id']
    email.type_email = data['type_email']
    email.email = data['email']

    db.session.add(email)
    db.session.commit()
    return {"message": f"Email {email.email} successfully updated"}


#Удаление выбранного по id эл. адреса
def delete():
    id = request.args.get('id')
    email = EmailModel.query.get(id)
    db.session.delete(email)
    db.session.commit()

    return {"message": f"Email  {email.email} successfully deleted."}

