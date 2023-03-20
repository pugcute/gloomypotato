N = int(input())

mod =10007

if N < 5:
    print(N)
elif N % 3 == 0:
    print(pow(3, N//3, mod))
elif N % 3 == 1:
    print((pow(3, (N-4)//3, mod) * 4) % mod)
else:
    print((pow(3, (N-2)//3, mod) * 2) % mod)