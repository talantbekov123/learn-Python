hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
	hrs = float(hrs)
	rate = float(rate)
except:
	print("Wrong input")
	quit();

result = rate * hrs;
if hrs > 40:
	result += (hrs - 40) * rate * 1.5
print(result)