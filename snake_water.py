import random
def gamewin(comp,you):       #  Game play between computer and you 
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
        
print("comp turn:snake(s) water(w) or Gun(g)?")
randomNo=random.randint(1,3)
if randomNo==1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==3:
    comp='g'
    
you= input("your turn:snake(s) water(w) or Gun(g)?")
a = gamewin(comp,you)
print(f"computer chose {comp}")
print(f"You chose {you}")
if a==None:
     print("the game is tia!")
elif a:
     print("you win!")
else:
     print("You lose!")