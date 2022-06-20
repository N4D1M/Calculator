
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")    # .cget() function is used to get text from widget(button widget)
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get() + text)
        screen.update()


    

window = Tk()
window.geometry("500x650") #width x height
window.maxsize(500, 650) 
window.title("Calculator")
window.configure(background="black")
# window.wm_iconbitmap("1.icon") #to add icon 

l1=Label(window,text="Calculator", width=10, fg="white", bg="navy blue", font="lucida 25 bold")
l1.place(x=30, y=50)

scvalue = StringVar()
scvalue.set("")
screen = Entry(window, textvariable=scvalue, font="lucida 30 bold")
screen.place(x=30, y=100)

#frame 1
fram1 = Frame(window, bg="black")
fram1.place(x=60, y=200)

btn1 = Button(fram1, text="C", width=5, fg="white", bg="black", font="lucida 18 bold")
btn1.pack(side=LEFT, padx=18, pady=12)
btn1.bind('<Button-1>',click)

btn2 = Button(fram1, text="9", width=5, fg="white", bg="black", font="lucida 18 bold")
btn2.pack(side=LEFT, padx=18, pady=12)
btn2.bind('<Button-1>',click)

btn3 = Button(fram1, text="8", width=5, fg="white", bg="black", font="lucida 18 bold")
btn3.pack(side=LEFT, padx=18, pady=12)
btn3.bind('<Button-1>',click)

#frame 2
fram1 = Frame(window, bg="black")
fram1.place(x=60, y=270)

btn1 = Button(fram1, text="7", width=5, fg="white", bg="black", font="lucida 18 bold")
btn1.pack(side=LEFT, padx=18, pady=12)
btn1.bind('<Button-1>',click)

btn2 = Button(fram1, text="6", width=5, fg="white", bg="black", font="lucida 18 bold")
btn2.pack(side=LEFT, padx=18, pady=12)
btn2.bind('<Button-1>',click)

btn3 = Button(fram1, text="5", width=5, fg="white", bg="black", font="lucida 18 bold")
btn3.pack(side=LEFT, padx=18, pady=12)
btn3.bind('<Button-1>',click)

#frame 3
fram1 = Frame(window, bg="black")
fram1.place(x=60, y=340)

btn1 = Button(fram1, text="4", width=5, fg="white", bg="black", font="lucida 18 bold")
btn1.pack(side=LEFT, padx=18, pady=12)
btn1.bind('<Button-1>',click)

btn2 = Button(fram1, text="3", width=5, fg="white", bg="black", font="lucida 18 bold")
btn2.pack(side=LEFT, padx=18, pady=12)
btn2.bind('<Button-1>',click)

btn3 = Button(fram1, text="2", width=5, fg="white", bg="black", font="lucida 18 bold")
btn3.pack(side=LEFT, padx=18, pady=12)
btn3.bind('<Button-1>',click)


#frame 4
fram1 = Frame(window, bg="black")
fram1.place(x=60, y=410)

btn1 = Button(fram1, text="1", width=5, fg="white", bg="black", font="lucida 18 bold")
btn1.pack(side=LEFT, padx=18, pady=12)
btn1.bind('<Button-1>',click)

btn2 = Button(fram1, text="0", width=5, fg="white", bg="black", font="lucida 18 bold")
btn2.pack(side=LEFT, padx=18, pady=12)
btn2.bind('<Button-1>',click)

btn3 = Button(fram1, text="*", width=5, fg="white", bg="black", font="lucida 18 bold")
btn3.pack(side=LEFT, padx=18, pady=12)
btn3.bind('<Button-1>',click)


#frame 5
fram1 = Frame(window, bg="black")
fram1.place(x=60, y=480)

btn1 = Button(fram1, text="-", width=5, fg="white", bg="black", font="lucida 18 bold")
btn1.pack(side=LEFT, padx=18, pady=12)
btn1.bind('<Button-1>',click)

btn2 = Button(fram1, text="+", width=5, fg="white", bg="black", font="lucida 18 bold")
btn2.pack(side=LEFT, padx=18, pady=12)
btn2.bind('<Button-1>',click)

btn3 = Button(fram1, text="/", width=5, fg="white", bg="black", font="lucida 18 bold")
btn3.pack(side=LEFT, padx=18, pady=12)
btn3.bind('<Button-1>',click)



#frame 6
fram1 = Frame(window, bg="black")
fram1.place(x=60, y=550)

btn1 = Button(fram1, text="%", width=5, fg="white", bg="black", font="lucida 18 bold")
btn1.pack(side=LEFT, padx=18, pady=12)
btn1.bind('<Button-1>',click)

btn2 = Button(fram1, text=".", width=5, fg="white", bg="black", font="lucida 18 bold")
btn2.pack(side=LEFT, padx=18, pady=12)
btn2.bind('<Button-1>',click)

btn3 = Button(fram1, text="=", width=5, fg="white", bg="black", font="lucida 18 bold")
btn3.pack(side=LEFT, padx=18, pady=12)
btn3.bind('<Button-1>',click)







# Button(window, text="Cancel", width=15, fg="white", bg="red", font=("bold 13")).place(x=250,y=450)

window.mainloop() 