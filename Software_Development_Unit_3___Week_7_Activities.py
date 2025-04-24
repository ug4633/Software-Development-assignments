import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

temp = 0

def confirmB():
    given_name = gName_var.get()
    family_name = fName_var.get()
    email = emailAdd_var.get()
    email_type = emailAddType_var.get()
    birthday = DoB_var.get()
    
    personal_info = []
    personal_info = [given_name, family_name, email, email_type, birthday]
    for i in personal_info:
        if i == '':
            tk.messagebox.showwarning("Error", "Please fill out boxes before proceeding")
            return False
            break
    if personal_info[4] == 'DD/MM/YYYY':
        tk.messagebox.showwarning("Error", "Please fill out boxes before proceeding")
        return False
    
    with open('personal_information.txt', 'a') as file_handle:
        for i in personal_info:
            file_handle.write(i + ', ')
        file_handle.write('\n\n')
        file_handle.close()

    tk.messagebox.showinfo("Completed", "Information successfully saved")
    print(personal_info)

def displayI():
    with open('personal_information.txt', 'r') as file_handle:
        file_contents = [line.strip() for line in file_handle if line.strip()]
    for line in file_contents:
        print(line + '\n')


main = tk.Tk()

gName  = tk.Label(main, text = 'Given name: ').grid(row = 0, column = 0)
gName_var = tk.StringVar()
gNameV = tk.Entry(main, textvariable = gName_var).grid(row = 0, column = 1)

fName  = tk.Label(main, text = 'Family name: ').grid(row = 1, column = 0)
fName_var = tk.StringVar()
fNameV = tk.Entry(main, textvariable = fName_var).grid(row = 1, column = 1)

emailAdd = tk.Label(main, text = 'Email address: ').grid(row = 2, column = 0)
emailAdd_var = tk.StringVar()
emailAddV = tk.Entry(main, textvariable = emailAdd_var).grid(row = 2, column = 1)

emailAddType = ttk.Label(main, text = 'Email Type: ').grid(row = 3, column =0)
emailAddType_var = tk.StringVar()
emailAddTypeV = ttk.Combobox(main, textvariable = emailAddType_var)
emailAddTypeV['values'] = ('Personal', 'School', 'Business')
emailAddTypeV.grid(row = 3, column = 1)
emailAddTypeV.current(0)

DoB = tk.Label(main, text = 'Date of birth: ').grid(row = 4, column = 0)
DoB_var = tk.StringVar()
DoBV = tk.Entry(main, textvariable = DoB_var)
DoBV.insert(0, 'DD/MM/YYYY')
DoBV.grid(row = 4, column = 1)

confirm = tk.Button(main, text = 'Enter', command = confirmB).grid(row = 5,column = 1)


display_info = tk.Button(main, text = 'Display information', command = displayI).grid(row = 6, column = 1)



main.mainloop()