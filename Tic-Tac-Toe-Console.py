grid = [[8 for x in range(3)] for x in range(3)]

turn = True # Start as O

# Game logic
while True:
    x_coord = int(input("Row: "))
    y_coord = int(input("Column: "))
    if grid[x_coord][y_coord] != 8 or 0 > x_coord > 2 or 0 > y_coord > 2:
        print("You can't park there mate.")
        continue
    if turn:
        #turn = False
        grid[x_coord][y_coord] = 0
    else:
        #turn = True
        grid[x_coord][y_coord] = 1

    # Row winning logic
    for row in grid:
        if sum(row) == 3:
            print("x wins via row")
            quit()
        elif sum(row) == 0:
            print("o wins via row")
            quit()
    
    # Column winning logic
    for i in range(3):
        column = [row[i] for row in grid]
        if sum(column) == 3:
            print("x wins via column")
            quit()
        elif sum(column) == 0:
            print("o wins via column")
            quit()
    
    # Diagonal winning logic
    neg_diag = pos_diag = 0
    for i in range(3):
        neg_diag += grid[i][i]
        pos_diag += grid[i][2-i]
    if pos_diag == 3 or neg_diag == 3:
        print("x wins via diagonal")
        quit()
    elif pos_diag == 0 or neg_diag == 0:
        print("o wins via diagonal")
        quit()
    
    # Display grid
    display = [["[ ]" for x in range(3)] for y in range(3)]
    y_v = 0
    for row in grid:
        x_v = 0
        for value in row:
            if value == 0:
                display[y_v][x_v] = "[O]"
            elif value == 1:
                display[y_v][x_v] = "[X]"
            else:
                display[y_v][x_v] = "[ ]"
            x_v += 1
        y_v += 1

    for r in display:
        print(*r)