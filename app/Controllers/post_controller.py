from Models.post_model import Post

def get_all_posts():
    return Post.get_all()

def get_post(post_id):
    return Post.get_by_id(post_id)

def create_post(data):
    post = Post(data.get('user_id'), data.get('title'), data.get('post_content'))
    post.save()
    return post

def update_post(post_id, data):
    post = Post.get_by_id(post_id)
    if not post:
        return None
    post.user_id = data.get('user_id', post.user_id)
    post.title = data.get('title', post.title)
    post.post_content = data.get('post_content', post.post_content)
    post.save()
    return post

def delete_post(post_id):
    Post.delete(post_id)
