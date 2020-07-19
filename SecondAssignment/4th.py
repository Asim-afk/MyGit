def ShowNumber(limit):
    i=0
    while i <= limit:
        if i % 2 == 0:
            print(str(i) + "EVEN")
        else:
            print(str(i) + "ODD")
        i += 1

number = int(input("Enter limit: "))
ShowNumber(number)
