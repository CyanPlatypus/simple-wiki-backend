import json

from ..db import Session, engine, Base
from ..model.article import Article
from ..model.user import User

from ..dto.dto_user import DtoUser

def add_user(userDto):
    session = Session()
    if get_user_db_by_name(userDto.name) != None :
        session.close()
        return False
    session.add(User(userDto.name, userDto.passw))
    #arts = session.query(Article).all()
    #arS = json.dumps([( DtoArticleInfo(ob.title, ob.author.name)).__dict__ for ob in arts])
    session.commit()
    session.close()
    return True

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
        userDto = DtoUser(user.name, user.passw)
        userDto.isAdmin = user.isAdmin
        return  userDto
    return None

def get_user_db_by_name(uname):
    session = Session()
    #user = [ DtoUser(user.name, user.passw) for user in session.query(User).filter(name == uname).first()]
    user =  session.query(User).filter(User.name == uname).first()
    session.close()
    if user is not None:
        return user
    return None

def get_user_id_by_name(uname):
    session = Session()
    #user = [ DtoUser(user.name, user.passw) for user in session.query(User).filter(name == uname).first()]
    user =  session.query(User).filter(User.name == uname).first()
    session.close()
    if user is not None:
        return user.id
    return None
    
