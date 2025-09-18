#!/usr/bin/env python3
"""
MÓDULO EXTERNO: sqlalchemy
==========================

¿QUÉ ES?
SQLAlchemy es el ORM (Object-Relational Mapping) más popular de Python.
Permite trabajar con bases de datos usando objetos Python en lugar de SQL.

INSTALACIÓN:
pip install sqlalchemy

¿PARA QUÉ SIRVE?
- Mapear tablas a clases Python
- Consultas con objetos en lugar de SQL
- Relaciones entre tablas
- Migraciones de base de datos
- Conexiones múltiples a BD
- Abstracción de diferentes BD

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para BD)
"""

def verificar_instalacion():
    """Verificar si sqlalchemy está instalado"""
    try:
        import sqlalchemy
        print("✅ Módulo 'sqlalchemy' instalado correctamente")
        print(f"📦 Versión: {sqlalchemy.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'sqlalchemy' no encontrado")
        print("💡 Para instalar: pip install sqlalchemy")
        return False

def ejemplo_sqlalchemy_basico():
    """Ejemplo básico de SQLAlchemy"""
    
    print("=" * 50)
    print("🗄️ MÓDULO SQLALCHEMY - ORM")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    print("\n📝 Ejemplo básico - Definir modelo:")
    print("""
# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000))
    created_at = Column(DateTime, default=datetime.utcnow)
    priority = Column(String(20), default='Media')
    
    def __repr__(self):
        return f"<Note(title='{self.title}', priority='{self.priority}')>"

# Crear conexión a base de datos
engine = create_engine('sqlite:///notes.db', echo=True)
Base.metadata.create_all(engine)

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()
    """)
    
    print("\n✅ Conceptos clave:")
    print("   • Base = declarative_base(): Clase base para modelos")
    print("   • Column(): Definir columnas")
    print("   • create_engine(): Conexión a BD")
    print("   • sessionmaker(): Crear sesiones")
    print("   • __tablename__: Nombre de tabla")

def ejemplo_sqlalchemy_crud():
    """Ejemplo de operaciones CRUD con SQLAlchemy"""
    
    print("\n" + "=" * 50)
    print("📝 OPERACIONES CRUD CON SQLALCHEMY")
    print("=" * 50)
    
    print("📝 CREATE - Crear registros:")
    print("""
# Crear una nota
nueva_nota = Note(
    title="Mi primera nota",
    content="Contenido de la nota",
    priority="Alta"
)

# Agregar a sesión
session.add(nueva_nota)

# Guardar en base de datos
session.commit()

# Crear múltiples notas
notas = [
    Note(title="Nota 1", content="Contenido 1", priority="Media"),
    Note(title="Nota 2", content="Contenido 2", priority="Baja"),
    Note(title="Nota 3", content="Contenido 3", priority="Alta")
]

session.add_all(notas)
session.commit()
    """)
    
    print("\n📝 READ - Leer registros:")
    print("""
# Obtener todas las notas
todas_notas = session.query(Note).all()

# Obtener nota por ID
nota = session.query(Note).filter_by(id=1).first()

# Filtrar por prioridad
notas_altas = session.query(Note).filter(Note.priority == 'Alta').all()

# Buscar en título
notas_busqueda = session.query(Note).filter(
    Note.title.like('%palabra%')
).all()

# Ordenar
notas_ordenadas = session.query(Note).order_by(Note.created_at.desc()).all()

# Limitar resultados
primeras_5 = session.query(Note).limit(5).all()
    """)
    
    print("\n📝 UPDATE - Actualizar registros:")
    print("""
# Actualizar una nota específica
nota = session.query(Note).filter_by(id=1).first()
if nota:
    nota.title = "Título actualizado"
    nota.priority = "Baja"
    session.commit()

# Actualizar múltiples registros
session.query(Note).filter(Note.priority == 'Media').update({
    Note.priority: 'Alta'
})
session.commit()
    """)
    
    print("\n📝 DELETE - Eliminar registros:")
    print("""
# Eliminar una nota específica
nota = session.query(Note).filter_by(id=1).first()
if nota:
    session.delete(nota)
    session.commit()

# Eliminar múltiples registros
session.query(Note).filter(Note.priority == 'Baja').delete()
session.commit()
    """)

