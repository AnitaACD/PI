"""
Tests automáticos para CI/CD
Proyecto Integrador — Sistema de Gestión
"""
import sys
import os

# Agregar el directorio padre al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_archivos_esenciales():
    """Verifica que existan los archivos clave del proyecto"""
    base = os.path.join(os.path.dirname(__file__), '..')
    archivos = [
        'app.py',
        'db.py',
        'requirements.txt',
        'Dockerfile',
        'docker-compose.yml',
        '.env.example',
    ]
    for archivo in archivos:
        ruta = os.path.join(base, archivo)
        assert os.path.exists(ruta), f"❌ Falta archivo: {archivo}"
    print("✅ Todos los archivos esenciales existen")


def test_requirements_contiene_flask():
    """Verifica que Flask esté en requirements.txt"""
    base = os.path.join(os.path.dirname(__file__), '..')
    with open(os.path.join(base, 'requirements.txt')) as f:
        contenido = f.read().lower()
    assert 'flask' in contenido, "❌ Flask no está en requirements.txt"
    assert 'pyodbc' in contenido, "❌ pyodbc no está en requirements.txt"
    print("✅ requirements.txt contiene dependencias clave")


def test_docker_compose_servicios():
    """Verifica que docker-compose tenga los servicios necesarios"""
    base = os.path.join(os.path.dirname(__file__), '..')
    with open(os.path.join(base, 'docker-compose.yml')) as f:
        contenido = f.read()
    assert 'flask_app' in contenido,  "❌ Falta servicio flask_app"
    assert 'sqlserver' in contenido,  "❌ Falta servicio sqlserver"
    assert 'volumes:' in contenido,   "❌ Falta configuración de volúmenes"
    assert 'networks:' in contenido,  "❌ Falta configuración de redes"
    assert 'healthcheck' in contenido,"❌ Falta healthcheck en sqlserver"
    print("✅ docker-compose.yml tiene todos los servicios")


def test_db_variables_entorno():
    """Verifica que db.py use variables de entorno"""
    base = os.path.join(os.path.dirname(__file__), '..')
    with open(os.path.join(base, 'db.py')) as f:
        contenido = f.read()
    assert 'os.getenv' in contenido, "❌ db.py no usa variables de entorno"
    assert 'DB_HOST' in contenido,   "❌ db.py no usa DB_HOST"
    print("✅ db.py usa variables de entorno correctamente")


def test_env_example_variables():
    """.env.example tiene las variables necesarias"""
    base = os.path.join(os.path.dirname(__file__), '..')
    with open(os.path.join(base, '.env.example')) as f:
        contenido = f.read()
    vars_requeridas = ['SA_PASSWORD', 'DB_HOST', 'DB_NAME', 'SECRET_KEY']
    for var in vars_requeridas:
        assert var in contenido, f"❌ Falta variable {var} en .env.example"
    print("✅ .env.example tiene todas las variables")


if __name__ == '__main__':
    tests = [
        test_archivos_esenciales,
        test_requirements_contiene_flask,
        test_docker_compose_servicios,
        test_db_variables_entorno,
        test_env_example_variables,
    ]
    
    fallidos = []
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(str(e))
            fallidos.append(test.__name__)
        except Exception as e:
            print(f"❌ Error en {test.__name__}: {e}")
            fallidos.append(test.__name__)
    
    print("\n" + "─"*40)
    print(f"Resultado: {len(tests)-len(fallidos)}/{len(tests)} tests pasaron")
    
    if fallidos:
        print("Tests fallidos:")
        for f in fallidos: print(f"  - {f}")
        sys.exit(1)
    
    print("🎉 Todos los tests pasaron")
    sys.exit(0)
