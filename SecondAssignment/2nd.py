def fizz_buzz(x):
    if x%3==0:
        return "Fizz"
    elif x%5==0:
        return "Buzz"
    else:
        return x

Ans= fizz_buzz(int(input("input the num: ")))

print(Ans)
