import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import json
from datetime import datetime, timezone
import flight_searcher

# Create the main application window
class FlightManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Manager")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        self.load_images()
        self.create_login_widgets()
        self.create_signup_widgets()
        
        self.show_login()

    def load_images(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("images/bg6.jpg"))

    def create_login_widgets(self):
        self.login_frame = tk.Frame(self.root)
        
        # Login widgets
        self.login_username_label = tk.Label(self.login_frame, text="User Name:")
        self.login_username_entry = tk.Entry(self.login_frame)
        
        self.login_password_label = tk.Label(self.login_frame, text="Password:")
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_clear_button = tk.Button(self.login_frame, text="Clear", command=self.clear_login)
        self.signup_button = tk.Button(self.login_frame, text="Switch To Sign up", command=self.show_signup)
        
        # Layout login widgets
        self.login_username_label.pack()
        self.login_username_entry.pack()
        self.login_password_label.pack()
        self.login_password_entry.pack()
        self.login_button.pack()
        self.login_clear_button.pack()
        self.signup_button.pack()
        
    def create_signup_widgets(self):
        self.signup_frame = tk.Frame(self.root)
        
        # Signup widgets
        self.signup_firstname_label = tk.Label(self.signup_frame, text="First Name:")
        self.signup_firstname_entry = tk.Entry(self.signup_frame)
        
        self.signup_lastname_label = tk.Label(self.signup_frame, text="Last Name:")
        self.signup_lastname_entry = tk.Entry(self.signup_frame)
        
        self.signup_username_label = tk.Label(self.signup_frame, text="User Name:")
        self.signup_username_entry = tk.Entry(self.signup_frame)
        
        self.signup_password_label = tk.Label(self.signup_frame, text="Password:")
        self.signup_password_entry = tk.Entry(self.signup_frame, show="*")
        
        self.signup_confirm_label = tk.Label(self.signup_frame, text="Confirm Password:")
        self.signup_confirm_entry = tk.Entry(self.signup_frame, show="*")
        
        self.signup_register_button = tk.Button(self.signup_frame, text="Register", command=self.register)
        self.signup_clear_button = tk.Button(self.signup_frame, text="Clear", command=self.clear_signup)
        self.login_button_signup = tk.Button(self.signup_frame, text="Switch To Login", command=self.show_login)
        
        # Layout signup widgets
        self.signup_firstname_label.pack()
        self.signup_firstname_entry.pack()
        self.signup_lastname_label.pack()
        self.signup_lastname_entry.pack()
        self.signup_username_label.pack()
        self.signup_username_entry.pack()
        self.signup_password_label.pack()
        self.signup_password_entry.pack()
        self.signup_confirm_label.pack()
        self.signup_confirm_entry.pack()
        self.signup_register_button.pack()
        self.signup_clear_button.pack()
        self.login_button_signup.pack()
        
        # Hide signup frame initially
        self.signup_frame.pack_forget()

    def show_login(self):
        self.login_frame.pack()
        self.signup_frame.pack_forget()

    def show_signup(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack()

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Enter User Name And Password")
            return

        with open("customers.json", "r") as file:
            data = json.load(file)["customers"]
            for customer in data:
                if customer["username"] == username and customer["password"] == password:
                    messagebox.showinfo("Success", "Successfully Login")
                    self.clear_login()
                    self.show_dashboard(customer)
                    return
        messagebox.showerror("Error", "Invalid User Name Or Password")

    def clear_login(self):
        self.login_username_entry.delete(0, tk.END)
        self.login_password_entry.delete(0, tk.END)

    def show_dashboard(self, user):
        dashboard_window = tk.Toplevel(self.root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("800x600")
        # Create and display flight information in the dashboard window here

    def register(self):
        first_name = self.signup_firstname_entry.get()
        last_name = self.signup_lastname_entry.get()
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        confirm_password = self.signup_confirm_entry.get()

        if not all([first_name, last_name, username, password, confirm_password]):
            messagebox.showerror("Error", "All Fields Are Required")
        elif password != confirm_password:
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same")
        else:
            try:
                with open("customers.json", "r") as file:
                    data = json.load(file)

                for customer in data["customers"]:
                    if customer["username"] == username:
                        messagebox.showerror("Error", "User Name Already Exists")
                        return

                new_customer = {
                    "fname": first_name,
                    "lname": last_name,
                    "username": username,
                    "password": password
                }

                data["customers"].append(new_customer)

                with open("customers.json", "w") as file:
                    json.dump(data, file, indent=4)

                messagebox.showinfo("Success", "Registration Successful")
                self.clear_signup()
                self.show_login()

            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}")

    def clear_signup(self):
        self.signup_firstname_entry.delete(0, tk.END)
        self.signup_lastname_entry.delete(0, tk.END)
        self.signup_username_entry.delete(0, tk.END)
        self.signup_password_entry.delete(0, tk.END)
        self.signup_confirm_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightManagerApp(root)
    root.mainloop()
