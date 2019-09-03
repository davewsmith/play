import uuid

from flask_login import UserMixin

from app import login_manager


USER_DB = dict()


@login_manager.user_loader
def user_loader(user_id):
    return User.get(user_id)


class User(UserMixin):

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = None

    def save(self):
        USER_DB[self.id] = self

    @classmethod
    def get(cls, id):
        return USER_DB.get(id, None)

    @classmethod
    def find_by_email(cls, email):
        for user in USER_DB.values():
            if email == user.email:
                return user
        return None
