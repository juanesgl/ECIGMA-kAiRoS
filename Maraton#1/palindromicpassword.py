from sys import stdin 


def close_pali(num_str): 

    num = int(num_str) 
    prefix = int(num_str[:3])

    candi = []
    for p in (prefix - 1, prefix, prefix + 1): 

        if 100 <= p <= 999: 
            p_str = str(p) 
            pal_str = p_str + p_str[::-1]
            candi.append(int(pal_str))

    best_candi = min(candi, key=lambda x: (abs(x - num), x))

    return str(best_candi)

def main(stdin): 

    cases = stdin.read().split() 

    if not cases: 
        return  

    N = int(cases[0]) 
    numbers = cases[1:N+1]

    for num_str in numbers: 
        print(close_pali(num_str))

main(stdin)