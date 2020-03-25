inputString=input("Enter your string: ")
counter=0
vowels=['a','o','u','e','i']
for Letter in inputString:
	if Letter in vowels:
		counter +=1
print(counter)