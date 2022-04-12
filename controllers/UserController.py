from flask import Blueprint, request

from models import UserModel, db

#разделение кода
user_bp = Blueprint('user_bp', __name__)

#Вывод информации о выбранном по id пользователе
def read():
    id = request.args.get('id')
    user = UserModel.query.get(id)
    results = {
        "id": user.id,
        "full_name": user.full_name,
        "avatar": user.avatar,
        "gender": user.gender,
        "birthday": user.birthday,
        "address": user.address,
    }
    return {"message": "success", "user": results}


#Создание нового пользователя
def create():
    if request.is_json:
        data = request.get_json()
        new_user = UserModel(**data)
        db.session.add(new_user)
        db.session.commit()
        return {"message": f"User {new_user.full_name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


# Фильтрация пользователей по полу и сортировка по выбранному параметру
def show():
    gender = request.args.get('gender')
    order_by = request.args.get('order_by')
    order_type = request.args.get('order_type')
    if order_type == 'asc' or order_type == None:
        type = db.asc
    elif order_type == 'desc':
        type = db.desc
    else:
        return {"error": f"Incorrect order_type '{order_type}'"}

    if order_by == 'id' or order_by == None:
        users = UserModel.query.filter(UserModel.gender == gender).order_by(type(UserModel.id))
    elif order_by == 'full_name':
        users = UserModel.query.filter(UserModel.gender == gender).order_by(type(UserModel.full_name))
    elif order_by == 'avatar':
        users = UserModel.query.filter(UserModel.gender == gender).order_by(type(UserModel.avatar))
    elif order_by == 'gender':
        users = UserModel.query.filter(UserModel.gender == gender).order_by(type(UserModel.gender))
    elif order_by == 'birthday':
        users = UserModel.query.filter(UserModel.gender == gender).order_by(type(UserModel.birthday))
    elif order_by == 'address':
        users = UserModel.query.filter(UserModel.gender == gender).order_by(type(UserModel.address))
    else:
        return {"error": f"Incorrect order_by '{order_by}'"}

    results = [
        {
            "id": user.id,
            "full_name": user.full_name,
            "avatar": user.avatar,
            "gender": user.gender,
            "birthday": user.birthday,
            "address": user.address,
        } for user in users]

    return {"users": results, "message": "success"}


#Редактирование выбранного по id пользователя
def update():
    data = request.get_json()
    user = UserModel.query.get(data['id'])

    user.full_name = data['full_name']
    user.avatar = data['avatar']
    user.gender = data['gender']
    user.birthday = data['birthday']
    user.address = data['address']

    db.session.add(user)
    db.session.commit()
    return {"message": f"User {user.full_name} successfully updated"}


#Удаление выбранного по id пользователя
def delete():
    id = request.args.get('id')
    user = UserModel.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return {"message": f"User {user.full_name} successfully deleted."}