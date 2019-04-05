import json

from ..db import Session, engine, Base
from ..model.article import Article
from ..model.user import User

from ..dto.dto_user import DtoUser

def add_user(userDto):
    session = Session()    
    session.add(User(userDto.name, userDto.passw))
    #arts = session.query(Article).all()
    #arS = json.dumps([( DtoArticleInfo(ob.title, ob.author.name)).__dict__ for ob in arts])
    session.commit()
    session.close()

def get_users():
    session = Session()
    users = [ DtoUser(user.name, user.passw) for user in session.query(User).all()]
    session.close()
    return users

def get_user_by_name(uname):
    session = Session()
    #user = [ DtoUser(user.name, user.passw) for user in session.query(User).filter(name == uname).first()]
    user =  session.query(User).filter(User.name == uname).first()
    session.close()
    if user is not None:
        return DtoUser(user.name, user.passw)    
    return None
    
