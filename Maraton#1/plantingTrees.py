from sys import stdin 

def main(stdin):


    lines = stdin.readlines()

    lista = list(map(int, lines[1].split()))  

    lista.sort(reverse = True) 

    countDays = 0 
    dia_Plantado = 1 

    for num in lista: 
        actual_pos = dia_Plantado + num 

        if actual_pos > countDays: 
            countDays = actual_pos 

        dia_Plantado += 1 

    print(countDays + 1 )


main(stdin)

