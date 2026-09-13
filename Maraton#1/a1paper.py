from sys import stdin 

def main(stdin):

    lines = stdin.readlines()

    o = int(lines[0])

    lista = list(map(int, lines[1].split()))  

    falta = [0] * (o - 1)
    num_minimo = 0 

    for i in range(len(lista)): 
        if i == 0:
            if lista[i] == 2:
                num_minimo = 2
                break
            else:
                falta[i] = 2 - lista[i]
        elif ((lista[i] // 2) >= falta[i-1]):
            num_minimo = i + 2
            falta[i] = falta[i - 1] * 2
            break
        else:
            falta[i] = falta[i - 1] * 2

    if num_minimo == 0:
        print("impossible")
        return

    suma = (2 ** (1/4)) / 2
    

    for i in range(1, num_minimo - 1):
        suma += ( (2 ** (1/4)) / (2 ** ((i + 2)/ 2)) ) * (falta[i] // 2)

    print(f"{suma:.11f}")

main(stdin)