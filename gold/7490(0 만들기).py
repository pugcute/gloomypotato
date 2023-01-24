# import sys
# sys.setrecursionlimit(10**9)
#
#
# def make0(cnt, answer_str, answer):
#     if answer == 0 and cnt == K:
#         tmp_answer.append(answer_str)
#         return
#     elif cnt == K and answer != 0:
#         return
#     else:
#         make0(cnt+1, answer_str + f'+{cnt+1}', answer + (cnt+1))
#         make0(cnt + 1, answer_str + f'-{cnt + 1}', answer - (cnt + 1))
#         if len(answer_str) > 2 and answer_str[-2] == '+':
#             tmp = int(answer_str[-1] + str(cnt+1))
#             make0(cnt + 1, answer_str + f' {cnt + 1}', answer - cnt + tmp)
#         elif len(answer_str) > 2 and answer_str[-2] == '-':
#             tmp = int(answer_str[-1] + str(cnt + 1))
#             make0(cnt + 1, answer_str + f' {cnt + 1}', answer + cnt - tmp)
#
# N = int(input())
#
# for _ in range(N):
#     K = int(input())
#     tmp_answer = []
#     make0(1, '1', 1)
#     tmp_answer.sort()
#     for ans in tmp_answer:
#         print(ans)
#     print()
#
#

a, b = int(input())
print(a+b)
