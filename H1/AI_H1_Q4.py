import random
randomNumber=str(random.randint(1000,9999))
tryNumber=input("Enter your guess number: ")
while randomNumber!=tryNumber:
	counter1=0
	counter2=0
	for n in range(4):
		if tryNumber[n]==randomNumber[n]:
			counter2 += 1
		elif tryNumber[n] in randomNumber:
			counter1 += 1
	print(str(counter1)+'+,'+str(counter2)+'++')
	tryNumber=input("Enter your guess number: ")
print('Congratulations! Your guess is correct! The number was: '+str(randomNumber))

# while randomNumber!=tryNumber:
# 	counter1=0
# 	counter2=0
# 	temp=randomNumber
# 	for n in range(4):
# 		if tryNumber[n]==randomNumber[n]:
# 			counter2 += 1
# 			temp = temp[:n] + 'A' + temp[(n+1):]
# 			print(temp)
# 	for n in range(4): 
# 		if tryNumber[n] in temp and not (temp[n]=='A'):
# 			counter1 += 1
# 	print(str(counter1)+'+,'+str(counter2)+'++')
# 	tryNumber=input("Enter your guess number: ")