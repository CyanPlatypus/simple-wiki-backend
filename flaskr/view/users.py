import functools
import json
from flask import request, abort

from ..service import service_user

from ..dto.dto_user import DtoUser

from ..authent import auth

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('users', __name__#, url_prefix='/signup'
)

@bp.route('/signup', methods = ['POST'])
def signup():
    j_data = request.get_json(force=True)
    if not service_user.add_user(DtoUser(j_data['login'], j_data['passw'])) :
        abort(400)
    #return '{"stat":"ok"}'
    return ''


@bp.route('/signin')
@auth.login_required
def signin(): 
    user = service_user.get_user_by_name(auth.username())
    return json.dumps(user.isAdmin)

