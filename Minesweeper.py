#encoding=utf-8

import random

def reveal(field,unlock):
    S
    return
def unlock(coordinates,field1):
    x=coordinates[0]
    y=coordinates[1]
    unlock=(x*y)-((y-1)*x)+1
    if y < 8:
        unlock=(((9-y)*(9))+(unlock))-(1*y+1)
    field1[unlock]=reveal(field,unlock)
    return s

def mineSweeper(field):
    field1=field
    counter=0
    while counter!=8:
        x=random.randint(1,len(field1))
        if field1[x] =="*":
            field1[x]="M"
            counter+=1
    return

field=["(y)"'\n'
       " 8","*","*","*","*","*","*","*","*",'\n'
       " 7","*","*","*","*","*","*","*","*",'\n'
       " 6","*","*","*","*","*","*","*","*",'\n'
       " 5","*","*","*","*","*","*","*","*",'\n'
       " 4","*","*","*","*","*","*","*","*",'\n'
       " 3","*","*","*","*","*","*","*","*",'\n'
       " 2","*","*","*","*","*","*","*","*",'\n'
       " 1","*","*","*","*","*","*","*","*",'\n'
       "  ","1","2","3","4","5","6","7","8","(x)"]    
print("Welcome to Minesweeper!\nType 'Help' if you want instructions for this game!\nType 'Start' if you want to begin!")
print(*field)
answer=input("What do you want to do?\n: ")
if answer == "start":
    field=mineSweeper(field)
    field1[unlock]=0
    for k in range(9,12):
        if field1[unlock+k]=="M":
            field1[unlock]+=1
        if field1[unlock+1]=="M":
                field1[unlock]+=1
        if field1[unlock-1]=="M":
            field1[unlock]+=1
    for k in range(9,12):
        if field1[unlock-k]=="M":
            field1[unlock]+=1
    print(*field1)