def ejemplo_sqlalchemy_relaciones():
    """Ejemplo de relaciones entre modelos"""
    
    print("\n" + "=" * 50)
    print("🔗 RELACIONES ENTRE MODELOS")
    print("=" * 50)
    
    print("📝 Definir relaciones:")
    print("""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    
    # Relación uno a muchos con notas
    notes = relationship("Note", back_populates="user")

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Relación muchos a uno con usuario
    user = relationship("User", back_populates="notes")

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    
    # Relación muchos a muchos con notas
    notes = relationship("Note", secondary="note_tags", back_populates="tags")

# Tabla de asociación para relación muchos a muchos
from sqlalchemy import Table

note_tags = Table('note_tags', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

# Agregar relación a Note
class Note(Base):
    # ... campos existentes ...
    tags = relationship("Tag", secondary=note_tags, back_populates="notes")
    """)
    
    print("\n📝 Usar relaciones:")
    print("""
# Crear usuario con notas
usuario = User(username="jose", email="jose@example.com")
session.add(usuario)
session.commit()

# Crear nota asociada al usuario
nota = Note(
    title="Nota de José",
    content="Contenido",
    user=usuario
)
session.add(nota)
session.commit()

# Acceder a notas del usuario
print(f"Notas de {usuario.username}:")
for nota in usuario.notes:
    print(f"  - {nota.title}")

# Acceder al usuario de una nota
print(f"Autor de la nota: {nota.user.username}")
    """)

def ejemplo_sqlalchemy_consultas_avanzadas():
    """Ejemplo de consultas avanzadas"""
    
    print("\n" + "=" * 50)
    print("🚀 CONSULTAS AVANZADAS")
    print("=" * 50)
    
    print("📝 Joins y agregaciones:")
    print("""
from sqlalchemy import func, and_, or_

# Join entre tablas
notas_con_usuario = session.query(Note, User).join(User).all()

# Contar notas por usuario
conteo = session.query(
    User.username,
    func.count(Note.id).label('total_notas')
).join(Note).group_by(User.username).all()

# Filtros complejos
notas_filtradas = session.query(Note).filter(
    and_(
        Note.priority == 'Alta',
        Note.created_at > datetime(2024, 1, 1)
    )
).all()

# Subconsultas
usuarios_activos = session.query(User).filter(
    User.id.in_(
        session.query(Note.user_id).distinct()
    )
).all()

# Consultas con exists
usuarios_con_notas = session.query(User).filter(
    User.notes.any(Note.priority == 'Alta')
).all()
    """)
    
    print("\n📝 Agregaciones y estadísticas:")
    print("""
# Estadísticas por prioridad
stats = session.query(
    Note.priority,
    func.count(Note.id).label('cantidad'),
    func.avg(func.length(Note.content)).label('longitud_promedio')
).group_by(Note.priority).all()

# Nota más reciente por usuario
notas_recientes = session.query(Note).filter(
    Note.id.in_(
        session.query(func.max(Note.id)).group_by(Note.user_id)
    )
).all()
    """)

def ejemplo_sqlalchemy_clase_completa():
    """Ejemplo de clase completa con SQLAlchemy"""
    
    print("\n" + "=" * 50)
    print("🏗️ CLASE COMPLETA NOTESASSISTANT")
    print("=" * 50)
    
    print("📝 Integración completa:")
    print("""
# database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000))
    priority = Column(String(20), default='Media')
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def __repr__(self):
        return f"<Note(id={self.id}, title='{self.title}')>"

class NoteService:
    def __init__(self, db_path="notes.db"):
        self.engine = create_engine(f'sqlite:///{db_path}', echo=False)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def create_note(self, title, content, priority="Media"):
        note = Note(title=title, content=content, priority=priority)
        self.session.add(note)
        self.session.commit()
        return note
    
    def get_all_notes(self):
        return self.session.query(Note).all()
    
    def get_note_by_id(self, note_id):
        return self.session.query(Note).filter_by(id=note_id).first()
    
    def update_note(self, note_id, **kwargs):
        note = self.get_note_by_id(note_id)
        if note:
            for key, value in kwargs.items():
                setattr(note, key, value)
            note.updated_at = datetime.utcnow()
            self.session.commit()
            return note
        return None
    
    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.session.delete(note)
            self.session.commit()
            return True
        return False
    
    def search_notes(self, query):
        return self.session.query(Note).filter(
            Note.title.like(f'%{query}%') |
            Note.content.like(f'%{query}%')
        ).all()
    
    def get_notes_by_priority(self, priority):
        return self.session.query(Note).filter_by(priority=priority).all()
    
    def close(self):
        self.session.close()

# Ejemplo de uso
if __name__ == "__main__":
    service = NoteService()
    
    # Crear nota
    nota = service.create_note("Mi nota", "Contenido de prueba", "Alta")
    print(f"Nota creada: {nota}")
    
    # Obtener todas las notas
    notas = service.get_all_notes()
    print(f"Total notas: {len(notas)}")
    
    # Buscar notas
    resultados = service.search_notes("prueba")
    print(f"Resultados búsqueda: {len(resultados)}")
    
    service.close()
    """)

