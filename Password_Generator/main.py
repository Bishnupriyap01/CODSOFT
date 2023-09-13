from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    complexity = complexity_var.get()
    if len(length_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Enter length first!")

    else:
        length = int(length_entry.get())

        if complexity == "low":
            include_digits = False
            include_special_chars = False
        elif complexity == "medium":
            include_digits = True
            include_special_chars = False
        else:
            include_digits = True
            include_special_chars = True

        characters = string.ascii_letters
        if include_digits:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.insert(0, new_password)
        pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    length = length_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(length) == 0 or len(password) == 0:
        messagebox.showinfo(title="something went wrong", message="You can't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="password_check!", message=f"DETAILS ENTERED:\n Email:{email}"
                                                                        f"\n Password: {password} \n Want to save it ?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{email} | {password}\n")
                length_entry.delete(0, END)
                password_entry.delete(0, END)


# _______________________________RESET________________________________#
def reset():
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    length_entry.delete(0, END)


# --------------------------DISPLAY SAVED USERID AND PASSWORDS---------#
def show():
    saved_passwords_window = Toplevel(window)
    saved_passwords_file = SavedPasswordsFile(saved_passwords_window)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=300)
logo_img = PhotoImage(file="img.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
email_label = Label(text="Email/Username:")
email_label.grid(row=1, column=0)
length_label = Label(text="Length of password:")
length_label.grid(row=2, column=0)
password_label = Label(text="Your Password:")
password_label.grid(row=4, column=0, sticky="EW")

# Entries
email_entry = Entry(width=38)
email_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "abc@gmail.com")
length_entry = Entry(width=38)
length_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
length_entry.focus()
password_entry = Entry(width=21)
password_entry.grid(row=4, column=1, columnspan=2, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", width=20, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Save", width=10, command=save)
add_button.grid(row=5, column=0, columnspan=1, sticky="EW")
reset_button = Button(text="Reset", width=10, command=reset)
reset_button.grid(row=5, column=1, columnspan=1, sticky="EW")
show_button = Button(text="Display file", width=10, command=show)
show_button.grid(row=5, column=2, columnspan=1, sticky="EW")

# complexity
complexity_label = Label(text="Choose Complexity:", pady=10)
complexity_label.grid(row=3, column=0, sticky="EW")
complexity_var = StringVar(value="medium")
complexity_radio_frame = ttk.Frame(window)
complexity_radio_frame.grid(row=3, column=1, sticky="EW")
complexity_radios = [
    ("Low", "low"),
    ("Medium", "medium"),
    ("High", "high")
]
for text, value in complexity_radios:
    radio = ttk.Radiobutton(complexity_radio_frame, text=text, variable=complexity_var, value=value)
    radio.pack(anchor="w", side=LEFT)


# saved password's file
class SavedPasswordsFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Saved Passwords")

        self.text = Text(root, wrap="none")
        self.text.pack(fill="both", expand=True)

        with open("data.txt", "r") as file:
            self.text.insert("1.0", file.read())


window.mainloop()
