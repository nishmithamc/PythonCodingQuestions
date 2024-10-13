#To accept n numbers from the user and append only the prime numbers to the list

n=int(input("enter the number of elements"))
prime_numbers=[]
for i in range(n):
    num=int(input(f'enter the number{i+1}'))
    if num > 1:
        isPrime=True
        for j in range(2,num):
            if num%j==0:
                isPrime=False
                break
        if isPrime:
            prime_numbers.append(num)
print('prime numbers are:',prime_numbers)
