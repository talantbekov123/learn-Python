fname = input("Enter file name: ")
fh = open(fname)
data = fh.read()
data = data.split()
data.sort()
res = list()
for word in data:
	if word not in res:
		res.append(word)
print(res)