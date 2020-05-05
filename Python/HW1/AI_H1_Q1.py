inputNumber=input("Enter your number:")
try:
	inputNumber=int(inputNumber)
	if inputNumber in range(1,9):
		if inputNumber % 2 == 0:
			print("Even")
		else:
			print("Odd")
	else:
		print("not valid input")
except ValueError:
	print("not valid input")