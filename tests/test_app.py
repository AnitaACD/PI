def test_import_app():
    import sys
    sys.path.insert(0, 'SistemaGestion_2')
    from app import app
    assert app is not None

def test_login_route():
    import sys
    sys.path.insert(0, 'SistemaGestion_2')
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
