# Integrantes

- David Martinez
- Franco Comas
- Antony Barahona

# Implementación del Algoritmo CYK en Python

Este proyecto implementa el algoritmo CYK (Cocke-Younger-Kasami) en Python para verificar si una cadena puede ser generada por una gramática libre de contexto en forma normal de Chomsky (CNF). Además, se mide la complejidad del algoritmo y se demuestra empíricamente que su complejidad es \(O(n^3)\).

## Descripción del Algoritmo CYK

El algoritmo CYK es un enfoque de programación dinámica para determinar si una cadena pertenece a un lenguaje generado por una gramática libre de contexto en CNF. Utiliza una tabla \(n 	imes n\) para dividir la cadena en subcadenas y verificar qué no terminales pueden derivar dichas subcadenas.

### Funcionamiento:

1. **Entrada**: 
   - Una gramática libre de contexto en CNF.
   - Una cadena de entrada.

2. **Proceso**:
   - Se construye una tabla para almacenar los no terminales que generan cada subcadena de la cadena de entrada.
   - Se analiza la cadena de manera creciente, comenzando con subcadenas de longitud 1 hasta la longitud completa de la cadena.
   - Para cada subcadena, se verifican las combinaciones de reglas de la gramática para determinar si el símbolo inicial de la gramática puede derivar la cadena completa.

3. **Salida**: 
   - `True` si la cadena puede ser derivada por la gramática.
   - `False` en caso contrario.

## Requisitos

1. Tener Kali Linux instalado (o cualquier sistema basado en Linux con Python 3).
2. Python 3.
3. El archivo `cyk.py` debe estar presente en el directorio del proyecto.

## Instrucciones para la ejecución

### Paso 1: Abrir la terminal

- Navega al directorio donde se encuentra el archivo `cyk.py`.
- Si estás usando Kali, abre una terminal.

### Paso 2: Verificar que tienes Python 3 instalado

Ejecuta el siguiente comando en la terminal para verificar que tienes Python 3 instalado:

```bash
python3 --version
```

Si no tienes Python 3, puedes instalarlo usando:

```bash
sudo apt-get install python3
```

### Paso 3: Ejecutar el script

Para ejecutar el script `cyk.py`, utiliza el siguiente comando:

```bash
python3 cyk.py
```

### Paso 4: Instalación de dependencias adicionales (opcional)

Si deseas visualizar los tiempos de ejecución de manera gráfica, debes instalar la librería `matplotlib`. Para instalarla, usa el siguiente comando:

```bash
pip install matplotlib
```

### Paso 5: Ejecutar con visualización de gráficos (opcional)

Si instalaste `matplotlib`, puedes ejecutar el script y generar un gráfico del tiempo de ejecución del algoritmo en función de la longitud de la cadena. Para ello, ejecuta:

```bash
python3 cyk.py
```

A continuación, se abrirá una ventana con el gráfico mostrando el crecimiento cúbico del algoritmo.

## Explicación de los resultados

- **Resultado `True`**: Significa que la cadena de entrada es generada por la gramática.
- **Resultado `False`**: La cadena no puede ser generada por la gramática.
- **Tiempos de ejecución**: A medida que aumentas la longitud de la cadena, notarás un aumento significativo en el tiempo de ejecución, lo cual es consistente con la complejidad \(O(n^3)\) del algoritmo.

### Ejemplo de ejecución en la terminal

```bash
┌──(usuario㉿Kali)-[~/mi_proyecto_cyk]
└─$ python3 cyk.py
Longitud: 5, Tiempo de ejecución: 0.000061 segundos
Longitud: 10, Tiempo de ejecución: 0.000299 segundos
Longitud: 15, Tiempo de ejecución: 0.000746 segundos
Longitud: 20, Tiempo de ejecución: 0.001934 segundos
Longitud: 25, Tiempo de ejecución: 0.003455 segundos
Longitud: 30, Tiempo de ejecución: 0.006086 segundos
```
