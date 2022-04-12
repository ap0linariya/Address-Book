from flask import Flask
from flask_migrate import Migrate

from models import db
from routes.user_bp import user_bp
from routes.phone_bp import phone_bp
from routes.email_bp import email_bp

#создание приложения Flask
app = Flask(__name__)
#подключение к базе данных
app.config.from_object('config')

#взаимодействие с базой данных
db.init_app(app)
#экземпляр Flask-Migrate для обработки миграций
migrate = Migrate(app, db)

#регистрация схемы разделения кода
app.register_blueprint(user_bp, url_prefix='/api/v1/users')
app.register_blueprint(phone_bp, url_prefix='/api/v1/users/number_phones')
app.register_blueprint(email_bp, url_prefix='/api/v1/users/emails')

if __name__ == '__main__':
    app.run(debug=True)