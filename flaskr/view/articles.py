import functools
import json

from flaskr.dto.dto_article import DtoArticleInfo
from ..service import service_article

from ..authent import auth

#from db import Session, engine, Base
#from model.article import Article

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('articles', __name__, url_prefix='/articles')

@bp.route('/test-article')
def test_article():
    return '[{ "title" : "nice boy", "author" : "Bob" }]'

@bp.route('/<int:id>')
@auth.login_required
def article(id):
    return service_article.get_article(id)

@bp.route('')
@auth.login_required
def all_articles():

    #Base.metadata.create_all(engine)
    ##session = Session()
    #article = Article('When you were young', 'Killers')
    #article2 = Article('Here comes the rain', 'Benjamin')
    #session.add(article)
    #session.add(article2)
    #session.commit()

    ##arts = session.query(Article).all()

    ##arS = json.dumps([ob.__dict__ for ob in arts])

    #for ar in arts:
        #arS(f'{{\"id\":{ar.id},\"title\":{ar.title}, \"author\":{ar.author}' + '},')
    

    ##session.close()

    return service_article.get_articles()

@bp.route('', methods = ['POST'])
@auth.login_required
def add_article():

    j_data = request.get_json(force=True)
    article = service_article.add_article(DtoArticleInfo(j_data['title'], auth.username(), j_data['content']))
    return json.dumps(article)

@bp.route('/<int:id>', methods = ['PUT'])
@auth.login_required
def update_article(id):

    j_data = request.get_json(force=True)
    article = service_article.update_article(DtoArticleInfo(j_data['title'], auth.username(), j_data['content'], id))
    return json.dumps(article)