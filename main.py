
from tkinter import *   # importing everything in the tkinter module
from tkinter import messagebox   # import the messagebox from the tkinter module


root = Tk()     # create window
root.title("Aauthentification")     # naming the window
root.geometry("600x600")     # setting the height and width of the window
root.config(bg="grey")      # altering the window background-color

input_label = Label(root, text="Please enter login details", bg="grey")
input_label.place(x=200, y=0)

input_label1 = Label(root, text="Username", bg="grey")    # create input_label Label widget
input_label1.place(x=250, y=70)     # position the input_label Label widget
user_entry = Entry(root)      # create user_input Entry widget
user_entry.place(x=200, y=100)     # positioning user_input Entry widget

input_label2 = Label(root, text="Password", bg="grey")    # create input_label2 Label widget
input_label2.place(x=250, y=170)      # positioning the input_label Label widget
pass_entry = Entry(root, show="*")      # create pass_entry Entry widget
pass_entry.place(x=200, y=200)      # positioning the pass_entry Entry widget


def check():
    username = ["Likho", "Axolisile", "Phindile", "Aphiwe"]
    passwords = ["2001", "1998", "2002", "2000"]
    found = False
    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == passwords[x1]:
            found = True
    if found == True:
        messagebox.showinfo("STATUS", "Access granted")
        root.destroy()
        import nextpage
    else:
        messagebox.showinfo("ERROR INFO", "Access denied")


# defining function to delete the entry inputs

def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


# define function responsible for exiting the window

def exit_program():
    root.destroy()


log_btn = Button(root, text="Login", borderwidth="2", bg="red", font=("Consolas 15 bold"), command=check)
log_btn.place(x=125, y=300)
clear_btn = Button(root, text="Clear", borderwidth="2", bg="red", font=("Consolas 15 bold"), command=clear)
clear_btn.place(x=250, y=300)
exit_btn = Button(root, text="Exit", borderwidth="2", bg="red", font=("Consolas 15 bold"), command=exit_program)
exit_btn.place(x=375, y=300)


# start the app
root.mainloop()
