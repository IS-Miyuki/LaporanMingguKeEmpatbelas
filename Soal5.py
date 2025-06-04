def kombinasi(n,r):
    if r == 0:
        return 1
    else:
        return kombinasi(n-1,r-1) * n / r

print(kombinasi(5,4))