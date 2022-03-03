from cgitb import text
from textwrap import fill
from tkinter import *

import interface  as ift






root=Tk()
root.title("Snake Game by Amir Chand Class XII" )
root.geometry("1000x1000")
root.configure(bg="Green")

intro= Label(root,text="Welcome to the \nJUNGLE",font=( "Times New Roman", 50, "normal"),bg="green",fg="white").pack()


tro= Label(root,text="\n",bg="green",fg="white").pack()
tro= Label(root,text="\n",bg="green",fg="white").pack()

#NEW game tab
new_game=Button(root,width=50,text="NEW GAME",fg="white",bg="green",command=ift.enter_name)


new_game.pack()

tro= Label(root,text="\n",bg="green",fg="white").pack()

#High score tab
high_score=Button(root,width=50,text="HIGH SCORE",fg="white",bg="green",command=ift.check)

high_score.pack()

root.mainloop()
