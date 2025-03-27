from users import User
import db_config


def access_db():
    """DBにアクセスする
    """

    session = db_config.session_local()
    user = User(username='taro yamada', email='taro_yamada@example.com')
    session.add(user)
    session.commit()

    users = session.query(User).all()
    for user in users:
        print(user)


if __name__ == '__main__':
    access_db()
