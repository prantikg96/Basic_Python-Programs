a = int(input('Enter first number  : ')) #input 1st integer
b = int(input('Enter second number : ')) #input 2nd integer
c = int(input('Enter third number  : ')) #input 3rd integer
if a < b and a < c :
 smallest = a
elif b < c :
 smallest = b
else :
 smallest = c
print("\n",smallest, "is the smallest of three numbers.")
