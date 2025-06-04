def prime(n, i = 2):
    if n == 0 or i == n:
        return True
    elif (n % i)  == 0:
        return False
    else:
        return prime(n,i+1) 

print(prime(6))