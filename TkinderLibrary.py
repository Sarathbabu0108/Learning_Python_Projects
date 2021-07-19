from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("sarath")
window.configure(bg="green")


def hello():
    print("button clicked")

button1 = Button(window,text="ok", bg = "yellow", fg= "black", command = hello)
button2 = Button(window,text="cancel ", bg = "yellow", fg= "black", command = hello)
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

window.mainloop()
