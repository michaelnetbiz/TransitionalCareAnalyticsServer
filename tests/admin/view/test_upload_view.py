from tcas.admin.model import Upload
from json import dumps, loads


def test_post_upload(app, csv):
    """

    Parameters
    ----------
    app
    csv
    """
    with open(csv, 'rb') as csvfile:
        with app.test_client() as client:
            res = client.post(
                path='/admin/upload/',
                data={
                    'file': csvfile
                },
                headers=[('Content-Type', 'multipart/form-data')]
            )
            assert res.status_code == 201


def test_get_upload(app):
    """

    Parameters
    ----------
    app
    """
    _id = Upload.query.first().id
    with app.test_client() as client:
        res = client.get(
            path='/admin/upload/' + _id
        )
        assert res.status_code == 200 and loads(res.data).get('id') == _id


def test_get_uploads(app):
    """

    Parameters
    ----------
    app
    """
    with app.test_client() as client:
        res = client.get(
            path='/admin/upload/'
        )
        assert res.status_code == 200 and len(loads(res.data)) > 0


def test_get_upload_404(app):
    """

    Parameters
    ----------
    app
    """
    with app.test_client() as client:
        res = client.get(
            path='/admin/upload/404/'
        )
        assert res.status_code == 404


def test_delete_upload(app):
    """

    Parameters
    ----------
    app
    """
    _id = Upload.query.first().id
    with app.test_client() as client:
        res = client.delete(
            path='/admin/upload/' + _id,
            headers=[('Content-Type', 'application/json')],
            data=dumps({'password': '123456'})
        )
        assert res.status_code == 202
