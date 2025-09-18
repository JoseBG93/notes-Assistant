#!/usr/bin/env python3
"""
MÓDULO EXTERNO: numpy
=====================

¿QUÉ ES?
NumPy es la librería fundamental para computación científica en Python.
Proporciona arrays multidimensionales y operaciones matemáticas rápidas.

INSTALACIÓN:
pip install numpy

¿PARA QUÉ SIRVE?
- Arrays multidimensionales eficientes
- Operaciones matemáticas vectorizadas
- Álgebra lineal básica
- Funciones estadísticas
- Base para pandas, matplotlib, scikit-learn
- Broadcasting automático

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Base de data science)
"""

def verificar_instalacion():
    """Verificar si numpy está instalado"""
    try:
        import numpy as np
        print("✅ Módulo 'numpy' instalado correctamente")
        print(f"📦 Versión: {np.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'numpy' no encontrado")
        print("💡 Para instalar: pip install numpy")
        return False

def ejemplo_numpy_basico():
    """Ejemplo básico de uso de numpy"""
    
    print("=" * 50)
    print("🧮 MÓDULO NUMPY - COMPUTACIÓN CIENTÍFICA")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    import numpy as np
    
    # 1. CREAR ARRAYS
    print("\n1️⃣ CREAR ARRAYS:")
    
    # Array desde lista
    lista = [1, 2, 3, 4, 5]
    array_1d = np.array(lista)
    print(f"   📊 Array 1D: {array_1d}")
    print(f"   📏 Shape: {array_1d.shape}")
    print(f"   🔢 Tipo: {array_1d.dtype}")
    
    # Array 2D (matriz)
    matriz = [[1, 2, 3], [4, 5, 6]]
    array_2d = np.array(matriz)
    print(f"   📊 Array 2D:\n{array_2d}")
    print(f"   📏 Shape: {array_2d.shape}")
    
    # 2. ARRAYS ESPECIALES
    print("\n2️⃣ ARRAYS ESPECIALES:")
    
    # Array de ceros
    zeros = np.zeros((3, 4))
    print(f"   🅾️ Zeros (3x4):\n{zeros}")
    
    # Array de unos
    ones = np.ones((2, 3))
    print(f"   1️⃣ Ones (2x3):\n{ones}")
    
    # Array con rango
    rango = np.arange(0, 10, 2)
    print(f"   📈 Rango [0, 10, paso=2]: {rango}")
    
    # Array con espacio lineal
    linspace = np.linspace(0, 1, 5)
    print(f"   📏 Linspace [0, 1, 5 puntos]: {linspace}")
    
    # 3. INFORMACIÓN DEL ARRAY
    print("\n3️⃣ INFORMACIÓN DEL ARRAY:")
    print(f"   📐 Dimensiones: {array_2d.ndim}")
    print(f"   📏 Shape: {array_2d.shape}")
    print(f"   📊 Tamaño total: {array_2d.size}")
    print(f"   🔢 Tipo de datos: {array_2d.dtype}")
    print(f"   💾 Bytes por elemento: {array_2d.itemsize}")

def ejemplo_numpy_operaciones():
    """Ejemplo de operaciones con numpy"""
    
    print("\n" + "=" * 50)
    print("🔢 OPERACIONES CON NUMPY")
    print("=" * 50)
    
    import numpy as np
    
    # 1. OPERACIONES BÁSICAS
    print("\n1️⃣ OPERACIONES BÁSICAS:")
    
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    
    print(f"   a = {a}")
    print(f"   b = {b}")
    print(f"   a + b = {a + b}")      # Suma elemento a elemento
    print(f"   a - b = {a - b}")      # Resta elemento a elemento
    print(f"   a * b = {a * b}")      # Multiplicación elemento a elemento
    print(f"   a / b = {a / b}")      # División elemento a elemento
    print(f"   a ** 2 = {a ** 2}")    # Potencia
    
    # 2. OPERACIONES CON ESCALARES
    print("\n2️⃣ OPERACIONES CON ESCALARES:")
    
    print(f"   a + 10 = {a + 10}")
    print(f"   a * 3 = {a * 3}")
    print(f"   a > 2 = {a > 2}")      # Comparación booleana
    
    # 3. FUNCIONES MATEMÁTICAS
    print("\n3️⃣ FUNCIONES MATEMÁTICAS:")
    
    datos = np.array([1, 4, 9, 16, 25])
    print(f"   datos = {datos}")
    print(f"   √datos = {np.sqrt(datos)}")
    print(f"   log(datos) = {np.log(datos)}")
    print(f"   sin(datos) = {np.sin(datos)}")
    
    # 4. ESTADÍSTICAS
    print("\n4️⃣ ESTADÍSTICAS:")
    
    numeros = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"   números = {numeros}")
    print(f"   📊 Suma: {np.sum(numeros)}")
    print(f"   📊 Media: {np.mean(numeros)}")
    print(f"   📊 Mediana: {np.median(numeros)}")
    print(f"   📊 Desviación estándar: {np.std(numeros):.2f}")
    print(f"   📊 Mínimo: {np.min(numeros)}")
    print(f"   📊 Máximo: {np.max(numeros)}")

