from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql import func
from config.setting import db
from .mixins.datetime import TimeTrackable
from flask_login import UserMixin
    



class User(db.Model, TimeTrackable, UserMixin):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50), nullable=False)
    password = mapped_column(String(100), nullable=False)

    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"{self.username}"
