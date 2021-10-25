from connection import *
from werkzeug.security import check_password_hash
class User(object):
    def __init__(self, id, username, password, namae):
        self.id = id
        self.username = username
        self.password = password
        self.namae = namae

    def __str__(self):
        return ["%s","%s","%s"] % (self.id, self.username, self.namae)

def user_fetch():
    cur.execute('SELECT id, username, useremail, namae, password_digest FROM users;')
    results = cur.fetchall()
    result = [User(u[0], u[1], u[4], u[3]) for u in results]
    return result

def authenticate(username, password):
    result = user_fetch()
    usernames = {u.username: u for u in result}
    user = usernames.get(username, None)
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    result = user_fetch()
    user_id = payload['identity']
    userids = {u.id: u for u in result}
    return userids.get(user_id, None)