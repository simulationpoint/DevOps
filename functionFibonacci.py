# Function for F(n) Fibonacci sequence

nthTerm = int(input("How many fibonacci sequence are you looking for: "))

# first two elements
firtElement = 0
seconedElement = 1
counter = 0

# check if the number of terms is valid
if nthTerm <= 0:
   print("Please enter a positive integer")
elif nthTerm == 1:
   print("Fibonacci sequence upto",nthTerm," are:")
   print(firtElement)
else:
   print("Fibonacci sequence:")
   while counter < nthTerm:
       print(firtElement)
       nthFibonacci = firtElement + seconedElement

       # recursive call

       firtElement = seconedElement
       seconedElement = nthFibonacci
       counter += 1
