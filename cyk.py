import time
import random

def cyk_algorithm(grammar, string):
    n = len(string)
    r = len(grammar)
    
    # Crear la tabla CYK (n x n)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Inicializar la primera columna de la tabla
    for i in range(n):
        for lhs, rhs in grammar.items():
            if (string[i],) in rhs:
                table[i][i].add(lhs)

    # Rellenar la tabla CYK
    for length in range(2, n + 1):  # Longitud de la subcadena
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rhs in grammar.items():
                    for production in rhs:
                        if len(production) == 2:
                            B, C = production
                            if B in table[i][k] and C in table[k + 1][j]:
                                table[i][j].add(lhs)

    # Verificar si el símbolo inicial está en la esquina superior derecha
    return 'S' in table[0][n - 1]

def generate_string(length):
    """Genera una cadena aleatoria de 'a' y 'b' con longitud `length`."""
    return ''.join(random.choice('ab') for _ in range(length))

def measure_time_for_length(grammar, length):
    string = generate_string(length)
    start_time = time.time()
    cyk_algorithm(grammar, string)
    end_time = time.time()
    return end_time - start_time

def main():
    grammar = {
        'S': [('A', 'B'), ('B', 'C')],
        'A': [('B', 'A'), ('a',)],
        'B': [('C', 'C'), ('b',)],
        'C': [('A', 'B'), ('a',)]
    }
    
    # Prueba con diferentes longitudes de cadena
    for length in range(5, 50, 5):
        exec_time = measure_time_for_length(grammar, length)
        print(f"Longitud: {length}, Tiempo de ejecución: {exec_time:.6f} segundos")

if __name__ == "__main__":
    main()
