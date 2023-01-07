
while True:
    number = int(input())
    if number == 0:
        break
    number_str = str(number)
    if len(number_str) == 1:
        print('yes')
    else:
        if len(number_str) % 2 == 0:
            left = number_str[0:len(number_str)//2]
            right = number_str[len(number_str)//2:][::-1]
            if left == right:
                print('yes')
            else:
                print('no')
        else:
            left = number_str[0:len(number_str) // 2]
            right = number_str[len(number_str) // 2+1:][::-1]
            if left == right:
                print('yes')
            else:
                print('no')