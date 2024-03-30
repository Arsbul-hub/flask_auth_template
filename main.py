import flask
from app import app, login_blueprint

if __name__ == "__main__":
    app.register_blueprint(login_blueprint)
    app.run(host="0.0.0.0", port=2000, debug=True)