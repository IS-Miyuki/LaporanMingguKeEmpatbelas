def jumlah(n:str):
    if len(n) == 0:
        return 0
    else:
        return jumlah(n[:-1]) + int(n[-1]) 

print(jumlah("54321"))