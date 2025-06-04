def deret_ganjil(n, i = 1):
    if n == 0:
        return 0
    else:
        return deret_ganjil(n-1, i+2) + i

print(deret_ganjil(5))