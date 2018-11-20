import tkinter
from tkinter import *
from tkinter import messagebox

import database
import gui

def test():
    print('Clicked')

#Login Button click from login Frame
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    rows = database.view_owner(username)
    if not rows:
        print('Invalid user name or passowrd')
        messagebox.showerror("Oops!",'Invalid Username')
    else:
        if rows[0][1] == password:
            print(rows)
            loginWindow.destroy()
            gui.home(username)
        else:
            messagebox.showerror('Oops!','Invalid Password')
            forgotPassButton.grid(row = 2, column = 1, sticky = E)

#signup button click form Login frame
def signUp():
    new_username.set('')
    new_password.set('')
    loginFrame.pack_forget()
    Header['text'] = 'Create Account'
    createAccFrame.pack()

def createAccount():
    username = n_usernameEntry.get()
    password = n_passwordEntry.get()
    #dont create a empty username
    if username == '':
        messagebox.showwarning('Error','Enter username')
        return

    rows = database.view_owner(username)
    if rows:
        messagebox.showerror("Oops!",'Username Aldready Exists')
    else:
        database.insert_owner(username,password)
        messagebox.showinfo('Registered','Sucessfully Signed Up')
        gotoLogin()

def gotoLogin():
    username.set('')
    password.set('')
    createAccFrame.pack_forget()
    Header['text'] = 'LOGIN'
    loginFrame.pack()

#Password reset functions
def passReset():
    new_username.set('')
    new_username.set('')
    loginFrame.pack_forget()
    Header['text'] = "Password Reset"
    passResetFrame.pack()

def gotoLogin_from_passreset():
    username.set('')
    password.set('')
    passResetFrame.pack_forget()
    Header['text'] = "LOGIN"
    loginFrame.pack()

def passResetSubmit():
    username = usernameEntry1.get()
    new_password_1 = passresetEntry1.get()
    new_password_2 = passresetEntry2.get()

    rows = database.view_owner(username)
    if not rows:
        messagebox.showerror("Oops!",'Invalid Username')
    else:
        if new_password_1 != new_password_2:
            messagebox.showwarning('Error','Passwords do not match.')
        else:
            database.update_owner(username,new_password_1)
            messagebox.showinfo('Sucess','Password Changed')
            gotoLogin_from_passreset()

#main window login
loginWindow = Tk()
loginWindow.title("ROG Login(owner)")

def on_closing():
    if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            loginWindow.destroy()
loginWindow.protocol("WM_DELETE_WINDOW", on_closing)

Header = Label(loginWindow, text = 'LOGIN', font = ('',35), pady = 10)
Header.pack()

username = StringVar()
password = StringVar()
new_username = StringVar()
new_password = StringVar()
new_password2 = StringVar()

#login Frame
loginFrame = Frame(loginWindow, padx = 100, pady = 10)

usernameLabel = Label(loginFrame, text = "Username: ")
usernameLabel.grid(row = 0, column = 0)
usernameEntry = Entry(loginFrame, textvariable = username, bd = 3)
usernameEntry.grid(row = 0, column = 1)

passwordLabel = Label(loginFrame, text = "Paswword: ")
passwordLabel.grid(row = 1, column = 0)
passwordEntry = Entry(loginFrame, textvariable = password, show = '*', bd = 3)
passwordEntry.grid(row = 1, column = 1)

signUpButton = Button(loginFrame, text = 'Sign Up', font = ('',10), padx = 5, pady = 5, fg = 'red', command = signUp)
signUpButton.grid(row = 3, column = 0, sticky = W)

loginButton = Button(loginFrame, text = 'Login', font = ('',15), padx = 5, pady = 5, bg = 'blue', command = login)
loginButton.grid(row = 3, column = 1)

forgotPassButton = Button(loginFrame, text = 'Forgot password', font = ('',8), fg = 'blue', command = passReset)

loginFrame.pack()



#Create Account frame
createAccFrame = Frame(loginWindow, padx = 100, pady = 10)

n_usernameLabel = Label(createAccFrame, text = "Username: ")
n_usernameLabel.grid(row = 0, column = 0)
n_usernameEntry = Entry(createAccFrame, textvariable = new_username, bd = 3)
n_usernameEntry.grid(row = 0, column = 1)

n_passwordLabel = Label(createAccFrame, text = "Paswword: ")
n_passwordLabel.grid(row = 1, column = 0)
n_passwordEntry = Entry(createAccFrame, textvariable = new_password, show = '*', bd = 3)
n_passwordEntry.grid(row = 1, column = 1)

gotoLoginButton = Button(createAccFrame, text = 'Go to Login', font = ('',10), padx = 5, pady = 5, fg = 'red', command = gotoLogin)
gotoLoginButton.grid(row = 2, column = 0, sticky = W)

createAccButton = Button(createAccFrame, text = 'Create Account', font = ('',15), padx = 5, pady = 5, bg = 'blue', command = createAccount)
createAccButton.grid(row = 2, column = 1)


#Reset Password
passResetFrame = Frame(loginWindow, padx = 100, pady = 10)

usernameLabel = Label(passResetFrame, text = "Username: ")
usernameLabel.grid(row = 0, column = 0)
usernameEntry1 = Entry(passResetFrame, textvariable = new_username, bd = 3)
usernameEntry1.grid(row = 0, column = 1)

passresetLabel1 = Label(passResetFrame, text = "New Password: ")
passresetLabel1.grid(row = 1, column = 0)
passresetEntry1 = Entry(passResetFrame, textvariable = new_password, show = '*', bd = 3)
passresetEntry1.grid(row = 1, column = 1)

passresetLabel2 = Label(passResetFrame, text = "Re-Enter Password: ")
passresetLabel2.grid(row = 2, column = 0)
passresetEntry2 = Entry(passResetFrame, textvariable = new_password2, show = '*', bd = 3)
passresetEntry2.grid(row = 2, column = 1)

gotoLoginButton = Button(passResetFrame, text = 'Go to Login', font = ('',10), padx = 5, pady = 5, fg = 'red', command = gotoLogin_from_passreset)
gotoLoginButton.grid(row = 3, column = 0, sticky = W)

submitButton = Button(passResetFrame, text = 'Submit', font = ('',15), padx = 5, pady = 5, bg = 'blue', command = passResetSubmit )
submitButton.grid(row = 3, column = 1)

loginWindow.mainloop()