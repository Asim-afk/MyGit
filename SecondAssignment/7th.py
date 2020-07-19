def mult(*a):
    mult = 1
    for i in a:
        mult  = mult*i
    return mult
ans= mult(8,2,3,-1,7)
print(ans)
