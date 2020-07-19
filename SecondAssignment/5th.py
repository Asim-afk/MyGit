def Max(a,b,c):
    M= max(a,b,c)
    return M

ans= Max(1,5,3)
print(ans)


#or


def Max2(a,b,c):
    if a>b>c or a>c>b:
        return a
    elif b>a>c or b>c>a:
        return b
    else:
        return c

ans= Max2(1,5,3)
print(ans)
        
