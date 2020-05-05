inputNumber=input("Enter your number:")
try:
	inputNumber=int(inputNumber)
	x1=0
	x2=1
	if inputNumber>=1:
		if inputNumber==1:
			print(x1)
		elif inputNumber==2:
			print(x2)
		else:
			for x in range(inputNumber-2):
				x1,x2=x2,x1+x2
			print(x2)
	else:
		print("Invalid input")
except ValueError:
	print("Invalid input")