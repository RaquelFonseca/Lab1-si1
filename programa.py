def encontra_maximo(array):
    maximo = array[0]
    for i in array:
        if maximo < i:
            maximo = i

    return maximo


assert encontra_maximo([27, 5, 2017]) == 2017

def encontra_minimo(array):
    minimo = array[0]
    for i in array:
        if minimo > i:
            minimo = i

    return minimo


assert encontra_minimo([27, 5, 2017]) == 5
