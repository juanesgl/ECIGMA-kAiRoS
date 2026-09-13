from sys import stdin as sd

def main(sd):
    
    matrix = []
    queensPos = []
    
    for _ in range(8):
        matrix.append(list(sd.readline().strip()))
    
    
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == '*':
                queensPos.append((col, row));          
    
    if len(queensPos) != 8:
        print('invalid')
        return 'invalid'
    
    for i in range(len(queensPos)):
        for j in range(i + 1, len(queensPos)):
            x1, y1 = queensPos[i]
            x2, y2 = queensPos[j]
            
            if x1 == x2 or y1 == y2:
                print('invalid')
                return 'invalid'
                
            if abs(x2 - x1) == abs(y2 - y1):
                print('invalid')
                return 'invalid'
        
    print('valid')
    return 'valid'

main(sd)