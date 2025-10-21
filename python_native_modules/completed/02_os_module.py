#!/usr/bin/env python3
"""
MÓDULO NATIVO: os
================

¿QUÉ ES?
El módulo 'os' significa "operating system" y proporciona funciones para interactuar con el sistema operativo.
Permite trabajar con archivos, directorios, variables de entorno, y procesos.

¿PARA QUÉ SIRVE?
- Navegar y manipular el sistema de archivos
- Crear, eliminar, renombrar archivos y directorios
- Obtener información del sistema operativo
- Trabajar con variables de entorno
- Ejecutar comandos del sistema

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Muy importante)
"""

import os
import tempfile
from datetime import datetime

def ejemplos_os_basicos():
    """Ejemplos básicos del módulo os"""
    
    print("=" * 50)
    print("💻 MÓDULO OS - SISTEMA OPERATIVO")
    print("=" * 50)
    
    # 1. DIRECTORIO ACTUAL
    print("\n1️⃣ DIRECTORIO ACTUAL:")
    directorio_actual = os.getcwd()
    print(f"   Directorio actual: {directorio_actual}")
    
    # 2. INFORMACIÓN DEL SISTEMA
    print("\n2️⃣ INFORMACIÓN DEL SISTEMA:")
    print(f"   Nombre del OS: {os.name}")  # 'posix' (Linux/Mac) o 'nt' (Windows)
    print(f"   Separador de rutas: '{os.sep}'")  # '/' en Linux/Mac, '\' en Windows
    print(f"   Usuario actual: {os.getenv('USER', 'No disponible')}")
    print(f"   Directorio home: {os.path.expanduser('~')}")
    
    # 3. VARIABLES DE ENTORNO
    print("\n3️⃣ VARIABLES DE ENTORNO:")
    print(f"   PATH: {os.environ.get('PATH', 'No encontrado')[:50]}...")
    print(f"   PYTHON_PATH: {os.environ.get('PYTHONPATH', 'No definido')}")
    print(f"   HOME: {os.environ.get('HOME', 'No disponible')}")
    
    # 4. LISTAR ARCHIVOS
    print("\n4️⃣ LISTAR ARCHIVOS EN DIRECTORIO ACTUAL:")
    try:
        archivos = os.listdir('.')
        print(f"   Encontrados {len(archivos)} elementos:")
        for i, archivo in enumerate(archivos[:5]):  # Solo primeros 5
            print(f"   [{i+1}] {archivo}")
        if len(archivos) > 5:
            print(f"   ... y {len(archivos) - 5} más")
    except PermissionError:
        print("   ❌ Sin permisos para listar este directorio")

def ejemplos_os_paths():
    """Ejemplos de manipulación de rutas con os.path"""
    
    print("\n" + "=" * 50)
    print("📁 MÓDULO OS.PATH - MANIPULACIÓN DE RUTAS")
    print("=" * 50)
    
    # Ejemplo de ruta
    ruta_ejemplo = "/home/jose/My_Projects/notesAssistant/run.py"
    
    print(f"🔧 Ruta de ejemplo: {ruta_ejemplo}")
    
    # 1. INFORMACIÓN DE LA RUTA
    print("\n1️⃣ INFORMACIÓN DE LA RUTA:")
    print(f"   Directorio padre: {os.path.dirname(ruta_ejemplo)}")
    print(f"   Nombre del archivo: {os.path.basename(ruta_ejemplo)}")
    print(f"   Separar en (dir, file): {os.path.split(ruta_ejemplo)}")
    print(f"   Separar extensión: {os.path.splitext(ruta_ejemplo)}")
    
    # 2. VERIFICACIONES
    print("\n2️⃣ VERIFICACIONES:")
    print(f"   ¿Existe? {os.path.exists(ruta_ejemplo)}")
    print(f"   ¿Es archivo? {os.path.isfile(ruta_ejemplo)}")
    print(f"   ¿Es directorio? {os.path.isdir(ruta_ejemplo)}")
    print(f"   ¿Es absoluta? {os.path.isabs(ruta_ejemplo)}")
    
    # 3. CONSTRUCCIÓN DE RUTAS
    print("\n3️⃣ CONSTRUCCIÓN DE RUTAS:")
    nueva_ruta = os.path.join("mi_proyecto", "src", "main.py")
    print(f"   os.path.join('mi_proyecto', 'src', 'main.py')")
    print(f"   Resultado: {nueva_ruta}")
    
    # 4. RUTAS ABSOLUTAS Y RELATIVAS
    print("\n4️⃣ RUTAS ABSOLUTAS Y RELATIVAS:")
    ruta_relativa = "archivo.txt"
    ruta_absoluta = os.path.abspath(ruta_relativa)
    print(f"   Relativa: {ruta_relativa}")
    print(f"   Absoluta: {ruta_absoluta}")

