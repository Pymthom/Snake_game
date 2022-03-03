
from tkinter import *
from database import high__score

from snake_main import play
name=None




def enter_name():
    root=Tk()
    root.title("Snake Game by Amir Chand Class XII" )
    root.geometry("500x100")
    root.configure(bg="Green")

    tro= Label(root,text="Enter Your name :",bg="green",fg="white").pack()

    lab=Entry(root)
    lab.pack()

    def name():
        global name
        name=""+lab.get()

        play(name)

        

    submit=Button(root,width=10,text="submit",fg="white",bg="green", command=name).pack()

    root.mainloop()


    
def check():
    root=Tk()
    root.title("Snake Game by Amir Chand Class XII" )
    root.geometry("500x100")
    root.configure(bg="Green")
    tro= Label(root,text="Enter Your name :",bg="green",fg="white").pack()

    lab=Entry(root)
    lab.pack()

    def name():
        global name
        name=""+lab.get()

        x=high__score(name)

        print(x)

        score= Label(root,text="Name : {}  High Score : {}".format(x[0],x[1]),bg="green",fg="white").pack()

        

    submit=Button(root,width=10,text="submit",fg="white",bg="green", command=name).pack()

    root.mainloop()




