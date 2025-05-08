print("Functions...")


def hii():
    print("Hello")


hii()


def hi(name):
    print(f"hiii,{name}")


hi("Shahid")


def add(a, b):
    print(a + b)
    return a + b


sum = add(10, 40)
print(add(4, 6))
print(sum)
add(66, 66)


# Default argument


def defa(name="Shahid"):
    print(f"Hello {name}")


defa()  # prints with default value

defa("Showkat")


print("Keyword arguments...")


def keyar(name, rollno):
    print(f"{name} has Roll no.: {rollno}")


keyar(name="Shahid", rollno=22511)


print("Recursion....")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))


