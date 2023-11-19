from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(window)
logo_image = PhotoImage(file="logo.png")
image = canvas.create_image(150, 150, image=logo_image)
canvas.pack()

window.mainloop()
