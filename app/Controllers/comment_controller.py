from Model.comment_model import Comment

def get_comments_from_post(postId: int):
    return "Comments under post"

def get_comments_from_user(userId: int):
    return "Comments from user"

def add_new_comment(postId: int, userId: int, comment: str):
    new_comment = Comment(UserId=userId,PostId=postId,CommentText=comment)
    return "Added new comment with success"

# User may post more than 1 comment, so comment variable is also needed
def delete_comment(postId: int, userId: int, comment: str):
    return "deleted comment"