#Keyboard Game
map_data = [
    "#####################",
    "#...#...............#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#..............#....#",
    "#..............#....#",
    "#####################"
]

player_row = 4
player_column = 9

quit_game = False

while not quit_game:
    print("\x1b[2J\x1b[H", end="")

    for row_index, row in enumerate(map_data):
        for col_index, map_char in enumerate(row):
            if row_index == player_row and col_index == player_column:
                print("@", end="")
            else:
                print(map_char, end="")
        print()
        
    print("What does the below commands stands for?")
    print("n: move north (up)")
    print("s: move south (down)")
    print("e: move east (right)")
    print("w: move west (left)")
    print("q: quit the game")
    command = input("Enter a move (n,s,e,w,q): ").lower()

    if command == "n":
        new_row = player_row - 1
        new_col = player_column
    elif command == "s":
        new_row = player_row + 1
        new_col = player_column
    elif command == "w":
        new_row = player_row
        new_col = player_column - 1
    elif command == "e":
        new_row = player_row
        new_col = player_column + 1
    elif command == "q":
        quit_game = True
        continue
    else:
        print(f"Unknown command: {command}")
        input("Press Enter to continue...")
        continue

    if map_data[new_row][new_col] == "#":
        print("You can't go that way.")
        input("Press Enter to continue...")
    else:
        player_row = new_row
        player_column = new_col

print("Your Game is quit. Thanks for playing!")
