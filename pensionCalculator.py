from tkinter import *
from tkinter import font
import tkinter.messagebox as mbox
from datetime import datetime
from dateutil import relativedelta

def calculations():
    service_in_months = 0

    dob = (datetime.strptime(dobentry.get(), "%d/%m/%Y")).date()
    doj = (datetime.strptime(dojentry.get(), "%d/%m/%Y")).date()
    dor = (datetime.strptime(retentry.get(), "%d/%m/%Y")).date()
    service_in_months = (dor.year - doj.year) * 12 + (dor.month - doj.month)
    print(service_in_months)
    service_in_half_years = 0
    if service_in_months % 6 >= 3:
        service_in_half_years = (service_in_months // 6) + 1
    else:
        service_in_half_years = service_in_months // 6
    print(service_in_half_years)
    basic = int(basicentry.get())
    pension = (basic / 2) * (service_in_half_years / 60)
    print(basic)
    print(int(pension))
    # age = int(dor - dob)
    # nxtbdage = int(age + 1)
    #print(service, age, nxtbdage)
    # display = "no coding done to calculate"
    # mbox.showinfo("  ", display.title())

entryWin = Tk()
label_font = font.Font(size=16)
entryWin.geometry('400x350')
entryWin.title("Entry window")
entryWin.configure(background="light green")
entryWin.minsize(400, 350)
entryWin.maxsize(400, 350)
ewinTitle = Label(entryWin, text="Enter Details", font=("Arial", 16), fg="blue", bg="light green")
ewinTitle.grid(columnspan = 2)
doblabel = Label(entryWin, text="Date of Birth ", font=label_font, fg="blue", bg="light green" )
dobentry = Entry(entryWin)
dojlabel = Label(entryWin, text="Date of Joining ", font=label_font, fg="blue", bg="light green")
dojentry = Entry(entryWin)
retlabel = Label(entryWin, text="Retirement Date ", font=label_font, fg="blue", bg="light green")
retentry = Entry(entryWin)
basiclabel = Label(entryWin, text="Basic pay on retirement ", font=label_font, fg="blue", bg="light green")
basicentry = Entry(entryWin)
dalabel = Label(entryWin, text="DA on retirement", font=label_font, fg="blue", bg="light green")
daentry = Entry(entryWin)
hralabel = Label(entryWin, text="HRA on retirement ", font=label_font, fg="blue", bg="light green")
hraentry = Entry(entryWin)
ccalabel = Label(entryWin, text="CCA on retirement ", font=label_font, fg="blue", bg="light green")
ccaentry = Entry(entryWin)
malabel = Label(entryWin, text="MA on retirement ", font=label_font, fg="blue", bg="light green")
maentry = Entry(entryWin)
doblabel.grid(row=1, column=0, sticky=W)
dobentry.grid(row=1, column=1)
dojlabel.grid(row=2, column=0, sticky=W)
dojentry.grid(row=2, column=1)
retlabel.grid(row=3, column=0, sticky=W)
retentry.grid(row=3, column=1)
basiclabel.grid(row=4, column=0, sticky=W)
basicentry.grid(row=4, column=1)
dalabel.grid(row=5, column=0, sticky=W)
daentry.grid(row=5, column=1)
hralabel.grid(row=6, column=0, sticky=W)
hraentry.grid(row=6, column=1)
ccalabel.grid(row=7, column=0, sticky=W)
ccaentry.grid(row=7, column=1)
malabel.grid(row=8, column=0, sticky=W)
maentry.grid(row=8, column=1, )

calcbutton = Button(entryWin, text="Calculate", font=label_font, fg="blue", bg="red", command=calculations)
calcbutton.grid(columnspan = 2)








entryWin.mainloop()