def ejemplo_numpy_indexing():
    """Ejemplo de indexing y slicing en numpy"""
    
    print("\n" + "=" * 50)
    print("🎯 INDEXING Y SLICING")
    print("=" * 50)
    
    import numpy as np
    
    # 1. INDEXING 1D
    print("\n1️⃣ INDEXING 1D:")
    
    arr = np.array([10, 20, 30, 40, 50])
    print(f"   array = {arr}")
    print(f"   arr[0] = {arr[0]}")        # Primer elemento
    print(f"   arr[-1] = {arr[-1]}")      # Último elemento
    print(f"   arr[1:4] = {arr[1:4]}")    # Slice
    
    # 2. INDEXING 2D
    print("\n2️⃣ INDEXING 2D:")
    
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"   matriz =\n{matriz}")
    print(f"   matriz[0, 0] = {matriz[0, 0]}")      # Elemento específico
    print(f"   matriz[1, :] = {matriz[1, ::]}")      # Fila completa
    print(f"   matriz[:, 2] = {matriz[:, 2]}")      # Columna completa
    print(f"   matriz[:2, :2] =\n{matriz[:2, :2]}")  # Submatriz
    
    # 3. INDEXING BOOLEANO
    print("\n3️⃣ INDEXING BOOLEANO:")
    
    datos = np.array([1, 5, 3, 8, 2, 7])
    condicion = datos > 4
    print(f"   datos = {datos}")
    print(f"   datos > 4 = {condicion}")
    print(f"   datos[datos > 4] = {datos[condicion]}")
    
    # Modificar elementos con condición
    datos[datos > 4] = 99
    print(f"   después de datos[datos > 4] = 99: {datos}")

def ejemplo_numpy_reshape():
    """Ejemplo de reshape y manipulación de forma"""
    
    print("\n" + "=" * 50)
    print("🔄 RESHAPE Y MANIPULACIÓN DE FORMA")
    print("=" * 50)
    
    import numpy as np
    
    # 1. RESHAPE
    print("\n1️⃣ RESHAPE:")
    
    original = np.arange(12)
    print(f"   original = {original}")
    print(f"   shape = {original.shape}")
    
    # Cambiar a matriz 3x4
    matriz_3x4 = original.reshape(3, 4)
    print(f"   reshape(3, 4) =\n{matriz_3x4}")
    
    # Cambiar a matriz 2x6
    matriz_2x6 = original.reshape(2, 6)
    print(f"   reshape(2, 6) =\n{matriz_2x6}")
    
    # 2. TRANSPOSE
    print("\n2️⃣ TRANSPOSE:")
    
    print(f"   matriz.T =\n{matriz_3x4.T}")
    
    # 3. FLATTEN
    print("\n3️⃣ FLATTEN:")
    
    plano = matriz_3x4.flatten()
    print(f"   flatten() = {plano}")
    
    # 4. CONCATENAR
    print("\n4️⃣ CONCATENAR ARRAYS:")
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    # Concatenar horizontalmente
    horizontal = np.concatenate([a, b])
    print(f"   concatenate([a, b]) = {horizontal}")
    
    # Stack vertical
    a_2d = a.reshape(1, -1)
    b_2d = b.reshape(1, -1)
    vertical = np.vstack([a_2d, b_2d])
    print(f"   vstack =\n{vertical}")

def ejemplo_numpy_broadcasting():
    """Ejemplo de broadcasting en numpy"""
    
    print("\n" + "=" * 50)
    print("📡 BROADCASTING")
    print("=" * 50)
    
    import numpy as np
    
    print("💡 Broadcasting: Operaciones entre arrays de diferentes shapes")
    
    # 1. SCALAR CON ARRAY
    print("\n1️⃣ SCALAR CON ARRAY:")
    
    arr = np.array([1, 2, 3, 4])
    scalar = 10
    resultado = arr + scalar
    print(f"   {arr} + {scalar} = {resultado}")
    
    # 2. ARRAYS DE DIFERENTES DIMENSIONES
    print("\n2️⃣ ARRAYS DE DIFERENTES DIMENSIONES:")
    
    matriz = np.array([[1, 2, 3], [4, 5, 6]])
    vector = np.array([10, 20, 30])
    
    print(f"   matriz (2x3) =\n{matriz}")
    print(f"   vector (3,) = {vector}")
    
    suma = matriz + vector
    print(f"   matriz + vector =\n{suma}")
    
    # 3. EJEMPLO PRÁCTICO: NORMALIZACIÓN
    print("\n3️⃣ EJEMPLO PRÁCTICO - NORMALIZACIÓN:")
    
    datos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"   datos originales =\n{datos}")
    
    # Calcular media por columna
    media = np.mean(datos, axis=0)
    print(f"   media por columna = {media}")
    
    # Restar media (broadcasting automático)
    datos_centrados = datos - media
    print(f"   datos centrados =\n{datos_centrados}")

