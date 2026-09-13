from math import factorial as fc
from sys import stdin

def combi(N, M):
    return fc(N) // (fc(M) * fc(N - M))


def main(stdin):
    N, M = map(int, stdin.readline().split())

    restrictions = []

    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        restrictions.append((a, b))

    total = 0

    for r in range(0, N + 1):
        total += combi(N, r)

    for pizza in range(1 << N): # this is the same as 2**N 
        valid = True

        for a, b in restrictions:
            if (pizza & (1 << (a - 1))) and (pizza & (1 << (b - 1))):
                valid = False
                break

        if not valid:
            total -= 1

    print(total)

main(stdin)