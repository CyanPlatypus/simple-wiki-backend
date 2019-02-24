from sqlalchemy import Column, String, Integer, Boolean

from ..db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    passw = Column(String(128))
    isAdmin = Column(Boolean)

    def __init__(self, name, passw):
        self.name = name
        self.passw = passw
        self.isAdmin = False