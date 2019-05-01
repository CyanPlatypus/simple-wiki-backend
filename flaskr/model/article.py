from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
import datetime

from ..model.user import User
from ..db import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    content = Column(Text())
    date = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", backref="articles")



    def __init__(self, title, author, content, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        #self.release_date = datetime.datetime.now()