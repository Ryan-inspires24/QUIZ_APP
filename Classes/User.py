from tkinter import *
from tkinter import messagebox
import os

class User:
    
    def __init__(self, userName, firstName, lastName, Class):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.Class = Class
        
    def RegisterUserInfo(self):
        register_window = Tk()
        register_window.title('USER REGISTERATION') 

        fn_frame = Frame(register_window)
        fn_lbel = Label(fn_frame, text='First Name')
        fn_entry = Entry(fn_frame)
        
        fn_frame.pack(padx=120, pady=20)
        fn_lbel.pack(side=LEFT)
        fn_entry.pack(side=RIGHT)
        
        ln_frame = Frame(register_window)
        ln_lbel = Label(ln_frame, text='Last Name')
        ln_entry = Entry(ln_frame)
        
        ln_frame.pack(padx=120, pady=20)
        ln_lbel.pack(side=LEFT)
        ln_entry.pack(side=RIGHT)
        
        user_frame = Frame(register_window)
        user_lbel = Label(user_frame, text='User Name')
        user_entry = Entry(user_frame)
        
        user_frame.pack(padx=120, pady=20)
        user_lbel.pack(side=LEFT)
        user_entry.pack(side=RIGHT)
        
        def register():
            self.userName = user_entry.get()
            self.firstName = fn_entry.get()
            self.lastName = ln_entry.get()
            userFile = open(f'{self.userName}.txt','w')
            userFile.close
            messagebox.showinfo('Success!', f'Welcome {self.userName}!')
        
        reg_btn = Button(register_window, text='REGISTER', command=register)
        reg_btn.pack(padx=50, pady=50)        

    
    def Login(self):
            login_window = Tk()
            login_window.title('USER REGISTERATION') 

            user_frame = Frame(login_window)
            user_lbel = Label(user_frame, text='Enter your user name please.')
            user_entry = Entry(user_frame)
        
            user_frame.pack(padx=120, pady=20)
            user_lbel.pack(side=LEFT)
            user_entry.pack(side=RIGHT)
           

            def login():
                self.userName = user_entry.get()
                file_path = f"{self.userName}.txt"
        
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                            file_contents = file.read()
            
                    messagebox.showinfo('Success!', f'Welcome back {self.userName}')
                else:
                    messagebox.showerror('Login Error', f"Sorry, the user '{self.userName}' does not exist.")


            login_btn = Button(login_window, text='Login', command=login)
            login_btn.pack(padx=50, pady=50)