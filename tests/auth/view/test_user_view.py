from json import dumps, loads

from tcas.auth.model import User


def test_get_user_404(app):
    with app.test_client() as client:
        res = client.get(
            path='/auth/user/404'
        )
        assert res.status_code == 404


def test_post_user(app):
    with app.test_client() as client:
        res = client.post(
            path='/auth/user/',
            headers=[('Content-Type', 'application/json')],
            data=dumps({
                'email': 'test_user_view@test.biz',
                'password': '123456'
            })
        )
        assert res.status_code == 201 and loads(res.data).get('token') is not None


def test_get_users(app):
    with app.test_client() as client:
        res = client.get(
            path='/auth/user/'
        )
        assert res.status_code == 200


def test_get_user(app, session):
    _id = session.query(User).first().id
    with app.test_client() as client:
        res = client.get(
            path='/auth/user/' + _id
        )
        assert res.status_code == 200


# def test_put_user(app, session):
#     user = session.query(User).first()
#     _id = user.id
#     email = user.email
#     with app.test_client() as client:
#         res = client.put(
#             path='/auth/user/' + _id,
#             headers=[('Content-Type', 'application/json')],
#             data=dumps({
#                 'key': 'email',
#                 'new_value': 'test_user_view_UPDATED@test.biz',
#                 'old_value': 'test_user_view@test.biz',
#                 'password': '123456'
#             })
#         )
#         assert res.status_code == 202 and loads(res.data).get('email') != email


def test_delete_user(app, session):
    _id = User.query.filter_by(email='test_user_view@test.biz').first().id
    with app.test_client() as client:
        res = client.delete(
            path='/auth/user/' + _id,
            headers=[('Content-Type', 'application/json')],
            data=dumps({'password': '123456'})
        )
        assert res.status_code == 202
