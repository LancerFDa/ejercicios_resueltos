def esMatrizCuadrada(matriz):

    for fila in matriz:
        if len(fila) != len(matriz):
            return False
    return True

esMatrizCuadrada([[1,2,3],
                     [1,2,3],
                     [1,2,3]])