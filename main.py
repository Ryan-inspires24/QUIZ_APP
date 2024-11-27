from tkinter import*
from Classes.User import *

window = Tk()
window.title('Simple Quiz Calculator')
user = User(userName='', firstName='', lastName='', Class='')

label = Label(window, text='Welcome, would you like to register or Login?')
label.pack(padx=50, pady=50)

register_btn = Button(window, text='Register', command=user.RegisterUserInfo)
login_btn = Button(window, text='Login', command=user.Login)

register_btn.pack(padx=50, pady=50)
login_btn.pack(padx=50, pady=50) 
window.mainloop()

