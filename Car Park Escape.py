'''
CODE ISNT CORRECT



Your task is to escape from the carpark using only the staircases provided 
to reach the exit. You may not jump over the edge of the levels (you’re not Superman!) 
and the exit is always on the far right of the ground floor.

1. You are passed the carpark data as an argument into the function.
2. Free carparking spaces are represented by a 0
3. Staircases are represented by a 1
4. Your parking place (start position) is represented by a 2
5. The exit is always the far right element of the ground floor.
6. You must use the staircases to go down a level.
7. You will never start on a staircase.
8. The start level may be any level of the car park.

Return an array of the quickest route out of the carpark
R1 = Move Right one parking space.
L1 = Move Left one parking space.
D1 = Move Down one level.
'''


def escape(carpark):
    stairs = 1
    start = 2
    result = []
    for level in carpark:
        if start in level:
            print(level.index(start) - level.index(stairs))
            spaces = level.index(start) - level.index(stairs)
            if spaces < 0:
                result.append('R' + str(abs(spaces)))
            else:
                result.append('L' + str(abs(spaces)))
            print(result)
            top_spot = level.index(stairs)
        
        elif stairs in level:
            down = 1
            if level.index(stairs) == top_spot:
                down += 1
                result.append('D' + str(down))
                top_spot = level.index(stairs)
            if top_spot != level.index(stairs):
                result.append('D' + str(1))
                spaces = top_spot - level.index(stairs)
                if spaces < 0:
                    result.append('R' + str(abs(spaces)))
                else:
                    result.append('L' + str(abs(spaces)))
                top_spot = level.index(stairs)
                
        else:
            if not result[-1].startswith('D'):
                result.append('D1')
            spaces = top_spot - (len(level)-1)
            if spaces == 0:
                return None
            result.append('R' + str(abs(spaces)))
        
    return result   
    
    
print(escape([[2, 0, 0, 1, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]))

print(escape([[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]))
                
            
print(escape([[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]))            
        
print(escape([[0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]))
