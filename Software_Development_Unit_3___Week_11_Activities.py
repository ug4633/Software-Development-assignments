from multiprocessing import Value
from queue import Empty
from re import L
import tkinter as tk
import re
from tkinter import Variable, messagebox

import datetime
from dateutil.relativedelta import relativedelta

main = tk.Tk()

window = tk.Frame(main)
window.pack(padx = 10, pady = 10, fill = 'y', expand = True)

#(I didnt make this email checker)
def validate_email_syntax(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def click():
    
    #email checks
    email = []

    email.append(email_nameV.get() + "@")
    email.append(email_typeV.get() + ".")
    email.append(email_domainV.get())

    if not (email_nameV.get() and email_typeV.get() and email_domainV.get()):
        messagebox.showwarning("Warning!", "Cannot have empty email")
        return


    emailDisplay = ("".join(email))
    if not validate_email_syntax(emailDisplay):
        messagebox.showwarning("Warning!", "Invalid email!")
        return


    #password check
    password1 = password.get()
    password2 = passwordCheck.get()

    if not (password1 and password2):
        messagebox.showwarning("Warning!", "Cannot have empty password")
        return

    else:
        if password1 != password2:
            messagebox.showwarning("Warning!", "The passwords doesn't match!")
            return

    passwordDisplay = password1
            
    #dob check
    if dobDate_data.get() and dobMonth_data.get() and dobYear_data.get():
        date = int(dobDate_data.get())
        month = int(dobMonth_data.get())
        year = int(dobYear_data.get())

        bday = []
        bday.append(str(year) + '/' + str(month) + '/' + str(date))

        birthday = datetime.datetime(year, month, date)
        current = datetime.datetime.now()
        check120 = datetime.datetime.now() - relativedelta(years = 120)

        birthdayDisplay = str(bday)

        if birthday >= current:
            messagebox.showwarning("Warning!", "Invalid birthday! (Must be in the past)")
            return
        elif birthday <= check120:
            messagebox.showwarning("Warning!", "Invalid birthday! (Must be within 120 years)")
            return
        else:
            messagebox.showinfo("Success", f"Email: {emailDisplay}\nPassword: {passwordDisplay}\nBirthday: {birthdayDisplay}")

    else:
        messagebox.showwarning("Warning!", "Cannot have empty date!")
        return








#Email frame
emailFrame = tk.LabelFrame(window, height = 200,  width = 200, text = 'Email', padx =20, pady = 20)

email_nameV = tk.StringVar()
email_typeV = tk.StringVar()
email_domainV = tk.StringVar()

email_name = tk.Entry(emailFrame, textvariable = email_nameV).grid(row = 0, column = 0)
email_at = tk.Label(emailFrame, text = "@").grid(row = 0, column = 1)
email_type = tk.Entry(emailFrame, width = 10, textvariable = email_typeV).grid(row = 0, column = 2)
seperator = tk.Label(emailFrame, text = '.').grid(row = 0, column = 3)
email_domain = tk.Entry(emailFrame, width = 5, textvariable = email_domainV).grid(row = 0, column = 4)




emailFrame.grid(row = 0, sticky = 'w')


#Password frame

password = tk.StringVar()

passwordFrame = tk.LabelFrame(window, text = 'Password', padx = 10, pady = 10)
 
passwordWindow = tk.Entry(passwordFrame, show = '*', textvariable = password).grid(row = 2, column = 0) 
 
passwordFrame.grid(row = 2, sticky = 'w')





#re-enter password frame

passwordCheck = tk.StringVar()

RpasswordFrame = tk.LabelFrame(window, text = 'Reenter Password', padx = 10, pady = 10)
 
RpasswordWindow = tk.Entry(RpasswordFrame, show = '*', textvariable=passwordCheck).grid(row = 3, column = 0) 
 
RpasswordFrame.grid(row = 3, sticky = 'w')



#Date of birth frame
dob = tk.LabelFrame(window, text = 'Date of birth (DD/MM/YYYY)', padx =10, pady = 10)

dobDate_data = tk.StringVar()
dobMonth_data = tk.StringVar()
dobYear_data = tk.StringVar()



dobDate = tk.Entry(dob, width = 4, textvariable = dobDate_data).grid(row = 4, column = 0)
seperator = tk.Label(dob, text = '/').grid(row = 4, column = 1)
dobMonth = tk.Entry(dob, width = 4, textvariable = dobMonth_data).grid(row = 4, column = 2)
seperator = tk.Label(dob, text = '/').grid(row = 4, column = 3)
dobYear = tk.Entry(dob, width = 8, textvariable = dobYear_data).grid(row = 4, column = 4)

dob.grid(row = 4, sticky = 'w')



#confirm button
confirm = tk.Button(window, text = "Confirm", command = click).grid(row = 4, column = 5)
                   
main.mainloop()
