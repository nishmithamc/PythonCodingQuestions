import random

i=input("Please Enter the range of number :")

if i.isdigit():
    i=int(i)

    if i==0:
        print("Please Enter the Number which is Larger than 0")
        quit()
else:
    print("Not a valid Digit !!")
    quit()

a=random.randint(1,i)

s=0 #Variable declared to store the number of times user taken a chance to guess the right answer

while True:
    s+=1

    guess_number=input("Guess a number ! :")

    if guess_number.isdigit():
        guess_number=int(guess_number)

        if guess_number==a:
            print("You are correct")
            break
        else:
            if guess_number>a: #hint to the user
                print("You are above the Number !")
            else:
                print("You are below the Number !")

    else:
        print("Please enter a valid Number")
        continue

print(f"You got it correct in {s} number of attempts")



#Python program to guess a number
