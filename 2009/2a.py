grid = [list(input("")),list(input("")),list(input("")),list(input(""))]
originalGrid = grid
removedGrid = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
rounds = int(input(""))

for i in range(rounds):
    red = 0
    green = 0
    blue = 0
    for y in range(4):
        for x in range(3):
            if grid[y][x] == grid[y][x+1]:
                removedGrid[y][x] = grid[y][x]
                removedGrid[y][x+1] = grid[y][x+1]
    for x in range(4):
        for y in range(3):
            if grid[y][x] == grid[y+1][x]:
                removedGrid[y][x] = grid[y][x]
                removedGrid[y+1][x] = grid[y+1][x]
    
    for y in range(4):
        red += removedGrid[y].count("R")
        green += removedGrid[y].count("G")
        blue += removedGrid[y].count("B")

    for y in range(3):
        for x in range(4):
            if grid[y+1][x] == removedGrid[y+1][x] and removedGrid[y][x] == False:
                grid[y+1][x] = grid[4-y][x]
                grid[y][x] = ""
    print(grid)

print(removedGrid)

# RRGB
# GGGR
# RBRB
# BBGR

#    B
#    R
# R RB
#   GR