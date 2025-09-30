from tkinter import *
window = Tk()

window.title("")

photo = PhotoImage(file='Square_compasses.svg.png')

label = Label(window,
              text="What is Freemasonry?",
              font=('Arial',40,'bold'),
              fg='#f2f2f2',
              bg='#0d2838',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

label.pack()

window.mainloop()