def integracion_con_notesassistant():
    """Ejemplo de integración con proyecto notesAssistant"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Estructura recomendada:")
    print("""
notesAssistant/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py         # Base de SQLAlchemy
│   │   └── note.py         # Modelo Note
│   ├── services/
│   │   ├── __init__.py
│   │   └── note_service.py # Servicio con SQLAlchemy
│   └── database/
│       ├── __init__.py
│       ├── connection.py   # Configuración BD
│       └── migrations/     # Migraciones
├── alembic/                # Migraciones
├── alembic.ini
└── requirements.txt
    """)
    
    print("\n🔧 Migración desde archivos:")
    print("""
# migration_script.py
from src.services.note_service import NoteService
import json

def migrate_from_json():
    service = NoteService()
    
    # Leer datos existentes
    with open('notes.json', 'r') as f:
        old_notes = json.load(f)
    
    # Migrar a SQLAlchemy
    for note_data in old_notes:
        service.create_note(
            title=note_data['title'],
            content=note_data['content'],
            priority=note_data.get('priority', 'Media')
        )
    
    print(f"Migradas {len(old_notes)} notas")
    service.close()

if __name__ == "__main__":
    migrate_from_json()
    """)
    
    print("\n🚀 Ventajas de usar SQLAlchemy:")
    print("   • Persistencia robusta")
    print("   • Consultas complejas fáciles")
    print("   • Relaciones entre datos")
    print("   • Migraciones automáticas")
    print("   • Múltiples bases de datos")
    print("   • Transacciones ACID")

def casos_uso_comunes():
    """Casos de uso más comunes de SQLAlchemy"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Definir modelo:")
    print("   class User(Base):")
    print("       __tablename__ = 'users'")
    print("       id = Column(Integer, primary_key=True)")
    
    print("\n2. Crear sesión:")
    print("   engine = create_engine('sqlite:///app.db')")
    print("   Session = sessionmaker(bind=engine)")
    print("   session = Session()")
    
    print("\n3. Consultas básicas:")
    print("   users = session.query(User).all()")
    print("   user = session.query(User).filter_by(id=1).first()")
    
    print("\n4. Insertar datos:")
    print("   user = User(name='Juan')")
    print("   session.add(user)")
    print("   session.commit()")
    
    print("\n5. Actualizar:")
    print("   user.name = 'Juan Carlos'")
    print("   session.commit()")
    
    print("\n6. Eliminar:")
    print("   session.delete(user)")
    print("   session.commit()")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_sqlalchemy_basico()
    ejemplo_sqlalchemy_crud()
    ejemplo_sqlalchemy_relaciones()
    ejemplo_sqlalchemy_consultas_avanzadas()
    ejemplo_sqlalchemy_clase_completa()
    casos_uso_comunes()
    integracion_con_notesassistant()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO sqlalchemy")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • ORM para bases de datos")
    print("   • Consultas con objetos Python")
    print("   • Relaciones entre tablas")
    print("   • Migraciones automáticas")
    print("   • Abstracción de BD")
    print("   • Transacciones seguras")
    print("\n📚 Documentación oficial:")
    print("   https://docs.sqlalchemy.org/")
    print("\n💡 Consejo: SQLAlchemy es poderoso pero complejo")
    print("   Aprende paso a paso, empezando por lo básico.") 