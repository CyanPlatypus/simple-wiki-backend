from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from ..model.user import User
from ..db import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(128))    
    #release_date = Column(Date)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", backref="articles")



    def __init__(self, title, author):
        self.title = title
        self.author = author
        #self.release_date = release_date