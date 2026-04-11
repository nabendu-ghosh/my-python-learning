from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = ""

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # data_file_path = "intermediate\password_manager\data.txt"
    data_json = "intermediate\password_manager\data.json"
    save_entry = False
    new_data = {
        website_entry.get():{
            "Email": email_entry.get(),
            "Password": password_entry.get()
        }
    }

    if len(password_entry.get()) > 0 and len(website_entry.get()) > 0:
        save_entry = messagebox.askokcancel(title=website_entry.get(), 
                                            message=f"Email: {email_entry.get()} \n"
                                            f"Password: {password_entry.get()} \nSave Details?")
    else:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty!!")

    if save_entry:
        # with open(file=data_file_path, mode="a") as data:
        #     data.write(f"{website_entry.get()} || {email_entry.get()} || {password_entry.get()} \n")
        try:
            with open(file=data_json, mode="r") as data_file:
                loaded_data=json.load(data_file)
        except json.JSONDecodeError:
            loaded_data = new_data
        else:
            loaded_data.update(new_data)
        finally:
            with open(file=data_json, mode="w") as data:
                json.dump(loaded_data,data,indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------------GET PASSWORD ---------------------------- #

def get_password():
    data_json = "intermediate\password_manager\data.json"
    with open(file=data_json, mode="r") as data_file:
        data = json.load(data_file)
    
    try:
        data[website_entry.get()]
    except KeyError:
        messagebox.showinfo(title="Oops", message="No Data Found")
    else:
        messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]["Email"]}\n"
                            f"Password: {data[website_entry.get()]["Password"]}")
        print(data[website_entry.get()])

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="intermediate\password_manager\logo.png")
canvas = Canvas(width=200,height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1,sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="EW")
email_entry.insert(0, "abc@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry = Entry(width=17)
password_entry.grid(row=3,column=1,sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2,sticky="EW")

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1,columnspan=2,sticky="EW")

search_button = Button(text="Search",fg="#3852B4",command=get_password)
search_button.grid(row=1,column=2,sticky="EW")

window.mainloop()