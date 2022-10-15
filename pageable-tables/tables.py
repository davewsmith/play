from app import create_app


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/tables.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = create_app(Config)


if __name__ == '__main__':
    app.run()
