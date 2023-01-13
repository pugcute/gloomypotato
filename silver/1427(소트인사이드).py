
# def select_sort():
#     for i in range(len(array)):
#         min_idx = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[min_idx]:
#                min_idx = j
#         array[i], array[min_idx] = array[min_idx], array[i]


# def insert_sort():
#     for i in range(1, len(array)):
#         for j in range(i, 0, -1):
#             if array[j] < array[j-1]:
#                 array[j], array[j-1] = array[j-1], array[j]
#             else:
#                 break

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    tail = a[1:]
    left = []
    right = []
    for num in tail:
        if pivot < num:
            right.append(num)
        else:
            left.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)

def count_sort():
    matrix = [0] * 10
    for num in array:
        matrix[num] += 1

    answer = []
    for i in range(len(matrix)):
        for j in range(matrix[i]):
            answer.append(i)
    return answer


array = [8, 7, 9, 1, 2, 3, 4, 5, 6, 0]
print(count_sort())


# numbers = input()
# matrix = [0] * 10
# for num in numbers:
#     matrix[int(num)] += 1
#
# answer = ''
# for i in range(9, -1, -1):
#     for j in range(matrix[i]):
#         answer += str(i)
# print(answer)