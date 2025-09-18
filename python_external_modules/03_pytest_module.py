#!/usr/bin/env python3
"""
MÓDULO EXTERNO: pytest
======================

¿QUÉ ES?
El módulo 'pytest' es el framework de testing más popular y potente 
de Python. Hace que escribir y ejecutar tests sea simple y efectivo.

INSTALACIÓN:
pip install pytest

¿PARA QUÉ SIRVE?
- Escribir unit tests de forma simple
- Ejecutar tests automáticamente
- Generar reportes de cobertura
- Fixtures para setup/teardown
- Parametrización de tests
- Mocking y stubbing

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para calidad)
"""

def verificar_instalacion():
    """Verificar si pytest está instalado"""
    try:
        import pytest
        print("✅ Módulo 'pytest' instalado correctamente")
        print(f"📦 Versión: {pytest.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'pytest' no encontrado")
        print("💡 Para instalar: pip install pytest")
        return False

def ejemplo_funciones_para_testing():
    """Funciones de ejemplo para hacer testing"""
    
    print("=" * 50)
    print("🧪 FUNCIONES PARA TESTING")
    print("=" * 50)
    
    # Simular funciones del proyecto notesAssistant
    
    class Note:
        """Clase simple para representar una nota"""
        def __init__(self, title, content, priority="Media"):
            self.title = title
            self.content = content
            self.priority = priority
            self.completed = False
        
        def mark_completed(self):
            self.completed = True
        
        def update_content(self, new_content):
            if not new_content.strip():
                raise ValueError("El contenido no puede estar vacío")
            self.content = new_content
        
        def __str__(self):
            return f"Nota: {self.title} - {self.priority}"
    
    def calcular_promedio(numeros):
        """Calcular promedio de una lista de números"""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        return sum(numeros) / len(numeros)
    
    def validar_email(email):
        """Validar formato básico de email"""
        if "@" not in email or "." not in email:
            return False
        return True
    
    def contar_palabras(texto):
        """Contar palabras en un texto"""
        if not texto:
            return 0
        return len(texto.split())
    
    print("✅ Funciones definidas para testing:")
    print("   • Note (clase)")
    print("   • calcular_promedio()")
    print("   • validar_email()")
    print("   • contar_palabras()")
    
    return Note, calcular_promedio, validar_email, contar_palabras

def ejemplo_tests_basicos():
    """Ejemplo de tests básicos con pytest"""
    
    print("\n" + "=" * 50)
    print("🧪 TESTS BÁSICOS CON PYTEST")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    # Importar pytest
    import pytest
    
    # Obtener funciones para testing
    Note, calcular_promedio, validar_email, contar_palabras = ejemplo_funciones_para_testing()
    
    # NOTA: En un archivo real, estos tests irían en archivos separados
    # Por ejemplo: test_notes.py, test_utils.py, etc.
    
    print("\n📝 Ejemplo de tests que escribirías:")
    print("""
# test_notes.py
import pytest
from notes import Note, calcular_promedio, validar_email, contar_palabras

def test_crear_nota():
    nota = Note("Mi nota", "Contenido de prueba")
    assert nota.title == "Mi nota"
    assert nota.content == "Contenido de prueba"
    assert nota.priority == "Media"
    assert nota.completed == False

def test_marcar_completada():
    nota = Note("Test", "Contenido")
    nota.mark_completed()
    assert nota.completed == True

def test_actualizar_contenido():
    nota = Note("Test", "Contenido original")
    nota.update_content("Nuevo contenido")
    assert nota.content == "Nuevo contenido"

def test_actualizar_contenido_vacio():
    nota = Note("Test", "Contenido")
    with pytest.raises(ValueError):
        nota.update_content("")

def test_calcular_promedio():
    assert calcular_promedio([1, 2, 3, 4, 5]) == 3.0
    assert calcular_promedio([10, 20]) == 15.0

def test_calcular_promedio_lista_vacia():
    with pytest.raises(ValueError):
        calcular_promedio([])

def test_validar_email():
    assert validar_email("test@example.com") == True
    assert validar_email("usuario@dominio.org") == True
    assert validar_email("email_invalido") == False
    assert validar_email("sin_arroba.com") == False

def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("Una sola palabra") == 3
    assert contar_palabras("") == 0
    assert contar_palabras("Python es genial") == 3
    """)
    
    print("\n🚀 Para ejecutar los tests:")
    print("   pytest test_notes.py")
    print("   pytest test_notes.py -v  # Verbose")
    print("   pytest test_notes.py::test_crear_nota  # Test específico")

