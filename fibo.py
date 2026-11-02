import sys

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(sys.argv[1])
ret = fibo(n)
print(f"{ret}")

# 枝分かれが指数関数的に増えていて最終的には1か0しか返さないけど、その枝の数分足し算になる
# --------------------------------------------------------------------------
# fibo(5)
# =  fibo(4)  + fibo(3)
# = (fibo(3)  + fibo(2)) + (fibo(2) + fibo(1))
# = ((fibo(2) + fibo(1)) + (fibo(1) + fibo(0))) + ((fibo(1) + fibo(0)) + 1)
# = ((fibo(1) + fibo(0)) + (1)) + ((1 + 0) + 0) + ((1 + 0) + 1)
# = ((1 + 0) + (1)) + ((1 + 0) + 0) + ((1 + 0) + 1)
# = 5