def ejemplos_os_operaciones_archivos():
    """Ejemplos de operaciones con archivos y directorios"""
    
    print("\n" + "=" * 50)
    print("🗂️ OPERACIONES CON ARCHIVOS Y DIRECTORIOS")
    print("=" * 50)
    
    # Crear directorio temporal para ejemplos
    directorio_temporal = tempfile.mkdtemp()
    print(f"🔧 Directorio temporal: {directorio_temporal}")
    
    try:
        # 1. CREAR DIRECTORIO
        print("\n1️⃣ CREAR DIRECTORIO:")
        nuevo_directorio = os.path.join(directorio_temporal, "mi_carpeta")
        os.mkdir(nuevo_directorio)
        print(f"   ✅ Creado: {nuevo_directorio}")
        
        # 2. CREAR ARCHIVO
        print("\n2️⃣ CREAR ARCHIVO:")
        nuevo_archivo = os.path.join(nuevo_directorio, "ejemplo.txt")
        with open(nuevo_archivo, 'w') as f:
            f.write("Hola, este es un archivo de ejemplo")
        print(f"   ✅ Creado: {nuevo_archivo}")
        
        # 3. OBTENER INFORMACIÓN DEL ARCHIVO
        print("\n3️⃣ INFORMACIÓN DEL ARCHIVO:")
        stats = os.stat(nuevo_archivo)
        print(f"   Tamaño: {stats.st_size} bytes")
        print(f"   Modificado: {datetime.fromtimestamp(stats.st_mtime)}")
        print(f"   Permisos: {oct(stats.st_mode)[-3:]}")
        
        # 4. LISTAR CONTENIDO
        print("\n4️⃣ LISTAR CONTENIDO:")
        contenido = os.listdir(nuevo_directorio)
        print(f"   Contenido de {os.path.basename(nuevo_directorio)}: {contenido}")
        
        # 5. RENOMBRAR ARCHIVO
        print("\n5️⃣ RENOMBRAR ARCHIVO:")
        archivo_renombrado = os.path.join(nuevo_directorio, "ejemplo_renombrado.txt")
        os.rename(nuevo_archivo, archivo_renombrado)
        print(f"   ✅ Renombrado a: {os.path.basename(archivo_renombrado)}")
        
        # 6. ELIMINAR ARCHIVO
        print("\n6️⃣ ELIMINAR ARCHIVO:")
        os.remove(archivo_renombrado)
        print(f"   ✅ Eliminado: {os.path.basename(archivo_renombrado)}")
        
        # 7. ELIMINAR DIRECTORIO
        print("\n7️⃣ ELIMINAR DIRECTORIO:")
        os.rmdir(nuevo_directorio)
        print(f"   ✅ Eliminado: {os.path.basename(nuevo_directorio)}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
    finally:
        # Limpiar directorio temporal
        try:
            os.rmdir(directorio_temporal)
        except:
            pass

def ejemplos_os_avanzados():
    """Ejemplos avanzados del módulo os"""
    
    print("\n" + "=" * 50)
    print("🚀 EJEMPLOS AVANZADOS")
    print("=" * 50)
    
    # 1. VARIABLES DE ENTORNO
    print("\n1️⃣ MANIPULAR VARIABLES DE ENTORNO:")
    # Obtener variable existente
    path_actual = os.environ.get('PATH', '')
    print(f"   PATH actual: {path_actual[:50]}...")
    
    # Establecer nueva variable
    os.environ['MI_VARIABLE'] = 'valor_personalizado'
    print(f"   Nueva variable: {os.environ.get('MI_VARIABLE')}")
    
    # 2. EJECUTAR COMANDOS DEL SISTEMA
    print("\n2️⃣ EJECUTAR COMANDOS DEL SISTEMA:")
    print("   💡 os.system('comando') - Ejecuta comando del sistema")
    print("   💡 Mejor usar subprocess para mayor control")
    
    # 3. CAMINAR POR DIRECTORIOS
    print("\n3️⃣ CAMINAR POR DIRECTORIOS:")
    print("   os.walk() - Recorre todos los subdirectorios")
    print("   Ejemplo de uso:")
    print("   for root, dirs, files in os.walk('/ruta'):")
    print("       for file in files:")
    print("           print(os.path.join(root, file))")
    
    # 4. PERMISOS DE ARCHIVOS
    print("\n4️⃣ PERMISOS DE ARCHIVOS:")
    print("   os.chmod(archivo, 0o755)  # Cambiar permisos")
    print("   os.access(archivo, os.R_OK)  # Verificar si se puede leer")
    print("   os.access(archivo, os.W_OK)  # Verificar si se puede escribir")
    print("   os.access(archivo, os.X_OK)  # Verificar si se puede ejecutar")

def casos_uso_comunes():
    """Casos de uso más comunes del módulo os"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Verificar si un archivo existe:")
    print("   if os.path.exists('archivo.txt'):")
    print("       # Procesar archivo")
    
    print("\n2. Crear directorios si no existen:")
    print("   if not os.path.exists('mi_directorio'):")
    print("       os.makedirs('mi_directorio')")
    
    print("\n3. Obtener archivos con extensión específica:")
    print("   archivos_py = [f for f in os.listdir('.') if f.endswith('.py')]")
    
    print("\n4. Construir rutas multiplataforma:")
    print("   ruta = os.path.join('carpeta', 'subcarpeta', 'archivo.txt')")
    
    print("\n5. Obtener directorio del script actual:")
    print("   directorio_script = os.path.dirname(os.path.abspath(__file__))")
    
    print("\n6. Leer variable de entorno con valor por defecto:")
    print("   debug_mode = os.environ.get('DEBUG', 'False')")
    
    print("\n7. Crear archivo temporal:")
    print("   temp_file = tempfile.NamedTemporaryFile(delete=False)")

def ejemplo_practico_completo():
    """Ejemplo práctico completo: Organizador de archivos"""
    
    print("\n" + "=" * 50)
    print("💡 EJEMPLO PRÁCTICO: ORGANIZADOR DE ARCHIVOS")
    print("=" * 50)
    
    def organizar_archivos_por_extension(directorio):
        """Organiza archivos por extensión"""
        
        print(f"📁 Organizando archivos en: {directorio}")
        
        if not os.path.exists(directorio):
            print("   ❌ El directorio no existe")
            return
        
        # Obtener todos los archivos
        archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
        
        if not archivos:
            print("   📭 No hay archivos para organizar")
            return
        
        # Agrupar por extensión
        extensiones = {}
        for archivo in archivos:
            _, ext = os.path.splitext(archivo)
            ext = ext.lower() or '.sin_extension'
            
            if ext not in extensiones:
                extensiones[ext] = []
            extensiones[ext].append(archivo)
        
        # Mostrar resumen
        print("\n   📊 Resumen de archivos encontrados:")
        for ext, lista in extensiones.items():
            print(f"   {ext}: {len(lista)} archivos")
        
        print("\n   💡 Para crear carpetas organizadas:")
        print("   for ext, archivos in extensiones.items():")
        print("       carpeta = os.path.join(directorio, ext[1:])")  # Remover el punto
        print("       os.makedirs(carpeta, exist_ok=True)")
        print("       for archivo in archivos:")
        print("           os.move(os.path.join(directorio, archivo), os.path.join(carpeta, archivo))")
    
    # Ejemplo con directorio actual
    organizar_archivos_por_extension('.')

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplos_os_basicos()
    ejemplos_os_paths()
    ejemplos_os_operaciones_archivos()
    ejemplos_os_avanzados()
    casos_uso_comunes()
    ejemplo_practico_completo()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO os")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Navegar y manipular sistema de archivos")
    print("   • Crear/eliminar archivos y directorios")
    print("   • Obtener información del sistema operativo")
    print("   • Trabajar con variables de entorno")
    print("   • Construir rutas multiplataforma")
    print("\n📚 Documentación oficial:")
    print("   https://docs.python.org/3/library/os.html")
    print("   https://docs.python.org/3/library/os.path.html") 