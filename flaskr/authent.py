from flask import Flask, g
from flask_httpauth import HTTPBasicAuth

from service import service_user

auth = HTTPBasicAuth()

@auth.verify_password
def verify_pw(username, password):
    user = service_user.get_user_by_name(username)
    if user is not None and user.check_password(password) :
        g.current_user = user
        return True
    return False