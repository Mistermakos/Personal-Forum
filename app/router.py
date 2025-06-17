from flask import Blueprint, render_template
from Views.users_view import users_bp
from Views.post_view import posts_bp
from Views.comments_view import comments_bp

main_bp = Blueprint("main", __name__)

# connecting routes
main_bp.register_blueprint(users_bp)
main_bp.register_blueprint(posts_bp)
main_bp.register_blueprint(comments_bp)

# ui routes
@main_bp.route('/')
def hello_world():
    return render_template("index.html")