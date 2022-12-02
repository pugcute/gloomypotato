
hour, minute = map(int, input().split())

if hour == 0:
    if minute >= 45:
        print(hour, minute-45)
    else:
        print(23, 60 - (45 - minute))
else:
    if minute >= 45:
        print(hour, minute - 45)
    else:
        print(hour-1, 60 - (45 - minute))