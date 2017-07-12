fileName = input("Enter a file name:")
handle = open(fileName)

sum = 0
c = 0

for elem in handle:
	index = elem.find('X-DSPAM-Confidence:')
	if(index != -1):
		num = elem[index + len('X-DSPAM-Confidence:'):]
		num = float(num.strip())
		sum += num
		c = c + 1

print('Average spam confidence:',sum / c)