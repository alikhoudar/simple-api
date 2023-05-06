from flask import Flask, jsonify, request
from db import users

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to my API!'})


@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        return jsonify({'message': 'User not found!'}), 404
    return jsonify({'user': user[0]})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        return jsonify({'message': 'User not found!'}), 404
    user[0]['name'] = request.json['name']
    return jsonify({'message': 'User updated successfully!'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        return jsonify({'message': 'User not found!'}), 404
    users.remove(user[0])
    return jsonify({'message': 'User deleted successfully!'})

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    user_id = max([user['id'] for user in users]) + 1
    user = {'id': user_id, 'name': name}
    users.append(user)
    return jsonify({'user_id': user_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
