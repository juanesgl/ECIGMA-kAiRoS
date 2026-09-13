from sys import stdin as sd 

def main():

    K = sd.readline()  # Number of cases
    coordinates = []
    
    for _ in range(int(K)):
        N = sd.readline()  # Number of buidings
        for _ in range(int(N)):
            coordinates.append(list(map(int, sd.readline().split(" "))))

        print(coordinates)
    

main()
