memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

for i in range(0, 20):
    n = fibo(i)
    print(f"{n} ", end="")

print()
