# 🔹 Common Modes:

# Mode	Description
# 'r'	Read (default) – error if file doesn’t exist
# 'w'	Write – creates file or overwrites
# 'a'	Append – creates file or adds to end
# 'x'	Create – error if file exists
# 'b'	Binary mode (e.g., 'rb', 'wb')
# 't'	Text mode (default)



print("Reading a file...")
file = open("text.txt","rb")
content = file.read()
print(content)
file.close()


print("Writing a file...")

file=open("text2.txt","w")
file.write("Hii, line injected by poython script..\n")
file.write("Hello, line 2 injected by poython script..\n")
file.close()