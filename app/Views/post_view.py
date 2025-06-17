from flask import Blueprint, jsonify, request
from Controllers.post_controller import get_all_posts, get_post, create_post, update_post, delete_post

posts_bp = Blueprint('posts_bp', __name__, url_prefix='/api/v1/Posts')

@posts_bp.route('/', methods=['GET'])
def list_posts():
    posts = get_all_posts()
    return jsonify([{'id': p.id, 'user_id': p.user_id, 'title': p.title, 'post_content': p.post_content} for p in posts])

@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    post = get_post(post_id)
    if post:
        return jsonify({'id': post.id, 'user_id': post.user_id, 'title': post.title, 'post_content': post.post_content})
    return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('/', methods=['POST'])
def create_post_route():
    data = request.get_json()
    post = create_post(data)
    return jsonify({'id': post.id, 'user_id': post.user_id, 'title': post.title, 'post_content': post.post_content}), 201

@posts_bp.route('/<int:post_id>', methods=['PUT'])
def update_post_route(post_id):
    data = request.get_json()
    post = update_post(post_id, data)
    if post:
        return jsonify({'id': post.id, 'user_id': post.user_id, 'title': post.title, 'post_content': post.post_content})
    return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post_route(post_id):
    delete_post(post_id)
    return jsonify({'result': 'Post deleted'})
