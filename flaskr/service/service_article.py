import json

from ..db import Session, engine, Base
from ..model.article import Article
from ..model.user import User
from ..dto.dto_article import DtoArticleInfo

def get_articles():
    session = Session()

    arts = session.query(Article).all()
    arS = json.dumps([( DtoArticleInfo(ob.title, ob.author.name)).__dict__ for ob in arts])

    session.close()

    return arS

def fill():
    create_db()
    session = Session()

    alice = User("alice", "alice")
    bob = User("bob", "bob")

    art1 = Article("badgers are everywhere", alice)
    art2 = Article("soon my prince will come", alice)
    art3 = Article("time managemrnt", bob)
    art4 = Article("true believers", bob)
    art5 = Article("waffles with strawberries", bob)

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