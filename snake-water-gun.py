import random

print("=============== Welcome ! In the Game of Snake,Water or Gun ==============")
def gamewin(comp,you):
    if comp==you:
        return None
    
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
        
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        
print("Comp turn :Snake(s) ,Water(w) or Gun(g):")
randno=random.randint(1,3)

if randno==1:
    comp='s'
elif randno==2:
    comp='w'        
elif randno==3:
    comp='g'        
            
you=input("Player 1 turn : Snake(s) ,Water(w) or Gun(g)?- ")
a=gamewin(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}") 

if a==None:
    print("The Game is a Tie !")
elif a :
    print("You Win !")
else :
    print("You Lose !")   
        
    