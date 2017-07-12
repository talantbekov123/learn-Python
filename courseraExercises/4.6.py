hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
	hrs = float(hrs)
	rate = float(rate)
except:
	print("Wrong input")
	quit()

def computepay(hrs,rate):
	result = rate * hrs;
	if hrs > 40:
		result += (hrs - 40) * rate * 1.5
		result -= (hrs - 40) * rate
	return result

print(computepay(hrs,rate))