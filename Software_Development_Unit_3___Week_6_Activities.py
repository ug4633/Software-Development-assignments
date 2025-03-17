import tkinter as tk

#Task 1b

def submit_data():
    responsee1 = v.get()
    responsee2 = w.get()
    responsee3 = question3.get()
    print(f"Opinion 1: {responsee1}")
    print(f"Opinion 2: {responsee2}")
    print(f"Opinion 3: {responsee3}")

#Making the window
root = tk.Tk()
root.title("Government Public Voice Survey")

#labels
title = tk.Label(root, text = "Citizen Voice Survey", bg = "orangered", bd = 10).grid(row = 0)


#buttons
response1 = tk.Label(root, text = "Public opinion on the satisfaction rating for the state government").grid(row = 3)
v = tk.IntVar()
tk.Radiobutton(title,text = "Very dissatisfied",variable = v, value = 5).grid(row = 1, column = 1, sticky = 's')
tk.Radiobutton(title,text = "Dissatisfied",variable = v, value = 4).grid(row = 2, column = 1, sticky = 's')
tk.Radiobutton(title,text = "OK",variable = v, value = 3).grid(row = 3, column = 1, sticky = 's')
tk.Radiobutton(title,text = "Satisfied",variable = v, value = 2).grid(row = 4, column = 1, sticky = 's')
tk.Radiobutton(title,text = "Very satisfied",variable = v, value = 1).grid(row = 5, column = 1, sticky = 's')

tk.Label(title).grid(row = 6)

w = tk.IntVar()
tk.Label(root, text = "Public opinion on who would make the best premier out of the current Premier and the Opposition Party Leader").grid(row = 8)
tk.Radiobutton(title,text = "Current Premier",variable = w, value = 5).grid(row = 8, column = 1, sticky = 'w')
tk.Radiobutton(title,text = "Opposition Partly Leader",variable = w, value = 4).grid(row = 9, column = 1, sticky = 'w')

tk.Label(title).grid(row = 10)

x = tk.IntVar()
response3 = tk.Label(root, text = "Public opinion on how long a state government should serve before the next election").grid(row = 11)
question3 = tk.Entry(title)
question3.grid(row = 11, column = 1)

submit_button = tk.Button(root, text="Submit", command=submit_data).grid(row = 12, column = 1)


tk.Label(text = "ALL RESPONSES WILL BE USED FOR GOVERNMENT PURPOSES AND DECISIONS, AND WILL NOT BE DISCLOSED TO THE PUBLIC, ALL RESPONES ARE ANONYMOUS", bg = 'orangered').grid(row = 12)


root.mainloop()