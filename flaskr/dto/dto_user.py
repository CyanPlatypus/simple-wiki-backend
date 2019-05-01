from werkzeug.security import check_password_hash

class DtoUser:
    # def __init__(self, id, name, passw):
    #     self.id = id
    #     self.name = name
    #     self.passw = passw
    #     self.isAdmin = False

    def __init__(self, name, passw):
        
        self.name = name
        self.passw = passw
        self.isAdmin = False

    def check_password (self, passwd):
        return check_password_hash(self.passw, passwd)