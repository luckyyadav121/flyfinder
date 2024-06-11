from tkinter import *
import gui
import data_manager
import pprint
import flight_searcher
import notification_manager
import datetime

if __name__ == "__main__":
    win = Tk()

    #gui.deshboard(trail_data)
    # app title
    win.title("Flight Manager")

    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    # heading label
    heading = Label(win, text="Login", font='Verdana 25 bold')
    heading.place(x=80, y=150)

    username = Label(win, text="User Name :", font='Verdana 10 bold')
    username.place(x=80, y=220)

    userpass = Label(win, text="Password :", font='Verdana 10 bold')
    userpass.place(x=80, y=260)

    # Entry Box
    user_name = StringVar()
    password = StringVar()

    userentry = Entry(win, width=40, textvariable=user_name)
    userentry.focus()
    userentry.place(x=200, y=223)

    passentry = Entry(win, width=40, show="*", textvariable=password)
    passentry.place(x=200, y=260)

    # button login and clear

    btn_login = Button(win, text="Login", font='Verdana 10 bold', command=gui.login)
    btn_login.place(x=200, y=293)

    btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=gui.clear)
    btn_login.place(x=260, y=293)

    # signup button

    sign_up_btn = Button(win, text="Switch To Sign up", command=gui.signup)
    sign_up_btn.place(x=350, y=20)

    #LOOP MAI CHALATI REHTI HAI
    win.mainloop()
