#encoding=utf-8

import random

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