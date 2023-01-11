
def poly_add(A_start, A_end, B_start, B_end):
    while A_start <= A_end and B_start <= B_end:
        if terms[A_start][1] > terms[B_start][1]:
            terms.append([terms[A_start][0], terms[A_start][1]])
            A_start = A_start + 1
        elif terms[A_start][1] == terms[B_start][1]:
            tmp = terms[A_start][0] + terms[B_start][0]
            if tmp != 0:
                terms.append([tmp, terms[A_start][1]])
            A_start = A_start + 1
            B_start = B_start + 1
        else:
            terms.append([terms[B_start][0], terms[B_start][1]])
            B_start = B_start + 1
    print(A_start)
    if A_start <= A_end:
        while A_start <= A_end:
            terms.append([terms[A_start][0], terms[A_start][1]])
            A_start = A_start + 1
    if B_start <= B_end:
        terms.append([terms[B_start][0], terms[B_start][1]])
        B_start = B_start + 1


terms = [[10, 4], [8, 3], [7, 1], [1, 0], [10, 3], [3, 2]]
avail = 6

ast = 0
af = 3
bs = 4
bf = 5
poly_add(ast, af, bs, bf)
print(terms[avail:])
