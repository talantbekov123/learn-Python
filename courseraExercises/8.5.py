fname = input("Enter file name: ")
fh = open(fname)

count = 0
for elem in fh:
    if elem.find('From') == 0 and len(elem) > 40:
        axilary = elem.split()
        count = count + 1
        print(axilary[1])
            
print("There were", count, "lines in the file with From as the first word")
