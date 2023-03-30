from flask import Blueprint
from flask import jsonify


user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/register')
def register():
    return jsonify(dict(status=True, msg="注册成功"))