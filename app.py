from config.setting import db
from flask_migrate import Migrate
from apps.post.views import post_bp, index as root_view
from apps.error.handlers import error_bp
from apps.user.views import user_bp
from apps import app


app.add_url_rule("/", view_func=root_view, endpoint="root")
app.register_blueprint(post_bp, url_prefix="/posts")
app.register_blueprint(error_bp)
app.register_blueprint(user_bp, url_prefix="/users")

db.init_app(app)
Migrate(app, db)



if __name__ == "__main__":
    app.run(debug=True)