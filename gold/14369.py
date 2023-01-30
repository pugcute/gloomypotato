
N = int(input())

for tc in range(1, N+1):
    alpa_dict = {}
    words = list(input())
    for i in range(ord('A'), ord('Z')+1):
        alpa_dict[chr(i)] = 0
    for word in words:
        alpa_dict[word] += 1
    answer = []
    if alpa_dict['Z']:
        tmp = alpa_dict['Z']
        alpa_dict['Z'] -= tmp
        alpa_dict['E'] -= tmp
        alpa_dict['R'] -= tmp
        alpa_dict['O'] -= tmp
        for _ in range(tmp):
            answer.append('0')
    if alpa_dict['X']:
        tmp = alpa_dict['X']
        alpa_dict['S'] -= tmp
        alpa_dict['I'] -= tmp
        alpa_dict['X'] -= tmp
        for _ in range(tmp):
            answer.append('6')
    if alpa_dict['G']:
        tmp = alpa_dict['G']
        alpa_dict['E'] -= tmp
        alpa_dict['I'] -= tmp
        alpa_dict['G'] -= tmp
        alpa_dict['H'] -= tmp
        alpa_dict['T'] -= tmp
        for _ in range(tmp):
            answer.append('8')
    if alpa_dict['S']:
        tmp = alpa_dict['S']
        alpa_dict['S'] -= tmp
        alpa_dict['E'] -= tmp
        alpa_dict['V'] -= tmp
        alpa_dict['E'] -= tmp
        alpa_dict['N'] -= tmp
        for _ in range(tmp):
            answer.append('7')
    if alpa_dict['V']:
        tmp = alpa_dict['V']
        alpa_dict['F'] -= tmp
        alpa_dict['I'] -= tmp
        alpa_dict['V'] -= tmp
        alpa_dict['E'] -= tmp
        for _ in range(tmp):
            answer.append('5')
    if alpa_dict['F']:
        tmp = alpa_dict['F']
        alpa_dict['F'] -= tmp
        alpa_dict['O'] -= tmp
        alpa_dict['U'] -= tmp
        alpa_dict['R'] -= tmp
        for _ in range(tmp):
            answer.append('4')
    if alpa_dict['I']:
        tmp = alpa_dict['I']
        alpa_dict['N'] -= tmp
        alpa_dict['I'] -= tmp
        alpa_dict['N'] -= tmp
        alpa_dict['E'] -= tmp
        for _ in range(tmp):
            answer.append('9')
    if alpa_dict['W']:
        tmp = alpa_dict['W']
        alpa_dict['T'] -= tmp
        alpa_dict['W'] -= tmp
        alpa_dict['O'] -= tmp
        for _ in range(tmp):
            answer.append('2')
    if alpa_dict['R']:
        tmp = alpa_dict['R']
        alpa_dict['T'] -= tmp
        alpa_dict['H'] -= tmp
        alpa_dict['R'] -= tmp
        alpa_dict['E'] -= tmp
        alpa_dict['E'] -= tmp
        for _ in range(tmp):
            answer.append('3')
    if alpa_dict['O']:
        tmp = alpa_dict['O']
        alpa_dict['O'] -= tmp
        alpa_dict['N'] -= tmp
        alpa_dict['E'] -= tmp
        for _ in range(tmp):
            answer.append('1')
    answer.sort()
    answer_word = ''.join(answer)
    print(f'Case #{tc}: {answer_word}')
