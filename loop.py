
def loop(n):
    if n <= 0:
        print(f"{0} ", end="")
        return n
    loop(n-1)
    print(f"{n} ", end="")

loop(10)
print()
