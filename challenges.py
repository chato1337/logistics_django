'''
    Escribir un ejemplo de una lambda function de python
'''

add = lambda x, y: x + y

'''
    Un ejemplo y utilización de lookup table
'''

lookup_table = {
    'manzana': 'fruit',
    'naranja': 'fruit',
    'zanahoria': 'vegetable',
    'lechuga': 'vegetable',
    'perro': 'animal',
    'gato': 'animal'
}

def getTableValue(key: str, lookup_list) -> str:
    if key in lookup_list:
        return lookup_table[key]
    else:
        return 'not-found'

'''
    Retornar un n-valor de la secuencia fibonacci con recursividad
'''

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


'''
    Un ejemplo de un quick sort
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)




def __main__():
    resultado = add(5, 3)
    print('lambda fn result: ', resultado)

    value = getTableValue('lechuga', lookup_table)
    print('lookup result: ', value)


    fibo = fibonacci(10)
    print('fibonaxi max result', fibo)

    array = [9, 5, 2, 8, 1, 10]
    sorted_array = quick_sort(array)

    print('quicksort', sorted_array)

if __name__ == "__main__":
    __main__()