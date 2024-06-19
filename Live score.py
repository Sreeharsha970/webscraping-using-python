#Live cricket score using python

from pycricbuzz import Cricbuzz   #input 
from tkinter import *


root=Tk()   # Tk function
root.title("Live cricket score")

root.geometry("100x850")    #dimensions of height and width


c = Cricbuzz()        # c is variable , cricbuzz is asinged to c variable
match = c.matches

score = c.livescore(match[0]['id'])   #match is stored in list
commentary = c.commentary(match[0]['id'])   #commentary is stored in list
score_board = c.scorecard(match[0]['id'])   #scoreboard is stored in list

for a in score :
    print(a)
    for b in score[a] :
        print(b,':',score[a][b])


    #scoreboard is changes to string , it will be form as dictonary format
s=str(score_board)                      # thatswhy score is changes to string
k=s.replace(",","\n")  # replace string ,data came from line by line


score1=Label(root,font=("time",15,"bold"),bg="white",text=k)
# label is created to root basedon gui application, 15 means size,bold is fontstyle
score1.grid(row=2,column=2,pady=25,padx=100)


root.mainloop() 










