def test(n:str):
    if len(n) == 0:
        return 0
    else:
        return test(n[:-1]) + int(n[-1]) 

print(test("54321"))