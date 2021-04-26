#encoding=utf-8

import os
import random

def revealFirstTime(field1,unlock,field):
    c=0
    if unlock>81 or unlock<0:
        return 
    if field1[unlock]!="*":
        if field1[unlock]=="M" and not (field[unlock]=="f" or field[unlock]=="F") :
            return "*"
        return field1[unlock]
    for k in range(8,11):
        if unlock+k<72:
            if field1[unlock+k]=="M":
                c+=1
    if field1[unlock+1]=="M":
        c+=1
    if field1[unlock-1]=="M":
        c+=1
    for k in range(8,11):
        if unlock-k>0:
            if field1[unlock-k]=="M": 
                c+=1
    if c>0:
        field[unlock]=c
    elif c==0:
        field[unlock]=0
    return c
def reveal(field1,unlock,field,firstTimeCheck):
    failed=-1
    c=0  
    if field1[unlock]=="M":
        return failed
    if field1[unlock]!="*":
        return field1[unlock]
    for k in range(8,11):
        if unlock+k<72:
            if field1[unlock+k]=="M":
                c+=1
    if field1[unlock+1]=="M":
        c+=1
    if field1[unlock-1]=="M":
        c+=1
    for k in range(8,11):
        if unlock-k>0:
            if field1[unlock-k]=="M": 
                c+=1
    if c>0:
        field[unlock]=c
    elif c==0:
        field[unlock]=0
    if firstTimeCheck==1:
        if c>0:
            for k in range(8,11):
                a=unlock+k
                if a<72 and a>0:
                    field[unlock+k]=revealFirstTime(field1,a,field)
            k=1
            a=unlock+k
            if a<72 and a>0:
                field[unlock+k]=revealFirstTime(field1,a,field)
            k=-1
            a=unlock+k
            if a<72 and a>0:
                field[unlock+k]=revealFirstTime(field1,a,field)  
            for k in range(-8,-11,-1):
                c=0
                a=unlock+k
                if a<72 and a>0:
                    c=revealFirstTime(field1,a,field)
                    field[unlock+k]=c
    counter=-1
    while 0 in field:
        counter=0
        for i in field:
            counter+=1
            if i ==0:
                for k in range(8,11):
                    a=counter+k
                    if a<72 and a>0:
                        c=revealFirstTime(field1,a,field)
                        if c==0:
                            field[counter+k]="0"                
                            field[counter+k]=c                   
                k=1
                a=counter+k
                if a<72 and a>0:
                    c=revealFirstTime(field1,a,field)
                    if c==0:
                        c="0"          
                    field[counter+k]=c 
                k=-1
                a=counter+k
                if a<72 and a>0:
                    c=revealFirstTime(field1,a,field) 
                    if c==0:
                        c="0"              
                    field[counter+k]=c  
                for k in range(-8,-11,-1):
                    c=0
                    a=counter+k
                    if a<72 and a>0:
                        c=revealFirstTime(field1,a,field)
                        field[counter+k]=c
                        if c==0:
                            field[counter+k]="0"
    return field

def unlock(coordinates,field1,field,firstTimeCheck):
    x=int(coordinates[0])
    y=int(coordinates[2])
    unlock=(x*y)-((y-1)*x)
    if y < 8:
        unlock=((8-y)*(9))+(unlock)
    field=reveal(field1,unlock,field,firstTimeCheck)
    return field

