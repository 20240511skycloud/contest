import datetime
from functools import wraps

import jwt
from flask import request, jsonify, current_app

from app import app, db
from models import User, Task

# ... other imports ...

def generate_token(user_id):
    """Generates a JWT token for the given user ID."""
    payload = {
        'sub': user_id,
        'iat': datetime.datetime.utcnow(),
        # 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def token_required(f):
    """Decorator to check for a valid JWT token in the request header."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': '缺少 Token'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['sub'])
            print(current_user)
        except:
            return jsonify({'message': 'Token 无效'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

