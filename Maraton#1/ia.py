from sys import stdin 


def find_minimal_pair(num_str): 

    X = int(num_str)
    
    if X == 1:
        return "0 0"

    def nCr(n, k):
        if k > n: 
            return 0
        if k > n - k:
            k = n - k
        res = 1
        for i in range(k):
            res = res * (n - i) // (i + 1)
        return res

    best_n = X
    best_k = 1

    for k in range(175, 1, -1):
        low = 2 * k
        high = best_n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            current_val = nCr(mid, k)
            
            if current_val == X:
                best_n = mid
                best_k = k
                break
            elif current_val < X:
                low = mid + 1
            else:
                high = mid - 1

    return f"{best_n} {best_k}"


def main(stdin): 

    cases = stdin.read().split() 

    if not cases: 
        return  

    numbers = cases

    for num_str in numbers: 
        print(find_minimal_pair(num_str))

main(stdin)