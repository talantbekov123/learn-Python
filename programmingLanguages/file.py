import os

os.chdir('/home/kairat/Desktop/learnPython/programmingLanguages')

fin = open('text.txt', 'rt');
fout = open('result.txt', 'wt');

data = ''
for i in range(5):
	s = fin.readline().split()
	for elem in s:
		if(len(elem) >= 3):
			data += elem[:3] + ' '
		else:
			data += elem + ' '
	data += '\n'

fout.write(data);
fout.close();
fin.close();
