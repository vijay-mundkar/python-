num = int(input("Enter the number :"))
count = 0
for i in range(2,num-1):
    if num % i == 0:
        count = 2
if count:
    print("It is a prime not number :")
else:
    print("It is prime number")
