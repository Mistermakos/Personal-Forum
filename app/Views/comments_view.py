from flask import Blueprint, jsonify, request
from Controllers.comment_controller import get_all_comments, get_comment, create_comment, update_comment, delete_comment

comments_bp = Blueprint('comments_bp', __name__, url_prefix='/api/v1/Comments')

@comments_bp.route('/', methods=['GET'])
def list_comments():
    comments = get_all_comments()
    return jsonify([{'id': c.id, 'user_id': c.user_id, 'post_id': c.post_id, 'comment_text': c.comment_text} for c in comments])

@comments_bp.route('/<int:comment_id>', methods=['GET'])
def get_comment_by_id(comment_id):
    comment = get_comment(comment_id)
    if comment:
        return jsonify({'id': comment.id, 'user_id': comment.user_id, 'post_id': comment.post_id, 'comment_text': comment.comment_text})
    return jsonify({'error': 'Comment not found'}), 404

@comments_bp.route('/', methods=['POST'])
def create_comment_route():
    data = request.get_json()
    comment = create_comment(data)
    return jsonify({'id': comment.id, 'user_id': comment.user_id, 'post_id': comment.post_id, 'comment_text': comment.comment_text}), 201

@comments_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment_route(comment_id):
    data = request.get_json()
    comment = update_comment(comment_id, data)
    if comment:
        return jsonify({'id': comment.id, 'user_id': comment.user_id, 'post_id': comment.post_id, 'comment_text': comment.comment_text})
    return jsonify({'error': 'Comment not found'}), 404

@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment_route(comment_id):
    delete_comment(comment_id)
    return jsonify({'result': 'Comment deleted'})
