import random
dic={0:"Scissor",1:"Paper",2:"Rock"}
a = random.randint(0,3)
b = int(input("Enter any number\n0 for scissor\n1 for paper\n2 for rock\n"))
print("you chose ",dic[b])
print("Computer chose ",dic[a])

if(a==b):
    print("Draw")

elif(a==0):
    if(b==1):
        print("you lose")
    if(b==2):
        print("you win")
elif(a==1):
    if(b==2):
        print("you lose")
    if(b==0):
        print("you win")
elif(a==2):
    if(b==1):
        print("you lose")
    if(b==0):
        print("you win")

    
