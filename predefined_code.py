from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x400")



dictionary = {'Colours :'["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1",
"deep pink","cyan"]
}

def bg_color():
    random1 = random.randint(0,8)
    print(dictionary["Colours"][random1])
    root.configure(background=dictionary["Colours"][random1])

btn = Button(root , text = 'Click me to change bg colour' , command=bg_color)
btn.place(relx=0.5 , rely=0.5,anchor=CENTER)

root.mainloop()
 