def ejemplo_fixtures():
    """Ejemplo de fixtures en pytest"""
    
    print("\n" + "=" * 50)
    print("🔧 FIXTURES EN PYTEST")
    print("=" * 50)
    
    print("💡 Fixtures: Setup y teardown automático para tests")
    
    print("""
# test_with_fixtures.py
import pytest
from notes import Note

@pytest.fixture
def nota_ejemplo():
    '''Fixture que crea una nota de ejemplo'''
    return Note("Nota de prueba", "Contenido de ejemplo", "Alta")

@pytest.fixture
def lista_notas():
    '''Fixture que crea una lista de notas'''
    return [
        Note("Nota 1", "Contenido 1", "Alta"),
        Note("Nota 2", "Contenido 2", "Media"),
        Note("Nota 3", "Contenido 3", "Baja")
    ]

def test_nota_con_fixture(nota_ejemplo):
    '''Test que usa fixture'''
    assert nota_ejemplo.title == "Nota de prueba"
    assert nota_ejemplo.priority == "Alta"

def test_lista_con_fixture(lista_notas):
    '''Test que usa fixture de lista'''
    assert len(lista_notas) == 3
    assert lista_notas[0].priority == "Alta"
    assert all(isinstance(nota, Note) for nota in lista_notas)

@pytest.fixture(scope="module")
def base_datos_temporal():
    '''Fixture que simula setup de base de datos'''
    print("\\n🔧 Configurando base de datos temporal...")
    # Setup
    db = {"notas": []}
    yield db  # Esto es lo que recibe el test
    # Teardown
    print("\\n🧹 Limpiando base de datos temporal...")
    db.clear()

def test_con_base_datos(base_datos_temporal):
    '''Test que usa base de datos temporal'''
    db = base_datos_temporal
    db["notas"].append({"id": 1, "titulo": "Test"})
    assert len(db["notas"]) == 1
    """)
    
    print("\n✅ Beneficios de fixtures:")
    print("   • Reutilización de código de setup")
    print("   • Limpieza automática (teardown)")
    print("   • Diferentes scopes (function, class, module)")
    print("   • Dependency injection automática")

def ejemplo_parametrizacion():
    """Ejemplo de parametrización en pytest"""
    
    print("\n" + "=" * 50)
    print("🔄 PARAMETRIZACIÓN EN PYTEST")
    print("=" * 50)
    
    print("💡 Parametrización: Ejecutar el mismo test con diferentes datos")
    
    print("""
# test_parametrized.py
import pytest
from notes import validar_email, contar_palabras

@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("usuario@dominio.org", True),
    ("email_invalido", False),
    ("sin_arroba.com", False),
    ("@dominio.com", False),
    ("usuario@", False),
])
def test_validar_email_parametrizado(email, expected):
    assert validar_email(email) == expected

@pytest.mark.parametrize("texto,palabras_esperadas", [
    ("Hola mundo", 2),
    ("Una sola palabra", 3),
    ("", 0),
    ("Python es genial", 3),
    ("a b c d e", 5),
])
def test_contar_palabras_parametrizado(texto, palabras_esperadas):
    assert contar_palabras(texto) == palabras_esperadas

@pytest.mark.parametrize("prioridad", ["Alta", "Media", "Baja"])
def test_crear_nota_diferentes_prioridades(prioridad):
    nota = Note("Test", "Contenido", prioridad)
    assert nota.priority == prioridad
    """)
    
    print("\n✅ Ventajas de parametrización:")
    print("   • Un test, múltiples casos")
    print("   • Reporte claro de qué caso falló")
    print("   • Código más limpio y mantenible")
    print("   • Fácil agregar nuevos casos")

def ejemplo_mocking():
    """Ejemplo de mocking en pytest"""
    
    print("\n" + "=" * 50)
    print("🎭 MOCKING EN PYTEST")
    print("=" * 50)
    
    print("💡 Mocking: Simular dependencias externas")
    
    print("""
# test_mocking.py
import pytest
from unittest.mock import Mock, patch, MagicMock

# Función que queremos testear
def enviar_email(email, asunto, contenido):
    '''Simula envío de email'''
    import smtplib
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('usuario', 'password')
    servidor.sendmail('from@email.com', email, f"Subject: {asunto}\\n\\n{contenido}")
    servidor.quit()
    return True

def guardar_nota_en_db(nota):
    '''Simula guardado en base de datos'''
    import sqlite3
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notas (titulo, contenido) VALUES (?, ?)", 
                   (nota.title, nota.content))
    conn.commit()
    conn.close()
    return True

# Tests con mocking
@patch('smtplib.SMTP')
def test_enviar_email_mock(mock_smtp):
    '''Test que mockea el servidor SMTP'''
    # Configurar el mock
    mock_server = Mock()
    mock_smtp.return_value = mock_server
    
    # Ejecutar función
    resultado = enviar_email("test@example.com", "Asunto", "Contenido")
    
    # Verificar que se llamó correctamente
    mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with('usuario', 'password')
    mock_server.sendmail.assert_called_once()
    mock_server.quit.assert_called_once()
    
    assert resultado == True

@patch('sqlite3.connect')
def test_guardar_nota_mock(mock_connect):
    '''Test que mockea la base de datos'''
    # Configurar mocks
    mock_conn = Mock()
    mock_cursor = Mock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Crear nota y ejecutar
    nota = Note("Test", "Contenido")
    resultado = guardar_nota_en_db(nota)
    
    # Verificar llamadas
    mock_connect.assert_called_once_with('notas.db')
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()
    
    assert resultado == True
    """)
    
    print("\n✅ Beneficios del mocking:")
    print("   • Tests rápidos (no dependen de servicios externos)")
    print("   • Tests deterministas (siempre el mismo resultado)")
    print("   • Verificar interacciones")
    print("   • Simular errores y casos edge")

