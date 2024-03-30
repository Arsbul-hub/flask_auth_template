from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

__basemodel = db.Model


class User(__basemodel, UserMixin):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String)
    password_hash = Column(String(128))
    role_id = Column(Integer, ForeignKey("Roles.id"))
    role = db.relationship("Role", uselist=False, backref="users")

    def __repr__(self):
        return f"Пользователь {self.username}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(__basemodel):
    __tablename__ = 'Roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    access_level = Column(Integer)
