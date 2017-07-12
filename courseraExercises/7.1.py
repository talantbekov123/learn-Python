fileName = input("Enter a file name:")
handle = open(fileName)
text = handle.read()
print(text.upper().strip());
