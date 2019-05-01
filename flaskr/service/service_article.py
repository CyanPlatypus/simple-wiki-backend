import json

from ..db import Session, engine, Base
from ..model.article import Article
from ..model.user import User
from ..dto.dto_article import DtoArticleInfo
from . import service_user

import datetime

def get_articles():

    session = Session()

    arts = session.query(Article).all()
    arS = json.dumps([( DtoArticleInfo(ob.title, ob.author.name, "", ob.date, ob.id)).__dict__ for ob in arts],  indent=4, sort_keys=True, default=str)

    session.close()

    return arS

def get_article(id):
    session = Session()
    art = session.query(Article).filter(Article.id == id).first()
    arS = json.dumps((DtoArticleInfo(art.title, art.author.name, art.content, art.date, art.id)).__dict__, indent=4, sort_keys=True, default=str)
    session.close()
    return arS

def add_article(artDto):
    session  = Session()
    user = service_user.get_user_db_by_name(artDto.author)
    art = Article(artDto.title, user, artDto.content)
    session.add(art)
    session.commit()
    art_id = art.id
    session.close()

    return art_id

def update_article(artDto):
    session  = Session()
    user = service_user.get_user_db_by_name(artDto.author)
    db_art = session.query(Article).filter(Article.id == artDto.id).first()
    art = Article(artDto.title, user, artDto.content, id=artDto.id)
    art.date = datetime.datetime.now()
    session.merge(art)
    session.commit()
    art_id = art.id
    session.close()
    return art_id

def delete_article(id, username):
    session  = Session()
    user = service_user.get_user_db_by_name(username)
    if user != None and user.isAdmin:
        session.query(Article).filter(Article.id == id).delete()
        session.commit()
    session.close()

def fill():
    create_db()
    session = Session()

    alice = User("alice", "alice")
    bob = User("bob", "bob")

    art1 = Article("badgers are everywhere", alice, "everywhere")
    art2 = Article("soon my prince will come", alice, "everywhere")
    art3 = Article("time managemrnt", bob, "everywhere")
    art4 = Article("true believers", bob, "everywhere")
    art5 = Article("waffles with strawberries", bob, "everywhere")

    session.add(alice)
    session.add(bob)

    session.add(art1)
    session.add(art2)
    session.add(art3)
    session.add(art4)
    session.add(art5)

    session.commit()
    session.close()

def create_db():
    Base.metadata.create_all(engine)