def answer1(field):
    coordinates="00000"
    while len(coordinates)!=3 and coordinates[0]!="f" and coordinates[0]!="F":
        coordinates=input("Type in the X and Y coordinates you want to unlock in the following format\n 'x,y', if you wanna mark a flag type 'F' and then the coordinates.\n : ")
    while coordinates=="F" or coordinates=="f":
        coordinates=input("Type in the coordinates in the following format 'x,y' : ")
        while len(coordinates)!=3 or not (coordinates[0].isdigit() and coordinates[2].isdigit()) or coordinates[0]=="0" or coordinates[0]=="9" or coordinates[2]=="0" or coordinates[2]=="9":
            coordinates=input("Make sure you are typing in this format 'x,y': ")
        x=int(coordinates[0])
        y=int(coordinates[2])
        unlock=(x*y)-((y-1)*x)
        if y < 8:
            unlock=((8-y)*(9))+(unlock)
        if field[unlock]=="*":
            field[unlock]="F"
            print(*field)
            print("\nCoordinate",coordinates,"flagged")
        coordinates=input("Type in the X and Y coordinates you want to unlock in the following format\n 'x,y', if you wanna mark a flag type 'F' and then the coordinates.\n : ")
        while len(coordinates)!=3 and coordinates[0]!="f" and coordinates[0]!="F":
            coordinates=input("Type in the X and Y coordinates you want to unlock in the following format\n 'x,y', if you wanna mark a flag type 'F' and then the coordinates.\n : ")
    
    if len(coordinates)==3:
        while not (coordinates[0].isdigit() and coordinates[2].isdigit()) or len(coordinates)!=3 or coordinates[0]=="0" or coordinates[0]=="9" or coordinates[2]=="0" or coordinates[2]=="9":
            coordinates=input("Make sure you are typing this format 'x,y': ")
        if coordinates[0] == 0 or coordinates[2] == 0:
            coordinates=input("No 0's are allowed. Please type again. 'x,y': ")
    return coordinates

def mineSweeper():
    field=["(y)"'\n'
           " 8 ","*","*","*","*","*","*","*","*",'\n'
           " 7 ","*","*","*","*","*","*","*","*",'\n'
           " 6 ","*","*","*","*","*","*","*","*",'\n'
           " 5 ","*","*","*","*","*","*","*","*",'\n'
           " 4 ","*","*","*","*","*","*","*","*",'\n'
           " 3 ","*","*","*","*","*","*","*","*",'\n'
           " 2 ","*","*","*","*","*","*","*","*",'\n'
           " 1 ","*","*","*","*","*","*","*","*",'\n'
           "   ","1","2","3","4","5","6","7","8","(x)"]
    print(*field)
    field1=["(y)"'\n'
           " 8 ","*","*","*","*","*","*","*","*",'\n'
           " 7 ","*","*","*","*","*","*","*","*",'\n'
           " 6 ","*","*","*","*","*","*","*","*",'\n'
           " 5 ","*","*","*","*","*","*","*","*",'\n'
           " 4 ","*","*","*","*","*","*","*","*",'\n'
           " 3 ","*","*","*","*","*","*","*","*",'\n'
           " 2 ","*","*","*","*","*","*","*","*",'\n'
           " 1 ","*","*","*","*","*","*","*","*",'\n'
           "   ","1","2","3","4","5","6","7","8","(x)"]
    counter=0
    while counter!=8:
        x=random.randint(1,len(field1)-1)
        if field1[x] =="*":
            field1[x]="M"
            counter+=1
    counter=0
    counter1=0
    firstTimeCheck=1
    while counter!=8 and counter1!=0:
        for i in field:
            if i =="*":
                counter1+=1
            if i =="F":
                counter+=1
        answer=answer1(field)
        field=unlock(answer,field1,field,firstTimeCheck)
        firstTimeCheck=0
        if field==-1:
            answer=input("You hit a bomb, wanna go again? (yes/no): ")
            while answer!="yes" and answer!="Yes" and answer !="no" and answer!="No":
                answer=input("(Input Error) You hit a bomb, wanna go again? (yes/no): ")
            return answer
        print(*field)
    answer=1
    return answer


print("Welcome to Minesweeper!\nType 'Help' if you want instructions for this game!\nType 'Start' if you want to begin!")
answer=input("What do you want to do?\n: ")
while answer!="start" and answer!="Start" and answer!="Start." and answer!="start.":
    answer=input("What do you want to do?\n: ")
while answer=="start" or answer=="Start" or answer=="Start." or answer=="start.":
    answer=mineSweeper()
    while answer=="yes" or answer=="Yes" or answer=="yes." or answer=="Yes.":
        answer=mineSweeper()
    if answer==1:
        print("Thank you for playing!")