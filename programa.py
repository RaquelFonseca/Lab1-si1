def encontra_maximo(array):
    maximo = array[0]
    for i in array:
        if maximo < i:
            maximo = i

    return maximo


assert encontra_maximo([27, 5, 2017]) == 2017
