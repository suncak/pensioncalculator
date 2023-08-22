from tkinter import *
from tkinter import font
import tkinter.messagebox as mbox
from datetime import datetime

def calculations():
    try:
        dob = (datetime.strptime(dobentry.get(), "%d/%m/%Y")).date()
        doj = (datetime.strptime(dojentry.get(), "%d/%m/%Y")).date()
        dor = (datetime.strptime(retentry.get(), "%d/%m/%Y")).date()
        service_in_months = (dor.year - doj.year) * 12 + (dor.month - doj.month)

        if service_in_months % 6 >= 3:
            service_in_half_years = (service_in_months // 6) + 1
        else:
            service_in_half_years = service_in_months // 6

        basic = int(basicentry.get())
        full_pension = int((basic / 2) * (service_in_half_years / 60))
        one_third_pension = int(full_pension / 3)
        pens_after_commutation = full_pension - one_third_pension
        da = int(daentry.get())
        hra = int(hraentry.get())
        cca = int(ccaentry.get())
        ma = int(maentry.get())
        ret_month = dor.month
        ds_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        pay_per_day = (basic + da + hra + cca + ma)/ds_in_months[ret_month]
        el_encash = int(240 * pay_per_day)

        age = (dor.year - dob.year)
        com_table = {20: 9.188, 21: 9.187, 22: 9.186, 23: 9.185, 24: 9.184, 25: 9.183, 26: 9.182, 27: 9.180, 28: 9.178,
                     29: 9.176, 30: 9.173, 31: 9.169, 32: 9.164, 33: 9.159, 34: 9.152, 35: 9.145, 36: 9.136, 37: 9.126,
                     38: 9.116, 39: 9.103, 40: 9.090, 41: 9.075, 42: 9.059, 43: 9.040, 44: 9.019, 45: 9.996, 46: 8.971,
                     47: 8.943, 48: 8.913, 49: 8.881, 50: 8.846, 51: 8.808, 52: 8.768, 53: 8.724, 54: 8.678, 55: 8.827,
                     56: 8.572, 57: 8.512, 58: 8.446, 59: 8.371, 60: 8.287, 61: 8.194, 62: 8.093, 63: 7.982, 64: 7.862,
                     65: 7.731, 66: 7.591, 67: 7.431, 68: 7.262, 69: 7.083, 70: 6.897, 71: 6.703, 72: 6.502, 73: 40611,
                     74: 6.085, 75: 5.872, 76: 5.657, 77: 5.443, 78: 5.229, 79: 5.018, 80: 4.812, 81: 9.188}

        commutation_amount = int(one_third_pension * 12 * com_table[age + 1])
        results = [full_pension, commutation_amount, pens_after_commutation, el_encash]
        result_window(results)

    except ValueError:
        mbox.showinfo("Error", "Check whether values for basic, DA etc are integer values and date boxes are in dd/mm/yyyy format")


def result_window(results):
    result_window = Toplevel(entryWin)
    result_window.title("Result Window")
    result_window.geometry("400x200")
    result_window.configure(background="light green")

    def delete_rwindow():
        result_window.destroy()

    result_labels = ["Full Pension:", "Commutation Amount:", "Pension after Commutation", "EL Encashment"]
    for idx, result in enumerate(results):
        result_label = Label(result_window, font=("Areal", 16), bg="light green", fg="blue", text=f"{result_labels[idx]} {result}")
        result_label.pack()
    okButton = Button(result_window, text="OK", width=5, height=1, font=label_font, fg="blue", bg="red",command=delete_rwindow)
    okButton.pack()


entryWin = Tk()
label_font = font.Font(size=16)
entryWin.geometry('400x600')
entryWin.title("Entry window")
entryWin.configure(background="light green")
# entryWin.minsize(400, 550)
# entryWin.maxsize(400, 550)
ewinTitle = Label(entryWin, text="Enter Details", font=("Arial", 16), fg="blue", bg="light green")
ewinTitle.grid(columnspan = 2)
doblabel = Label(entryWin, text="Date of Birth ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
dobentry = Entry(entryWin)
dojlabel = Label(entryWin, text="Date of Joining ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
dojentry = Entry(entryWin)
retlabel = Label(entryWin, text="Retirement Date ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
retentry = Entry(entryWin)
basiclabel = Label(entryWin, text="Basic pay on retirement ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
basicentry = Entry(entryWin)
dalabel = Label(entryWin, text="DA on retirement", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
daentry = Entry(entryWin)
hralabel = Label(entryWin, text="HRA on retirement ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
hraentry = Entry(entryWin)
ccalabel = Label(entryWin, text="CCA on retirement ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
ccaentry = Entry(entryWin)
malabel = Label(entryWin, text="MA on retirement ", font=label_font, fg="blue", bg="light green", padx=10, pady=10)
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

def clear():
    dobentry.delete(0, END)
    dojentry.delete(0, END)
    retentry.delete(0, END)
    basicentry.delete(0, END)
    daentry.delete(0, END)
    hraentry.delete(0, END)
    ccaentry.delete(0, END)
    maentry.delete(0, END)

def appexit():
    entryWin.destroy()

calcbutton = Button(entryWin, text="Calculate", font=label_font, fg="white", bg="red", command=calculations)
calcbutton.grid(row=9, column=0, padx=15, pady=0)

clearbutton = Button(entryWin, text="Clear", font=label_font, width=9, fg="white", bg="red", command=clear)
clearbutton.grid(row=9, column=1, padx=15, pady=15)

exitbutton = Button(entryWin, text="Exit", font=label_font, fg="blue", bg="red", command=appexit)
exitbutton.grid(row=11, columnspan=2, padx=15, pady=15)

entryWin.mainloop()