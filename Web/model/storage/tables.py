import bcrypt

from sqlalchemy import Column, String, Integer, Binary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, server_default='')

class User(Base):
    __tablename__ = 'users'

    username = Column(String, nullable=False, primary_key=True)
    password = Column(Binary(60), nullable=False)

    def check_password(self, password: bytes):
        return bcrypt.checkpw(password, self.password)