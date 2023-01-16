from tkinter import *
window = Tk()
window.title("app")
window.geometry("1299x820")
img = PhotoImage(
    file='C:/Users/karth/OneDrive/Documents/code coffee/Python/GDSC/project/1200px-Emblem_of_India_(Government_Gazette).svg (2).png')
lable = Label(window, image=img)
lable.place(x=0, y=0)


def show_page1():
    page2.pack_forget()
    page3.pack_forget()

    page1.pack()


def show_page2():
    page1.pack_forget()
    page3.pack_forget()
    page2.pack()


def show_page3():
    page1.pack_forget()
    page2.pack_forget()
    page3.pack()


page1 = Frame()
page2 = Frame()
page3 = Frame()

login_button = Button(page1, text='log in', font=(
    'Courier', 20, 'bold'), command=show_page2, border=10)
login_button.grid(row=1, column=0)
signup_button = Button(page1, text='Sign up', font=(
    'Courier', 20, 'bold'), command=page2, border=10)
signup_button.grid(row=2, column=0)
# ====================================================================================
a = Label(page2, text="which type of waste you would like to recycle? ", font=(
    'Courier', 20, 'bold'))
a.grid(row=0, column=1)
waste_paper = Button(page2, text="paper", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3, )
waste_paper.grid(row=1, column=1)
card_board = Button(page2, text="card_board", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
card_board.grid(row=1, column=2)
plastic = Button(page2, text="plastic", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
plastic.grid(row=1, column=3)
metal = Button(page2, text="metal", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
metal.grid(row=2, column=1)
WEEE = Button(page2, text="   WEEE   ", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
WEEE.grid(row=2, column=2)
wood = Button(page2, text=" wood  ", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
wood.grid(row=2, column=3)
glass = Button(page2, text='glass', font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
glass.grid(row=3, column=1)
clothing_textile = Button(page2, text=' clothing ', font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
clothing_textile.grid(row=3, column=2)
others = Button(page2, text="others ", font=(
    'Courier', 35, 'bold'), border=10, command=show_page3)
others.grid(row=3, column=3)
# =========================================================================================
address_label = Label(
    page3, text="Fill the essentials :", font=('Courier', 35, 'bold'))
address_label.grid(row=0, column=0)
address_label = Label(
    page3, text="address :", font=('Courier', 35, 'bold'))
address_label.grid(row=1, column=2)
b_entry = Entry(page3, width=20, font=('Courier', 35, 'bold'))
b_entry.grid(row=2, column=2)
phone_label = Label(page3, text="your phone no. :",
                    font=('Courier', 35, 'bold'))
phone_label.grid(row=3, column=2)
b_entry = Entry(page3, width=20, font=('Courier', 35, 'bold'))
b_entry.grid(row=4, column=2)
timeslot_label = Label(
    page3, text='pick you preffered time slot :', font=('Courier', 35, 'bold'))
timeslot_label.grid(row=5, column=0)
morning = Radiobutton(page3, text="8:00 AM -11:00 AM",
                      font=('Courier', 35, 'bold'))
morning.grid(row=6, column=2)
afternoon = Radiobutton(page3, text="11:00 AM -4:00 PM",
                        font=('Courier', 35, 'bold'))
afternoon.grid(row=7, column=2)
night = Radiobutton(page3, text="4:00 PM -11:00 PM",
                    font=('Courier', 35, 'bold'))
night.grid(row=8, column=2)
finish_button = Button(page3, text="Submit", font=('Courier', 35, 'bold'))
finish_button.grid(row=9, column=0)
# ==================================================================================

show_page1()


window.mainloop()
