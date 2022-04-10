from flask import Flask, render_template
from flask_migrate import Migrate

from models import db
from routes.user_bp import user_bp
from routes.phone_bp import phone_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/api/v1/users')
app.register_blueprint(phone_bp, url_prefix='/api/v1/users/number_phones')

if __name__ == '__main__':
    app.run(debug=True)