def ejemplo_numpy_algebra_lineal():
    """Ejemplo de álgebra lineal básica"""
    
    print("\n" + "=" * 50)
    print("🔢 ÁLGEBRA LINEAL BÁSICA")
    print("=" * 50)
    
    import numpy as np
    
    # 1. PRODUCTO PUNTO
    print("\n1️⃣ PRODUCTO PUNTO:")
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    producto_punto = np.dot(a, b)
    print(f"   a = {a}")
    print(f"   b = {b}")
    print(f"   a · b = {producto_punto}")
    
    # 2. MULTIPLICACIÓN DE MATRICES
    print("\n2️⃣ MULTIPLICACIÓN DE MATRICES:")
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"   A =\n{A}")
    print(f"   B =\n{B}")
    
    producto_matrices = np.dot(A, B)
    print(f"   A × B =\n{producto_matrices}")
    
    # 3. OPERACIONES MATRICIALES
    print("\n3️⃣ OPERACIONES MATRICIALES:")
    
    matriz = np.array([[1, 2], [3, 4]])
    print(f"   matriz =\n{matriz}")
    
    # Determinante
    det = np.linalg.det(matriz)
    print(f"   determinante = {det:.2f}")
    
    # Inversa (si existe)
    if det != 0:
        inversa = np.linalg.inv(matriz)
        print(f"   inversa =\n{inversa}")
    
    # Eigenvalues y eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matriz)
    print(f"   eigenvalues = {eigenvalues}")
    print(f"   eigenvectors =\n{eigenvectors}")

def ejemplo_numpy_arrays_aleatorios():
    """Ejemplo de arrays aleatorios"""
    
    print("\n" + "=" * 50)
    print("🎲 ARRAYS ALEATORIOS")
    print("=" * 50)
    
    import numpy as np
    
    # Fijar semilla para reproducibilidad
    np.random.seed(42)
    
    # 1. NÚMEROS ALEATORIOS
    print("\n1️⃣ NÚMEROS ALEATORIOS:")
    
    # Array aleatorio entre 0 y 1
    aleatorio = np.random.random(5)
    print(f"   random(5) = {aleatorio}")
    
    # Enteros aleatorios
    enteros = np.random.randint(1, 10, size=5)
    print(f"   randint(1, 10, 5) = {enteros}")
    
    # 2. DISTRIBUCIONES
    print("\n2️⃣ DISTRIBUCIONES:")
    
    # Distribución normal
    normal = np.random.normal(0, 1, 5)
    print(f"   normal(μ=0, σ=1, 5) = {normal}")
    
    # Distribución uniforme
    uniforme = np.random.uniform(-1, 1, 5)
    print(f"   uniform(-1, 1, 5) = {uniforme}")
    
    # 3. MATRICES ALEATORIAS
    print("\n3️⃣ MATRICES ALEATORIAS:")
    
    matriz_aleatoria = np.random.random((3, 3))
    print(f"   matriz aleatoria (3x3) =\n{matriz_aleatoria}")
    
    # 4. MUESTREO
    print("\n4️⃣ MUESTREO:")
    
    poblacion = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    muestra = np.random.choice(poblacion, size=3, replace=False)
    print(f"   población = {poblacion}")
    print(f"   muestra (3) = {muestra}")

