

# while len(stack):
#     current_idx = len(stack) - 1
#     current_val = stack.pop()
#     top = len(stack) - 1
#     while top >= -1:
#         if top == -1:
#             dict_stack[current_idx] = top+1
#             break
#         if stack[top] > current_val:
#             dict_stack[current_idx] = top + 1
#             break
#         else:
#             top -= 1
#
# for i in range(N):
#     print(dict_stack[i], end=' ')
