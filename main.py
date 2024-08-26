import matplotlib.pyplot as plt
import numpy as np
import time

MAX_TAMANO = 300

def medir_tiempo(funcion, *args):
    inicio = time.time()
    funcion(*args)
    fin = time.time()
    return fin - inicio

def generar_lista(tamano):
    return np.random.randint(0, 1000, tamano).tolist()

# Ejemplos
def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i
        while j > 0 and lista[j - 1] > actual:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = actual

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + centro + quicksort(derecha)

def personalizada(lista):
    pass

# Main
tamano = []
tiempo_registro = []

fns = {
    '1': {
        'fn': burbuja,
        'nombre': 'Burbuja'
    },
    '2': {
        'fn': seleccion,
        'nombre': 'Selección'
    },
    '3': {
        'fn': insercion,
        'nombre': 'Inserción'
    },
    '4': {
        'fn': quicksort,
        'nombre': 'Quicksort'
    },
    '5': {
        'fn': personalizada,
        'nombre': 'Personalizado'
    }
}

opcion = input('Seleccione el algoritmo a evaluar:\n1. Burbuja\n2. Selección\n3. Inserción\n4. Quicksort\n5. Personalizado\n')
fn = fns[opcion]['fn']

for i in range(1, MAX_TAMANO + 1):
    tamano.append(i)
    lista = generar_lista(i)
    tiempo = medir_tiempo(fn, lista)
    tiempo_registro.append(tiempo)


# Aproximaciones de referencia
max_tiempo = max(tiempo_registro)
n = np.arange(1, MAX_TAMANO + 1)
log_n = np.log(n) * (max_tiempo / np.log(MAX_TAMANO))
n_log_n = n * log_n / MAX_TAMANO
n2 = (n ** 2) * (max_tiempo / (MAX_TAMANO ** 2))
n3 = (n ** 3) * (max_tiempo / (MAX_TAMANO ** 3))
_2pow_n = 2 ** n * (max_tiempo / 2 ** MAX_TAMANO)
lineal = n * (max_tiempo / MAX_TAMANO)

# Establecer a cual se aproxima más
aproximaciones = {
    'O(n)': sum(abs(tiempo_registro - lineal)),
    'O(log(n))': sum(abs(tiempo_registro - log_n)),
    'O(n log(n))': sum(abs(tiempo_registro - n_log_n)),
    'O(n^2)': sum(abs(tiempo_registro - n2)),
    'O(n^3)': sum(abs(tiempo_registro - n3)),
    'O(2^n)': sum(abs(tiempo_registro - _2pow_n)),
}
mejor_aproximacion = min(aproximaciones, key=aproximaciones.get)
print(f'La mejor aproximación es {mejor_aproximacion}')

# Gráfica
plt.plot(tiempo_registro, tamano, label=fns[opcion]['nombre'])
plt.plot(lineal, n, label='O(n)')
plt.plot(log_n, n, label='O(log(n))')
plt.plot(n_log_n, n, label='O(n log(n))')
plt.plot(n2, n, label='O(n^2)')
plt.plot(n3, n, label='O(n^3)')
plt.plot(_2pow_n, n, label='O(2^n)')
# plt.xscale('log')
plt.ylabel('Tamaño de la entrada')
plt.xlabel('Tiempo (s)')
plt.legend()

plt.show()
