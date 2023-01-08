
photo_num = int(input())
order_num = int(input())
dict_photo = {}

orders = list(map(int, input().split()))
cnt = 0

for order in orders:
    if len(dict_photo.keys()) >= photo_num and order not in dict_photo.keys():
        keys = list(dict_photo.keys())
        values = list(dict_photo.values())
        min_val = values.index(min(values))
        del dict_photo[keys[min_val]]

    if order not in dict_photo.keys():
        dict_photo[order] = 1
    else:
        dict_photo[order] += 1


for ans in sorted(dict_photo.keys()):
    print(ans, end=' ')