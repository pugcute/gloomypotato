

check_board = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6']
prev_knight = ''
flag = 0
while len(check_board) != 0:
    knight = input()
    try:
        check_board.remove(knight)
    except:
        flag = 1
        break

if flag == 1:
    print('Invalid')
else:
    print('Valid')