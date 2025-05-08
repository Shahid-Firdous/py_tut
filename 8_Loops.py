# Intendatioin must be considered from now onwards...



a = {1, 2, 3, 4, 5, 6576, 7}


for ab in a:
    print(ab)


for name in "Shahid":
    print(name)


for i in range(10):
    print(i)


for j in range(0, 20, 2):  # start,stop,step
    print(j)


c = 0
while c < 10:
    print(c)
    c += 1


for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)


for i in range(5):
    print(i)
else:
    print("Loop completed without break.")
