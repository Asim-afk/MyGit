def speedcheck(speed):
    if speed <=70:
        return"OK"
    else:
        demerit= (speed - 70)/5
        if demerit <= 12:
            return "demerit points: " + str(demerit)
        else:
            return "license suspended"
speedLog= int(input("speed: "))
print(speedcheck(speedLog))

                
