from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
count=0
#print random_number
# Start your game!4
while count<3:
    num=input("Guess a number")
    if num==random_number :
        print "Hurray...You win"
        count+=1
        break
    else:
        print "You lose, Bad luck Try again "
        count+=1
print"The number right is  %d"%random_number
    
    
    
    
