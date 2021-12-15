# lists used to make a matrix of numbers

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[3][0])


for row in number_grid:
    for colo in row:
        print(colo)