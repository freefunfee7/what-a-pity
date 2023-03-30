from flask import Flask
from config import Config
from app.controllers.auth.user import user

pity = Flask(__name__)

# 注册蓝图
pity.register_blueprint(user)

pity.config.from_object(Config)