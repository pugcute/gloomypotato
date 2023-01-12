
matrix = [[0] * 8 for _ in range(8)]


king, rock, N = map(str, input().split())


king_row = 8-int(king[1])
king_col = ord(king[0])
rock_row = 8-int(rock[1])
rock_col = ord(rock[0])

for _ in range(int(N)):
    command = input()
    if command == 'R':
        next_king_row = king_row
        next_king_col = king_col + 1
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row
            next_rock_col = next_king_col + 1
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'L':
        next_king_row = king_row
        next_king_col = king_col - 1
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row
            next_rock_col = next_king_col - 1
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'T':
        next_king_row = king_row - 1
        next_king_col = king_col
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row - 1
            next_rock_col = next_king_col
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'B':
        next_king_row = king_row + 1
        next_king_col = king_col
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row + 1
            next_rock_col = next_king_col
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'RT':
        next_king_row = king_row - 1
        next_king_col = king_col + 1
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row - 1
            next_rock_col = next_king_col + 1
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'LT':
        next_king_row = king_row - 1
        next_king_col = king_col - 1
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row - 1
            next_rock_col = next_king_col - 1
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'RB':
        next_king_row = king_row + 1
        next_king_col = king_col + 1
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row + 1
            next_rock_col = next_king_col + 1
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

    if command == 'LB':
        next_king_row = king_row + 1
        next_king_col = king_col - 1
        if next_king_row < 0 or next_king_row >= 8 or next_king_col < 65 or next_king_col >= 73:
            continue
        if rock_row == next_king_row and rock_col == next_king_col:
            next_rock_row = next_king_row + 1
            next_rock_col = next_king_col - 1
            if next_rock_row < 0 or next_rock_row >= 8 or next_rock_col < 65 or next_rock_col >= 73:
                continue
            else:
                king_row = next_king_row
                king_col = next_king_col
                rock_row = next_rock_row
                rock_col = next_rock_col
        else:
            king_row = next_king_row
            king_col = next_king_col

print(chr(king_col) + str(8-king_row))
print(chr(rock_col) + str(8-rock_row))


