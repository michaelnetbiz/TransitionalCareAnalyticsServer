def test_get_report_404(app):
    with app.test_client() as client:
        res = client.get(path='/admin/report/404/')
        assert res.status_code == 404


def test_get_report(app):
    with app.test_client() as client:
        res = client.get(path='/admin/report/')
        assert res.status_code == 200
