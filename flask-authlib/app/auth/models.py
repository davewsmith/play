from flask_login import UserMixin

from app import login_manager


USER_DB = dict()


@login_manager.user_loader
def user_loader(user_id):
    return User.get(user_id)


class User(UserMixin):

    def __init__(self, name):
        self.id = u'42'
        self.name = name

    def save(self):
        USER_DB[self.id] = self

    @classmethod
    def get(cls, id):
        return USER_DB.get(id, None)
