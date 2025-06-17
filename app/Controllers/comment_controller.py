from Models.comment_model import Comment

def get_all_comments():
    return Comment.get_all()

def get_comment(comment_id):
    return Comment.get_by_id(comment_id)

def create_comment(data):
    comment = Comment(data.get('user_id'), data.get('post_id'), data.get('comment_text'))
    comment.save()
    return comment

def update_comment(comment_id, data):
    comment = Comment.get_by_id(comment_id)
    if not comment:
        return None
    comment.user_id = data.get('user_id', comment.user_id)
    comment.post_id = data.get('post_id', comment.post_id)
    comment.comment_text = data.get('comment_text', comment.comment_text)
    comment.save()
    return comment

def delete_comment(comment_id):
    Comment.delete(comment_id)
