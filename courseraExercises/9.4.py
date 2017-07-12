name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

values = dict()

for elem in handle :
	if elem.find('From') != -1 and len(elem) < 40:
		index = elem.find(':')
		email = elem[index + 2:].strip()
		values[email] = values.get(email, 1) + 1

element = ''
c = 0
for elem in values :
	if values[elem] > c :
		c = values[elem]
		element = elem

print(element.split()[0], values[element] - 1)