from flask import Blueprint, jsonify, request
from Controllers.user_controller import get_all_users, get_user, create_user, update_user, delete_user

users_bp = Blueprint('users_bp', __name__, url_prefix='/api/v1/Users')

@users_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/', methods=['POST'])
def create_user_route():
    data = request.get_json()
    user = create_user(data)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    user = update_user(user_id, data)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    delete_user(user_id)
    return jsonify({'result': 'User deleted'})
