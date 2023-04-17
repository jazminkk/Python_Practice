import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

NAVY = "#2B3467"
WHITE = "#FCFFE7"
FONT = ("Courier", 14, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pwd():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)
    pwd = "".join(password_list)
    password.delete(0, 'end')
    password.insert(0, pwd)
    pyperclip.copy(pwd)
    tkinter.messagebox.showinfo(title="Copy Password", message="Password will in the clipboard.")


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_pwd():
    web_data = website.get()
    if web_data == "":
        messagebox.showinfo(title="Empty Entry", message="The website field is empty!")
    else:
        try:
            with open("./pwd.json", 'r') as f:
                all_data = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo(title="No File", message="No data file found!")
        else:
            if web_data in all_data:
                match_data = all_data[web_data]
                msg = f"Website: {web_data}\nEmail: {match_data['email']}\nPassword: {match_data['password']}"
                messagebox.showinfo(title="Details", message=msg)
                username.delete(0, 'end')
                username.insert(0, match_data["email"])
                password.delete(0, 'end')
                password.insert(0, match_data["password"])
            else:
                messagebox.showinfo(title="No Record", message="No details for the website exists!")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    web_data = website.get()
    name_data = username.get()
    pwd_data = password.get()

    if web_data == "" or name_data == "" or pwd_data == "":
        messagebox.askokcancel(title="Empty Entry", message="Please don't leave any fields empty!")
    else:
        check_msg = f"There are the details entered:\n" \
              f"Website: {web_data}\n" \
              f"Email: {name_data}\n" \
              f"Password: {pwd_data}\n" \
              f"Is it ok to save?"
        is_ok = messagebox.askokcancel(title="Check Info", message=check_msg)
        if is_ok:
            new_data = {web_data: {
                "email": name_data,
                "password": pwd_data,
            }}
            try:
                with open("./pwd.json", 'r') as f:
                    all_data = json.load(f)
            except FileNotFoundError:
                with open("./pwd.json", 'w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                all_data.update(new_data)
                with open("./pwd.json", 'w') as f:
                    json.dump(all_data, f, indent=4)
            finally:
                website.delete(0, 'end')
                password.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=WHITE)

# Logo
mylogo = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=mylogo)
canvas.grid(column=1, row=0)

# Titles And Entries
website_label = tkinter.Label(text="Website:", font=FONT, fg=NAVY, bg=WHITE, highlightthickness=0)
website_label.grid(column=0, row=1)

website = tkinter.Entry(width=21, bg=WHITE, highlightthickness=0)
website.grid(column=1, row=1)
website.focus()

username_label = tkinter.Label(text="Email/Username:", font=FONT, fg=NAVY, bg=WHITE, highlightthickness=0)
username_label.grid(column=0, row=2)

username = tkinter.Entry(width=40, bg=WHITE, highlightthickness=0)
username.grid(column=1, row=2, columnspan=2)
username.insert(0, "y70932@gmail.com")

password_label = tkinter.Label(text="Password:", font=FONT, fg=NAVY, bg=WHITE, highlightthickness=0)
password_label.grid(column=0, row=3)

password = tkinter.Entry(width=21, bg=WHITE, highlightthickness=0)
password.grid(column=1, row=3)

# Buttons
find_pwd_btn = tkinter.Button(text="Search", width=17, command=find_pwd, font=FONT, bg='black', highlightthickness=0)
find_pwd_btn.grid(column=2, row=1)

generate_pwd_btn = tkinter.Button(text="Generate Password", width=17, command=generate_pwd, font=FONT, bg='black', highlightthickness=0)
generate_pwd_btn.grid(column=2, row=3)

add_btn = tkinter.Button(text="Add", width=42, command=save_info, font=FONT, bg='black', highlightthickness=0)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()

# <a href="https://www.flaticon.com/free-stickers/seo-and-web" title="seo and web stickers">Seo and web stickers created by vectorsmarket15 - Flaticon</a>