def integracion_con_notesassistant():
    """Ejemplo de integración con proyecto notesAssistant"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    import numpy as np
    
    print("💡 Usos de NumPy en tu proyecto de notas:")
    
    # 1. ANÁLISIS DE LONGITUD DE NOTAS
    print("\n1️⃣ ANÁLISIS DE LONGITUD DE NOTAS:")
    
    # Simular longitudes de notas
    longitudes_notas = np.array([45, 120, 78, 200, 34, 156, 89, 67, 145, 234])
    
    print(f"   📊 Longitudes: {longitudes_notas}")
    print(f"   📊 Media: {np.mean(longitudes_notas):.1f} caracteres")
    print(f"   📊 Desviación: {np.std(longitudes_notas):.1f}")
    print(f"   📊 Nota más corta: {np.min(longitudes_notas)}")
    print(f"   📊 Nota más larga: {np.max(longitudes_notas)}")
    
    # 2. ANÁLISIS TEMPORAL
    print("\n2️⃣ ANÁLISIS TEMPORAL:")
    
    # Simular notas por día (últimos 30 días)
    notas_por_dia = np.random.poisson(3, 30)  # Media de 3 notas por día
    
    print(f"   📅 Notas últimos 30 días: {notas_por_dia}")
    print(f"   📊 Promedio diario: {np.mean(notas_por_dia):.1f}")
    print(f"   📊 Día más productivo: {np.max(notas_por_dia)} notas")
    print(f"   📊 Días sin notas: {np.sum(notas_por_dia == 0)}")
    
    # 3. CATEGORIZACIÓN AUTOMÁTICA
    print("\n3️⃣ CATEGORIZACIÓN POR LONGITUD:")
    
    # Categorizar notas por longitud
    categorias = np.select(
        [longitudes_notas < 50, longitudes_notas < 100, longitudes_notas < 200],
        ['Corta', 'Media', 'Larga'],
        default='Muy Larga'
    )
    
    for i, (longitud, categoria) in enumerate(zip(longitudes_notas, categorias)):
        print(f"   Nota {i+1}: {longitud} chars → {categoria}")
    
    # 4. DETECCIÓN DE PATRONES
    print("\n4️⃣ DETECCIÓN DE PATRONES:")
    
    # Simular matriz de características de notas
    # Filas = notas, Columnas = [longitud, palabras, párrafos, enlaces]
    caracteristicas = np.array([
        [45, 8, 1, 0],    # Nota corta
        [120, 25, 2, 1],  # Nota media
        [200, 45, 4, 2],  # Nota larga
        [78, 15, 2, 0],   # Nota media
        [300, 60, 6, 3]   # Nota muy larga
    ])
    
    print(f"   📊 Matriz de características (5 notas x 4 features):")
    print(f"   [longitud, palabras, párrafos, enlaces]")
    print(f"{caracteristicas}")
    
    # Análisis estadístico por característica
    print(f"   📊 Promedios por característica:")
    promedios = np.mean(caracteristicas, axis=0)
    caracteristicas_nombres = ['Longitud', 'Palabras', 'Párrafos', 'Enlaces']
    
    for nombre, promedio in zip(caracteristicas_nombres, promedios):
        print(f"      {nombre}: {promedio:.1f}")

def casos_uso_comunes():
    """Casos de uso más comunes de numpy"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Crear arrays:")
    print("   np.array([1, 2, 3])")
    print("   np.zeros((3, 4))")
    print("   np.arange(0, 10, 2)")
    
    print("\n2. Operaciones básicas:")
    print("   a + b  # Suma elemento a elemento")
    print("   a * 3  # Multiplicación por escalar")
    print("   np.sum(a)  # Suma total")
    
    print("\n3. Estadísticas:")
    print("   np.mean(array)")
    print("   np.std(array)")
    print("   np.min(array), np.max(array)")
    
    print("\n4. Indexing:")
    print("   array[0]  # Primer elemento")
    print("   array[array > 5]  # Filtrado booleano")
    print("   array[:, 1]  # Segunda columna")
    
    print("\n5. Reshape:")
    print("   array.reshape(3, 4)")
    print("   array.T  # Transponer")
    print("   array.flatten()  # Aplanar")
    
    print("\n6. Álgebra lineal:")
    print("   np.dot(a, b)  # Producto punto")
    print("   np.linalg.inv(matrix)  # Inversa")
    print("   np.linalg.eig(matrix)  # Eigenvalues")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_numpy_basico()
    ejemplo_numpy_operaciones()
    ejemplo_numpy_indexing()
    ejemplo_numpy_reshape()
    ejemplo_numpy_broadcasting()
    ejemplo_numpy_algebra_lineal()
    ejemplo_numpy_arrays_aleatorios()
    casos_uso_comunes()
    integracion_con_notesassistant()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO numpy")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Arrays multidimensionales eficientes")
    print("   • Operaciones matemáticas vectorizadas")
    print("   • Álgebra lineal básica")
    print("   • Estadísticas y análisis numérico")
    print("   • Base para pandas, matplotlib, scikit-learn")
    print("   • Broadcasting automático")
    print("\n📚 Documentación oficial:")
    print("   https://numpy.org/doc/")
    print("\n💡 Consejo: NumPy es la BASE de todo data science")
    print("   Sin NumPy no hay pandas, matplotlib, ni scikit-learn.") 