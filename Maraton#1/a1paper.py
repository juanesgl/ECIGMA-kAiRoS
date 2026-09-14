from sys import stdin 

def main(stdin):

    lines = stdin.readlines()

    if not lines: 
        return 
    
    o = int(lines[0])

    lista = list(map(int, lines[1].split()))  

    falta = [0] * (o - 1)
    num_minimo = 0 

    for i in range(len(lista)): 
        if i == 0:
           necesarias = 2 
        else: 
            necesarias = falta[i - 1] * 2 

        if lista[i] >= necesarias: 
            num_minimo = i + 2 
            falta[i] = 0 
            break
        else: 
            falta[i] = necesarias - lista[i]

    if num_minimo == 0:
        print("impossible")
        return 

    suma = 0.0 

    for i in range(num_minimo - 1): 
        k = i + 2 
        lc = 2 ** (-(2 * k -1) / 4 )

        hu = 2 if i == 0 else falta[i - 1] * 2 
        unir = hu // 2 

        suma += lc * unir 

    print(f"{suma:.11f}")

main(stdin)