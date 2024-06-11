from tkinter import *
import flight_searcher
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import json
from datetime import datetime, timezone


# ---------------------------------------------------------------Login Function --------------------------------------
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    else:
        with open("customers.json", "r") as file:
            data = json.load(file)
            data = data["customers"]
            print(data)
            for temp in data:
                if temp["username"] == user_name.get() and temp["password"] == password.get():
                    messagebox.showinfo("Success", "Successfully Login", parent=win)
                    close()
                    dashboard(temp)
            else:
                messagebox.showerror("Error", "Invalid User Name Or Password", parent=win)


# ------------------------------------------------ End Login Function ---------------------------------

# ------------------------------------------------- DeshBoard Panel -----------------------------------------
def display_flights(data, user):

    des = Tk()
    des.title("Flight Manager")
    des.maxsize(width=1100, height=500)
    des.minsize(width=1100, height=500)

    # img = ImageTk.PhotoImage(Image.open("images/bg6.jpg"))
    # # Add image to the Canvas Items
    # canvas = Canvas(des, width=900, height=400)
    # canvas.create_image(0, 0, anchor='nw', image=img)
    # canvas.pack()

    print(data)
    Y_AXIS = 300
    canvas = Canvas(des)
    flight_no_l = Label(des, text="Flight no.", font='Verdana 11 bold')
    flight_no_l.place(x=20, y=60)
    # canvas.create_line(100, 240, 100, 650, width=2)

    from_country_l = Label(des, text="Departure", font='Verdana 11 bold')
    from_country_l.place(x=20, y=90)
    # canvas.create_line(200, 240, 200, 650, width=1)

    to_country_l = Label(des, text="Destination", font='Verdana 11 bold')
    to_country_l.place(x=20, y=120)
    # canvas.create_line(300, 240, 300, 650, width=1)

    date_l = Label(des, text="Date", font='Verdana 11 bold')
    date_l.place(x=20, y=150)
    # canvas.create_line(400, 240, 400, 750, width=1)

    departure_time_l = Label(des, text="Departure Time", font='Verdana 11 bold')
    departure_time_l.place(x=20, y=180)
    # canvas.create_line(500, 240, 500, 750, width=1)

    arrival_time_l = Label(des, text="Arrival Time", font='Verdana 11 bold')
    arrival_time_l.place(x=20, y=210)
    # canvas.create_line(600, 240, 600, 750, width=1)


    total_duration = Label(des, text="Total Duration", font='Verdana 11 bold')
    total_duration.place(x=20, y=240)
    # canvas.create_line(700, 240, 700, 850, width=1)

    distance = Label(des, text="Distance", font='Verdana 11 bold')
    distance.place(x=20, y=270)
    # canvas.create_line(700, 240, 700, 850, width=1)

    availability_l = Label(des, text="availability", font='Verdana 11 bold')
    availability_l.place(x=20, y=300)
    # canvas.create_line(700, 240, 700, 850, width=1)

    bag = Label(des, text="Luggage Weight", font='Verdana 11 bold')
    bag.place(x=20, y=330)

    extra_bag = Label(des, text="Extra luggage price", font='Verdana 11 bold')
    extra_bag.place(x=20, y=360)

    fare_l = Label(des, text="Fare", font='Verdana 11 bold')
    fare_l.place(x=20, y=390)
    # canvas.create_rectangle(0, 280, 800, 282, fill="black")
    # canvas.pack()

    i = len(data)
    j = 0
    if i==0:
        messagebox.showinfo(" ", "No flight Available", parent=win)
        close()
        dashboard(user)

    while i:
        details = data[j]
        j += 1
        temp = details['utc_departure']
        dpt = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)
        temp = details['utc_arrival']
        arv = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)

        flight_no_l = Label(des, text=f"{details['flight_no']}", font='Verdana 10 bold')
        flight_no_l.place(x=220, y=60)
        # canvas.create_line(100, 240, 100, 650, width=2)

        from_country_l = Label(des, text=f"{details['from']['city']}, {details['from']['country']}", font='Verdana 10 normal')
        from_country_l.place(x=220, y=90)
        # canvas.create_line(200, 240, 200, 650, width=1)

        to_country_l = Label(des, text=f"{details['to']['city']}, {details['to']['country']}", font='Verdana 10 normal')
        to_country_l.place(x=220, y=120)
        # canvas.create_line(300, 240, 300, 650, width=1)

        date_l = Label(des, text=f"{dpt.strftime('%d-%m-%Y')}", font='Verdana 10 normal')
        date_l.place(x=220, y=150)
        # canvas.create_line(400, 240, 400, 750, width=1)

        departure_time_l = Label(des, text=f"{dpt.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        departure_time_l.place(x=220, y=180)
        # canvas.create_line(500, 240, 500, 750, width=1)

        arrival_time_l = Label(des, text=f"{arv.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        arrival_time_l.place(x=220, y=210)
        # canvas.create_line(600, 240, 600, 750, width=1)

        total_duration = Label(des, text=f"{details['duration']}", font='Verdana 10 normal')
        total_duration.place(x=220, y=240)
        # canvas.create_line(700, 240, 700, 850, width=1)

        distance = Label(des, text=f"{details['distance']}", font='Verdana 10 normal')
        distance.place(x=220, y=270)
        # canvas.create_line(700, 240, 700, 850, width=1)

        availability_l = Label(des, text=f"{details['availability']}", font='Verdana 10 normal')
        availability_l.place(x=220, y=300)
        # canvas.create_line(700, 240, 700, 850, width=1)

        bag_limit = Label(des, text=f"{details['bag_limit']} Kg", font='Verdana 10 normal')
        bag_limit.place(x=220, y=330)

        extra_bag_cost = Label(des, text=f"₹ {details['bags_price']['1']} per bag", font='Verdana 10 normal')
        extra_bag_cost.place(x=220, y=360)

        fare_l = Label(des, text=f"₹ {details['price']}", font='Verdana 10 normal')
        fare_l.place(x=220, y=390)

        i -= 1


def dashboard(user):

    # def display_flights(data):
    #     print(data)
    #     Y_AXIS = 300
    #
    #     canvas = Canvas(des)
    #
    #     flight_no_l = Label(des, text="Flight no.", font='Verdana 11 bold')
    #     flight_no_l.place(x=20, y=250)
    #     # canvas.create_line(100, 240, 100, 650, width=2)
    #
    #     from_country_l = Label(des, text="From", font='Verdana 11 bold')
    #     from_country_l.place(x=120, y=250)
    #     # canvas.create_line(200, 240, 200, 650, width=1)
    #
    #     to_country_l = Label(des, text="Destination", font='Verdana 11 bold')
    #     to_country_l.place(x=250, y=250)
    #     # canvas.create_line(300, 240, 300, 650, width=1)
    #
    #     date_l = Label(des, text="Date", font='Verdana 11 bold')
    #     date_l.place(x=370, y=250)
    #     # canvas.create_line(400, 240, 400, 750, width=1)
    #
    #     departure_time_l = Label(des, text="Departure Time", font='Verdana 11 bold')
    #     departure_time_l.place(x=500, y=250)
    #     # canvas.create_line(500, 240, 500, 750, width=1)
    #
    #     arrival_time_l = Label(des, text="Arrival Time", font='Verdana 11 bold')
    #     arrival_time_l.place(x=650, y=250)
    #     # canvas.create_line(600, 240, 600, 750, width=1)
    #
    #     availability_l = Label(des, text="Availability", font='Verdana 11 bold')
    #     availability_l.place(x=780, y=250)
    #     # canvas.create_line(700, 240, 700, 850, width=1)
    #
    #     fare_l = Label(des, text="Fare", font='Verdana 11 bold')
    #     fare_l.place(x=900, y=250)
    #
    #     # canvas.create_rectangle(0, 280, 800, 282, fill="black")
    #     # canvas.pack()
    #
    #
    #     i = len(data)
    #     j = 0
    #
    #     if i==0:
    #         messagebox.showinfo(" ", "No flight Available", parent=win)
    #         close()
    #         dashboard(user)
    #
    #     while i:
    #         details = data[j]
    #         j += 1
    #
    #         temp = details['utc_departure']
    #         dpt = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)
    #         temp = details['utc_arrival']
    #         arv = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)
    #
    #         flight_no_l = Label(des, text=f"{details['flight_no']}", font='Verdana 10 bold')
    #         flight_no_l.place(x=20, y=Y_AXIS)
    #         # canvas.create_line(100, 240, 100, 650, width=2)
    #
    #         from_country_l = Label(des, text=f"{details['from']['city']}", font='Verdana 10 normal')
    #         from_country_l.place(x=120, y=Y_AXIS)
    #         # canvas.create_line(200, 240, 200, 650, width=1)
    #
    #         to_country_l = Label(des, text=f"{details['to']['city']}", font='Verdana 10 normal')
    #         to_country_l.place(x=250, y=Y_AXIS)
    #         # canvas.create_line(300, 240, 300, 650, width=1)
    #
    #         date_l = Label(des, text=f"{dpt.strftime('%d-%m-%Y')}", font='Verdana 10 normal')
    #         date_l.place(x=370, y=Y_AXIS)
    #         # canvas.create_line(400, 240, 400, 750, width=1)
    #
    #         departure_time_l = Label(des, text=f"{dpt.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
    #         departure_time_l.place(x=500, y=Y_AXIS)
    #         # canvas.create_line(500, 240, 500, 750, width=1)
    #
    #         arrival_time_l = Label(des, text=f"{arv.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
    #         arrival_time_l.place(x=650, y=Y_AXIS)
    #         # canvas.create_line(600, 240, 600, 750, width=1)
    #
    #         availability_l = Label(des, text=f"{details['availability']}", font='Verdana 10 normal')
    #         availability_l.place(x=780, y=Y_AXIS)
    #         # canvas.create_line(700, 240, 700, 850, width=1)
    #
    #         fare_l = Label(des, text=f"{details['price']}", font='Verdana 10 normal')
    #         fare_l.place(x=900, y=Y_AXIS)
    #
    #         i -= 1


    def details():
        flight = flight_searcher.FlightSearch()
        flight_data = flight.get_flight_details(from_country.get(), from_city.get(), to_country.get(), to_city.get(),
                                                from_date.get(), to_date.get())
        # print(flight_data)
        display_flights(flight_data, user)


    def clear():
        from_country.delete(0, END)
        to_country.delete(0, END)
        from_city.delete(0, END)
        to_city.delete(0, END)
        from_date.delete(0, END)
        to_date.delete(0, END)
        ticket_type.delete(0, END)
        return_date_to.delete(0, END)
        return_date_from.delete(0, END)

    des = Tk()
    des.title("Flight Manager")
    des.maxsize(width=1100, height=500)
    des.minsize(width=1100, height=500)


    img = ImageTk.PhotoImage(Image.open("images/bg6.jpg"))

    # Add image to the Canvas Items
    canvas = Canvas(des, width=900, height=400)
    canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.pack()

    # heading label
    heading = Label(des, text=f"FLIGHT SEARCH", font='Verdana 22 bold')
    heading.place(x=400, y=40)

    from_country = StringVar()
    from_city = StringVar()
    to_country = StringVar()
    to_city = StringVar()
    from_date = StringVar()
    to_date = StringVar()
    ticket_type = StringVar()
    return_date_to = StringVar()
    return_date_from = StringVar()

    from_country_l = Label(des, text="From Country", font='Verdana 10 bold')
    from_country_l.place(x=80, y=150)
    from_country_f = Entry(des, width=20, textvariable=from_country)
    from_country_f.place(x=190, y=150)

    from_city_l = Label(des, text="From City", font='Verdana 10 bold')
    from_city_l.place(x=80, y=220)
    from_city_f = Entry(des, width=20, textvariable=from_city)
    from_city_f.place(x=190, y=220)

    to_country_l = Label(des, text="To Country", font='Verdana 10 bold')
    to_country_l.place(x=430, y=150)
    to_country_f = Entry(des, width=20, textvariable=to_country)
    to_country_f.place(x=520, y=150)

    to_city_l = Label(des, text="To City", font='Verdana 10 bold')
    to_city_l.place(x=430, y=220)
    to_city_f = Entry(des, width=20, textvariable=to_city)
    to_city_f.place(x=520, y=220)

    from_date_l = Label(des, text="From Date", font='Verdana 10 bold')
    from_date_l.place(x=80, y=290)
    from_date_f = Entry(des, width=20, textvariable=from_date)
    from_date_f.place(x=190, y=290)

    to_date_l = Label(des, text="To Date", font='Verdana 10 bold')
    to_date_l.place(x=430, y=290)
    to_date_f = Entry(des, width=20, textvariable=to_date)
    to_date_f.place(x=520, y=290)

    return_l = Label(des, text="Ticket Type", font='Verdana 10 bold')
    return_l.place(x=760, y=150)
    return_f = Entry(des, width=20, textvariable=ticket_type)
    return_f.place(x=900, y=150)

    to_date_l = Label(des, text="Return Date from", font='Verdana 10 bold')
    to_date_l.place(x=760, y=220)
    to_date_f = Entry(des, width=20, textvariable=return_date_from)
    to_date_f.place(x=900, y=220)

    r_date_l = Label(des, text="Return Date to", font='Verdana 10 bold')
    r_date_l.place(x=760, y=290)
    r_date_f = Entry(des, width=20, textvariable=return_date_to)
    r_date_f.place(x=900, y=290)


    btn = Button(des, text="Search", font='Verdana 10 bold', width=60, command=details, relief="groove")
    btn.place(x=20, y=370)

    btn_login = Button(des, text="Clear", font='Verdana 10 bold', width=58, command=clear, relief="groove")
    btn_login.place(x=552, y=370)


# ------------------------------------------------- End Deshboard Panel --------------------------------------------
# ------------------------------------------------- Signup Window --------------------------------------------------

def signup():
    def action():
        if first_name.get() == "" or last_name.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                exist = False
                # with open("customers.json", "r") as fl:
                #     data = json.load(fl)
                #     if data[user_name.get()]["username"] == user_name.get():
                #         exist = True
                if exist:
                    messagebox.showerror("Error", "User Name Already Exits", parent=winsignup)
                else:
                    format = {
                        "fname": first_name.get(),
                        "lname": last_name.get(),
                        "username": user_name.get(),
                        "password": password.get()
                    }

                    with open("customers.json", "r") as outfile:
                        file_data = json.load(outfile)

                    with open("customers.json", "w") as outfile:
                        file_data["customers"].append(format)
                        json.dump(file_data, outfile, indent=4)
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=winsignup)
                    clear()
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        first_name.delete(0, END)
        last_name.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window

    winsignup = Tk()
    winsignup.title("Flight Manager")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    # heading label
    heading = Label(winsignup, text="Signup", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label
    first_name = Label(winsignup, text="First Name :", font='Verdana 10 bold')
    first_name.place(x=80, y=130)

    last_name = Label(winsignup, text="Last Name :", font='Verdana 10 bold')
    last_name.place(x=80, y=160)

    user_name = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name.place(x=80, y=190)

    password = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password.place(x=80, y=220)

    very_pass = Label(winsignup, text="Verify Password:", font='Verdana 10 bold')
    very_pass.place(x=80, y=250)

    # --------------------------------------------- Entry Box -----------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=40, textvariable=first_name)
    first_name.place(x=200, y=133)

    last_name = Entry(winsignup, width=40, textvariable=last_name)
    last_name.place(x=200, y=163)

    user_name = Entry(winsignup, width=40, textvariable=user_name)
    user_name.place(x=200, y=193)

    password = Entry(winsignup, width=40, textvariable=password)
    password.place(x=200, y=223)

    very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
    very_pass.place(x=200, y=253)

    # button login and clear

    btn_signup = Button(winsignup, text="Signup", font='Verdana 10 bold', command=action)
    btn_signup.place(x=200, y=313)

    btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear)
    btn_login.place(x=280, y=313)


    sign_up_btn = Button(winsignup, text="Switch To Login", command=switch)
    sign_up_btn.place(x=350, y=20)

    winsignup.mainloop()


# ----------------------------------------------------------- End Singup Window ------------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("Flight Manager")

# window size
win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

# heading label
heading = Label(win, text="Login", font='Verdana 25 bold')
heading.place(x=200, y=150)

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

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login, foreground="green",
                   activebackground="green", activeforeground="white", relief="groove")
btn_login.place(x=200, y=293)

btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear, foreground="red",
                   activebackground="red", activeforeground="white", relief="groove")
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win, text="Switch To Sign up", command=signup, foreground="black",
                     activebackground="green", activeforeground="white", relief="groove")
sign_up_btn.place(x=350, y=20)

win.mainloop()