def ejemplo_comandos_pytest():
    """Ejemplo de comandos útiles de pytest"""
    
    print("\n" + "=" * 50)
    print("⚡ COMANDOS ÚTILES DE PYTEST")
    print("=" * 50)
    
    print("🚀 Comandos básicos:")
    print("   pytest                    # Ejecutar todos los tests")
    print("   pytest test_file.py       # Ejecutar archivo específico")
    print("   pytest -v                 # Verbose (más detalles)")
    print("   pytest -s                 # Mostrar prints")
    print("   pytest -x                 # Parar en primer fallo")
    print("   pytest --tb=short         # Traceback corto")
    
    print("\n🎯 Comandos avanzados:")
    print("   pytest -k 'test_email'    # Solo tests que contengan 'test_email'")
    print("   pytest -m 'slow'          # Solo tests marcados como 'slow'")
    print("   pytest --collect-only     # Ver qué tests se ejecutarían")
    print("   pytest --lf               # Solo tests que fallaron la última vez")
    print("   pytest --ff               # Ejecutar primero los que fallaron")
    
    print("\n📊 Reportes y cobertura:")
    print("   pytest --cov=src          # Reporte de cobertura")
    print("   pytest --cov-report=html  # Reporte HTML")
    print("   pytest --junit-xml=report.xml  # Reporte XML")
    
    print("\n🔧 Configuración:")
    print("   pytest.ini                # Archivo de configuración")
    print("   conftest.py               # Fixtures compartidas")
    print("   --maxfail=2               # Parar después de 2 fallos")

def integracion_con_notesassistant():
    """Ejemplo de integración con proyecto notesAssistant"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Estructura de tests para tu proyecto:")
    
    print("""
notesAssistant/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── note.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── note_service.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Fixtures compartidas
│   ├── test_models/
│   │   ├── __init__.py
│   │   └── test_note.py
│   ├── test_services/
│   │   ├── __init__.py
│   │   └── test_note_service.py
│   └── test_utils/
│       ├── __init__.py
│       └── test_validators.py
├── pytest.ini
└── requirements-dev.txt
    """)
    
    print("\n📝 Ejemplos de tests para tu proyecto:")
    print("""
# tests/test_models/test_note.py
def test_crear_nota():
    nota = Note("Mi nota", "Contenido")
    assert nota.title == "Mi nota"
    assert nota.content == "Contenido"

# tests/test_services/test_note_service.py
def test_guardar_nota(tmp_path):
    service = NoteService(tmp_path)
    nota = Note("Test", "Contenido")
    id_nota = service.save(nota)
    assert id_nota is not None

# tests/test_utils/test_validators.py
def test_validar_titulo():
    assert validar_titulo("Título válido") == True
    assert validar_titulo("") == False
    """)
    
    print("\n🔧 Configuración recomendada:")
    print("""
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --strict-markers
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    """)
    
    print("\n🚀 Comandos para tu proyecto:")
    print("   pytest tests/                    # Todos los tests")
    print("   pytest tests/test_models/        # Solo tests de modelos")
    print("   pytest -m 'not slow'             # Excluir tests lentos")
    print("   pytest --cov=src                 # Cobertura de código")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_funciones_para_testing()
    ejemplo_tests_basicos()
    ejemplo_fixtures()
    ejemplo_parametrizacion()
    ejemplo_mocking()
    ejemplo_comandos_pytest()
    integracion_con_notesassistant()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO pytest")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Escribir unit tests simples")
    print("   • Fixtures para setup/teardown")
    print("   • Parametrización de tests")
    print("   • Mocking de dependencias")
    print("   • Reportes de cobertura")
    print("   • Ejecución selectiva de tests")
    print("\n📚 Documentación oficial:")
    print("   https://docs.pytest.org/")
    print("\n💡 Consejo: pytest hace testing divertido")
    print("   Es la herramienta estándar para testing en Python.") 