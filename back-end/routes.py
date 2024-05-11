from flask import request, jsonify, Flask, send_from_directory

import models
from app import app, db
from auth import generate_token, token_required
from schemas import TaskSchema



@app.route("/")
def index():
  return send_from_directory('dist', 'index.html')

@app.route('/api/users', methods=['POST'])
def create_user():
    # ... (实现用户注册逻辑)
    data = request.get_json()
    c_username = data.get('username')
    c_passwd = data.get('password')

    if not c_username or not c_passwd:
        return jsonify({'message': '用户名和密码都是必填项'}), 400

    if models.User.query.filter_by(c_username=c_username).first():
        return jsonify({'message': '用户名已被占用'}), 400

    user = models.User(c_username=c_username, c_passwd=c_passwd)
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': 'ok'})

@app.route('/api/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    c_username = data.get('username')
    c_passwd = data.get('password')

    if not c_username or not c_passwd:
        return jsonify({'message': '用户名和密码都是必填项'}), 400

    user = models.User.query.filter_by(c_username=c_username).first()
    if user and (user.c_passwd == c_passwd):
        token = generate_token(str(user.id))
        return jsonify({'message': '登录成功', 'token': token}), 200
        # 在实际应用中，您需要生成 JWT 并返回给用户
    else:
        return jsonify({'message': '用户名或密码错误'}), 401


@app.route('/api/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    title = data.get('title')
    desc = data.get('desc')

    if not title or not desc:
        return jsonify({'message': '标题和描述都是必填项'}), 400

    task = models.Task(c_title=title, c_description=desc,c_user_id=current_user.id,c_status=0)
    db.session.add(task)
    db.session.commit()
    return jsonify({'status': 'ok'})

@app.route('/api/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    tasks = models.Task.query.filter_by(c_user_id=current_user.id).all()
    schema = TaskSchema(many=True)
    return jsonify(schema.dump(tasks))

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
@token_required
def get_task(current_user_id,task_id):
    task = models.Task.query.filter_by(id=task_id,c_user_id=current_user_id.id).first()
    if not task:
        return jsonify({'message': '任务不存在'}), 404
    schema = TaskSchema()
    return jsonify(schema.dump(task))

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user_id,task_id):
    data = request.get_json()
    task = models.Task.query.filter_by(id=task_id,c_user_id=current_user_id.id).first()
    if not task:
        return jsonify({'message': '任务不存在'}), 404
    task.c_title = data.get('title', task.c_title)
    task.c_description = data.get('desc', task.c_description)
    db.session.commit()
    return jsonify({'message': '任务更新成功'}), 200

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user_id,task_id):
    task = models.Task.query.filter_by(id=task_id,c_user_id=current_user_id.id).first()
    if not task:
        return jsonify({'message': '任务不存在'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'status': 'ok'})


