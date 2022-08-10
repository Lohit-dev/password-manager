from cmath import log
from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor  # import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    with open("saved_passwords.txt", "a") as file:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()


        messagebox.showinfo(message="Are you sure?")

        file.write(website + " " + email + " " + password + "\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()  # initialize screen
screen.title("My Password Manager")
screen.config(padx=20, pady=20)

# Canvas setup
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string="Lohitsharma92@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

screen.mainloop()  # loop the screen
