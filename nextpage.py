from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Authentification")
root.geometry("600x600")
root.config(bg="tan")

# Creating labels
amount = Label(root, text="Please enter amount in account", bg="tan")

# Creating entries
account = Entry(root)


def check():
    try:
        if int(account.get()) >= 3000:
            messagebox.showinfo("Status Feedback", "Congratulations. You qualify to go to Malaysia.")
    except ValueError:
        if account.get() != int:
            messagebox.showinfo("Message", "Insert more funds into account")
    else:
        if int(account.get()) < 3000:
            messagebox.showerror("Message", "Invalid")


def clear_all():
    account.delete(0, END)


def exit_program():
    return root.destroy()


# Creating buttons
check = Button(root, text="Check qualification", command=check, bg="blue")
clear = Button(root, text="Clear", command=clear_all, bg="blue")
exit_btn = Button(root, text="Exit", command=exit_program, bg="blue")


# Placing
amount.place(x=100, y=20)
account.place(x=120, y=80)
check.place(x=120, y=130)
clear.place(x=160, y=190)
exit_btn.place(x=165, y=240)

root.mainloop()
