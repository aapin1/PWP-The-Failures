
from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib
import random
import os
import tkinter


def start():  #Main menu
  global root
  root = Tk()
  root.geometry()
  root.geometry("450x500")
  root.title("Login")
  intro = Label(root, text="Create account or login")
  intro.pack()
  create = Button(root, text="Create account", command = add) #Goes to add account
  create.pack()
  login = Button(root, text="Login", command = check) #Check function allows the user to login
  login.pack()
  quit_button = Button(root,text = "Quit",command = root.destroy) #Shut down
  quit_button.pack()
  root.mainloop()

def add():  #Create account
  root.destroy()
  global make
  global fname
  global lname
  global username
  global password
  make = Tk()
  make.geometry("450x500")
  make.title("Create account")
  fname = StringVar()
  lname = StringVar()
  username = StringVar()
  password = StringVar()
  name_label = Label(make,text = "Enter first name")
  name_label.pack()
  name = Entry(make, textvariable=fname)
  name.pack()
  lname_label = Label(make,text = "Enter last name")
  lname_label.pack() 
  lname = Entry(make, textvariable=lname)
  lname.pack()
  username_label = Label(make, text ="Enter your username")
  username_label.pack()
  username_input = Entry(make, textvariable=username)
  username_input.pack()
  password_label = Label(make, text = "Enter your password")
  password_label.pack()
  password_input = Entry(make, textvariable=password)
  password_input.pack()
  create = Button(make, text="Create account", command=create_account)
  create.pack()
  quit_button = Button(make,text = "Quit",command = lambda:exit(make))
  quit_button.pack()
  make.mainloop()
def create_account():
  fname_value = fname.get()
  lname_value = lname.get()
  username_value = username.get()
  password_value = password.get()
  keygen(fname_value, lname_value, username_value, password_value)
def exit(thing):
  thing.destroy()
  start()

def keygen(fname,lname,username,password):  #Generates a random key and saves to database

  salt = os.urandom(16)
  # hashed = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt
  password1 = password.encode('utf-8')
  password_hash = hashlib.pbkdf2_hmac('sha384', password1, salt, 100000)
  # cursor.execute('INSERT INTO emp VALUES ({key}, "{name}", "{lname}", "{user}", "{password}")'.format(key=keygen, name=fname, lname=lname, user=username, password=password_hash))
  cursor.execute( "INSERT INTO user_info (first_name, last_name, username, password_hash, salt) VALUES (?, ?, ?, ?, ?)",
    (fname, lname, username, password_hash, salt))

  connected.commit()
  connected.close()
  make.destroy()
  messagebox.showinfo('',"Your account has been created!")
  start()

def check(): #Login Function
  root.destroy()
  global check_window
  global userNameLog
  global passwordLog
  check_window = Tk()
  check_window.geometry("450x500")
  check_window.title("Login")
  userNameLog = StringVar()
  passwordLog = StringVar()
  userName_label = Label(check_window, text = "Enter your username")
  userName_label.pack()
  userName = Entry(check_window, textvariable=userNameLog)
  userName.pack()
  password_label = Label(check_window, text = "Enter your password")
  password_label.pack()
  password = Entry(check_window, textvariable=passwordLog, show = '*')
  password.pack()
  loginer = Button(check_window,text="Enter",command = preLogin) #Calls function that will send values over
  loginer.pack()
  quit_button = Button(check_window,text = "Quit",command = lambda:exit(check_window))
  quit_button.pack()
  check_window.mainloop()
def preLogin(): #Sends to login function
  userLog = userNameLog.get()
  passLog = passwordLog.get()
  login(userLog, passLog)

def login(username, password):  #Checks if username and password match within database
  user = str(username)
  passwo = str(password)
  cursor = sqlite3.connect('database.db')
  con = cursor.cursor()
  con.execute(
  "SELECT first_name, password_hash, salt FROM user_info WHERE username = ?",
  (user, ))
  find = con.fetchone()
  con.close()
  if find:
    userStored, passwordStored, saltStored, *_ = find 
    password1 = passwo.encode('utf-8')
    password_hash = hashlib.pbkdf2_hmac('sha384', password1, saltStored, 100000)
    if password_hash == passwordStored:
      menu(user)
    else:
      messagebox.showerror("", "Incorrect username or password")
      
  # cursor.execute("SELECT * FROM emp WHERE user = '{username}' AND pass = '{password}'".format(username=user,password = password_hash))
  # result = cursor.fetchall()
  # if result != []:
  #    menu(user)
  # else:
  #   messagebox.showinfo('',"Your account does not match our databases")
  #   check_window.destroy()
  #   start()
    
  
connected = sqlite3.connect("database.db")

def menu(u):  #The menu when you login
  userName = str(u)
  check_window.destroy()
  menu = tkinter.Tk()
  welcomemsg = Label(menu, text = f"Welcome {userName}")
  welcomemsg.grid(row = 0, column = 0)
  back_button = tkinter.Button(menu, text="Back")
  forward_button = tkinter.Button(menu, text="Forward")
  left_button = tkinter.Button(menu, text="Left")
  right_button = tkinter.Button(menu, text="Right")

  log = tkinter.Frame(menu)
  log.grid(row=6, column=0, padx=10, pady=10)
  logLabel = tkinter.Label(log, text="Log")
  logText = tkinter.Text(log, width=30, height=10)
  logLabel.grid(row=0, column=0, padx=5, pady=5)
  logText.grid(row=1, column=0, padx=5, pady=5)

  video = tkinter.Frame(menu)
  video.grid(row = 1, column = 0)
  videoCanvas = tkinter.Canvas(video, width=500, height=300, bg = 'grey')
  videoCanvas.grid(row = 0, column = 0)
  
  back_button.grid(row=2, column=2, padx=10, pady=10)
  forward_button.grid(row=1, column=2, padx=10, pady=10)
  left_button.grid(row=2, column=1, padx=10, pady=10)
  right_button.grid(row=2, column=3, padx=10, pady=10)

  quit_button = Button(menu, text = "Quit",command = lambda:exit(menu))
  quit_button.grid(row = 3, column = 2)
  menu.mainloop() 
# Creating a cursor object using the cursor method
cursor = connected.cursor()

# Creating a table
cursor.execute('''CREATE TABLE IF NOT EXISTS user_info (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fname TEXT,
lname TEXT,
username TEXT,
password_hash BLOB,
salt BLOB)''')





# Commiting the changes
connected.commit()


start()