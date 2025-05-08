a = int(input("Enter any number :"))
if a > 10:
    print("Input is greater than 10")
elif a < 10:
    print("Your number is less than 10")
else:
    print("Invalid input!")


b = int(input("Enter your age: "))
veiw = "Adult" if b >= 18 else "Minor"
print(veiw)

c = int(input("Enter your score: "))
print("Pass" if c > 77 else "Fail")
