def esMatrizCuadrada(matriz):

    for fila in matriz:
        if len(fila) != len(matriz):
            return False
    return True

def esAntisimetrica(matriz):

    diagonal = 0
    
    for fila in matriz:
        for columna in fila:
            if (fila[diagonal] and columna) != 0:
                return False
        diagonal += 1
    return True


            
if __name__ == '__main__':
    # Test Cases:

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, 3],
                             [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]) is True

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, -2],
                             [2, 2, 3]]) is False

    assert esAntisimetrica([ [1, 2, 5],
                             [0, 1, -9],
                             [0, 0, 1]]) is False
    
    assert esAntisimetrica([ [1, 2,  5],
                             [-2, 1, -9],
                             [-5, 0, 1]]) is False