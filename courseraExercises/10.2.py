name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

values = dict()

for elem in handle :
	if elem.find('From') != -1 and len(elem) > 40:
		axilary = elem.split()
		hour = axilary[5][:2]
		values[hour] = values.get(hour, 0) + 1

result = list()
for elem in values.items() :
	result.append(elem)

result.sort()

for k,v in result:
	print(k,v)