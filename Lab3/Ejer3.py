def division(p1, p2, k, epsilon, lista):
    if p2-p1 < epsilon:
        y1 = p1**3 - 6 * p1**2 + 4*p1 + 12
        y2 = p2**3 - 6 * p2**2 + 4*p2 + 12

        if y1 <= k <= y2 or y2 <= k <= y1:
            lista.append([p1, p2])
    else:
        puntoMedio = (p2-p1)/2
        tp = division(p1, (p1+puntoMedio), k, epsilon, lista)
        tp2 = division((p2-puntoMedio), p2, k, epsilon, lista)

def main(p1,p2,k,epsilon):
    conjuntoX = []
    (division(p1, 2, k, epsilon, conjuntoX))
    (division(2, p2, k, epsilon, conjuntoX))
    return conjuntoX


print(main(2,5,-1,0.15))