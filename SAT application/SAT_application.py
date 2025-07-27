from asyncio import SelectorEventLoop
from pickle import TRUE
from re import X
import tkinter as tk
import datetime #for the calendar widget
import calendar
from tkinter import BOTH, BOTTOM, StringVar, Tk, messagebox
from tkinter import ttk

#global data used throughout software
user = 'ug4633'
reminders = {datetime.datetime(2026, 9, 15, 23, 00): "Birthday", datetime.datetime(2025, 12, 25): "Christmas"}
current = datetime.datetime.now()
year = int(current.strftime('%Y'))
monthLS = current.strftime('%b')
monthN = int(current.strftime('%m'))
date = int(current.strftime('%d'))
day = current.strftime('%A')
hour = int(current.strftime('%H'))
minute = int(current.strftime('%M'))
inventory = {"Item": ["Small item that is to not be left out in the sun or else it wont melt", False], "Item2": ["Description", True], "Item2": ["Description", True], "Item2": ["Description", True], "Item2": ["Description", True], "Item2": ["Description", True], "Item2": ["Description", True]}

#widget functions
def calendarWidgetDisplay(parent):
    global calendarWidget

    calendarWidget = tk.Label(parent, text = f"{current.strftime('%Y')}\n{current.strftime('%B')} {current.strftime('%d')}\n{current.strftime('%A')}", font = ('Times New Roman', 18), bg = '#8edba2', padx = 10, pady = 10, relief = 'solid', borderwidth=1)
    #print(calendar.month(year, month))

    calendarWidget.pack(fill = tk.BOTH, expand = True)

def weatherWidget(parent): #due to requiring installation of modules for the weather, i dont think it'd be a good submission for the sat, will come back when solution is figured
    pass

#cute cat
def cutecat(parent):
    
    cat = tk.Label(parent, image = test, bg = '#8edba2')
    cat.pack(fill = tk.BOTH, expand = True)

#reminder widget
def reminderLine(parent):
    global monthLS, date, reminders
    for n in reminders:
        detail = reminders[n]
        text = tk.Label(parent, bg = '#cfffdc', text = f'{detail}, {n.strftime('%x')} {n.strftime('%I')}{n.strftime('%p')}', anchor = 'w', relief = 'solid', borderwidth = 1)
        text.pack(fill = tk.BOTH, expand = True, padx =2)

def ReminderWidget(parent):

    global reminders, reminderScreenButtonIcon, reminderScreenButton, reminderWindow

    reminderWindow = tk.LabelFrame(parent, text = 'Upcoming reminders: ', bg = '#68b27b', relief = 'solid', borderwidth=1 ,font = ('Times New Roman', 12))
    reminderWindow.pack(fill = tk.BOTH, expand = True)


    reminderScreenButton = tk.Button(reminderWindow, relief = 'flat', activebackground='#68b27b', command = reminderClick, image = reminderScreenButtonIcon, height = 30, width = 30)
    reminderScreenButton.pack(side = tk.RIGHT, padx =10)
    
    reminderLine(reminderWindow)
    
def reminderClick():
    global reminderPage, reminders, create, seperator, editReminder, reminderAccess
    reminderScreenButton.config(image = reminderScreenButtonIcon)

    homeWelcome.pack_forget()
    bigButtons.pack(fill = tk.BOTH, expand = True, side =tk.BOTTOM)
    seperator.pack_forget()
    
    reminderPage = tk.Frame(app, bg = '#68b27b', height = 500, relief = 'flat')
    reminderPage.pack(fill = tk.X, side = tk.BOTTOM, padx = 20, pady = 30)
    reminderPage.pack_propagate(False)

    text = tk.Label(reminderPage, text = "Reminders: ", font = ('Times New Roman', 18), bg = '#68b27b')
    text.pack(side = tk.TOP, anchor = 'w', pady = 10)

    #the create and edit button
    buttonArea = tk.Frame(reminderPage, height = 60, bg = '#cfffdc')
    buttonArea.pack(side = tk.BOTTOM, fill = tk.X)
    buttonArea.pack_propagate(False)

    create = tk.Button(buttonArea, bg = '#cfffdc', activebackground = '#cfffdc', image = createNewIcon, command = createClick, relief = 'flat', height = 50, width = 101, padx = 5, pady = 5)
    create.pack(side = tk.RIGHT)

    editReminder = tk.Button(buttonArea, bg = '#cfffdc', activebackground = '#cfffdc', image = editIcon, command = editReminderClick, relief = 'flat', height = 50, width = 101, padx = 5, pady = 5)
    editReminder.pack(side = tk.RIGHT)

    #this customizes the scrollbar to match the color
    reminderScroll = ttk.Style()
    reminderScroll.theme_use('classic')
    reminderScroll.configure("Vertical.TScrollbar", background = '#68b27b', arrowcolor = '#cfffdc', troughcolor = '#cfffdc')

    reminderList = ttk.Scrollbar(reminderPage, orient = 'vertical') #, text = 'Reminders: ', font = ('Times New Roman', 20),  height = 550
    reminderList.pack(side = tk.RIGHT, fill = tk.Y)

    reminderAccess = tk.Listbox(reminderPage, yscrollcommand=reminderList.set, width = 375, bg = '#cfffdc', relief = 'flat')
    i = 0
    for n in reminders:
        reminderAccess.insert(i, f'{reminders[n]}, {n.strftime('%x')} {n.strftime('%I')}{n.strftime('%p')}')
        i += 1

    reminderAccess.pack(side = tk.LEFT, fill = tk.BOTH)
    reminderAccess.pack_propagate(False)

    reminderList.config(command = reminderAccess.yview)

def createClick():
    global clickPage, entryYearV, entryMonthV, entryDateV, entryHourV, entryMinuteV, descriptReminder

    create.config(image = createNewIcon)
    reminderPage.pack_forget()
    bigButtons.pack_forget()

    clickPage = tk.Frame(app, bg = '#68b27b', height = 500, relief = 'flat')
    clickPage.pack(fill = tk.X, padx = 20, pady = 30)
    

    entryArea = tk.LabelFrame(clickPage, text = "Date: ", font = ('Times New Roman', 18), bg = '#68b27b', height =250)
    entryArea.pack(pady = 10, fill = tk.BOTH, side = tk.TOP)
    entryArea.pack_propagate(False)

    placeholder = tk.Label(entryArea, text = "      ", bg = '#68b27b', font = ('Times New Roman', 14))
    placeholder.grid(row = 1, column = 0, sticky = 'w', pady = 5, padx  = 5)

    #year row
    entryYearT = tk.Label(entryArea, text = 'Year: ', bg = '#cfffdc', font = ('Times New Roman', 12))
    entryYearT.grid(row = 1, column = 5, sticky = 'e', pady = 5, padx = 5)

    entryYearV = tk.StringVar()
    entryYearE = tk.Entry(entryArea, bg = '#cfffdc', width = 10, textvariable = entryYearV)
    entryYearE.grid(row = 1, column = 6, sticky = 'nesw', pady = 5)

    entryYearT = tk.Label(entryArea, text = f'Example: {year}', bg = '#cfffdc', font = ('Times New Roman', 8))
    entryYearT.grid(row = 1, column = 7, sticky = 'w', pady = 5, padx = 5)
    
    #month row
    entryMonthT = tk.Label(entryArea, text = 'Month: ', bg = '#cfffdc', font = ('Times New Roman', 12))
    entryMonthT.grid(row = 2, column = 5, sticky = 'e', pady = 5, padx = 5)

    entryMonthV = tk.StringVar()
    entryMonthE = tk.Entry(entryArea, bg = '#cfffdc', width = 5, textvariable = entryMonthV)
    entryMonthE.grid(row = 2, column = 6, sticky = 'nesw', pady = 5)

    entryMonthT = tk.Label(entryArea, text = f'Example: {monthN}', bg = '#cfffdc', font = ('Times New Roman', 8))
    entryMonthT.grid(row = 2, column = 7, sticky = 'w', pady = 5, padx = 5)

    #date row
    entryDateT = tk.Label(entryArea, text = 'Date: ', bg = '#cfffdc', font = ('Times New Roman', 12))
    entryDateT.grid(row = 3, column = 5, sticky = 'e', pady = 5, padx = 5)

    entryDateV = tk.StringVar()
    entryDateE = tk.Entry(entryArea, bg = '#cfffdc', width = 5, textvariable = entryDateV)
    entryDateE.grid(row = 3, column = 6, sticky = 'nesw', pady = 5)

    entryDateT = tk.Label(entryArea, text = f'Example: {date}', bg = '#cfffdc', font = ('Times New Roman', 8))
    entryDateT.grid(row = 3, column = 7, sticky = 'w', pady = 5, padx = 5)

    #hour row
    entryHourT = tk.Label(entryArea, text = 'Hour (24): ', bg = '#cfffdc', font = ('Times New Roman', 12))
    entryHourT.grid(row = 4, column = 5, sticky = 'e', pady = 5, padx = 5)

    entryHourV = tk.StringVar()
    entryHourE = tk.Entry(entryArea, bg = '#cfffdc', width = 5, textvariable = entryHourV)
    entryHourE.grid(row = 4, column = 6, sticky = 'nesw', pady = 5)

    entryHourT = tk.Label(entryArea, text = f'Example: {hour}', bg = '#cfffdc', font = ('Times New Roman', 8))
    entryHourT.grid(row = 4, column = 7, sticky = 'w', pady = 5, padx = 5)

    #minute row
    entryHourT = tk.Label(entryArea, text = 'Minute (60): ', bg = '#cfffdc', font = ('Times New Roman', 12))
    entryHourT.grid(row = 5, column = 5, sticky = 'e', pady = 5, padx = 5)

    entryMinuteV = tk.StringVar()
    entryHourE = tk.Entry(entryArea, bg = '#cfffdc', width = 5, textvariable = entryMinuteV)
    entryHourE.grid(row = 5, column = 6, sticky = 'nesw', pady = 5)

    entryHourT = tk.Label(entryArea, text = f'Example: {minute}', bg = '#cfffdc', font = ('Times New Roman', 8))
    entryHourT.grid(row = 5, column = 7, sticky = 'w', pady = 5, padx = 5)

    entryAreaBelow = tk.LabelFrame(clickPage, text = 'Description: ', font = ('Times New Roman', 14), bg = '#68b27b', height =250)
    entryAreaBelow.pack(pady = 10, fill = tk.BOTH, side = tk.TOP)
    entryAreaBelow.pack_propagate(False)

    descriptReminder = tk.Text(entryAreaBelow, bg = '#cfffdc', height = 100, )
    descriptReminder.pack(fill = tk.BOTH, padx = 10, pady = 10, side = tk.TOP)
    descriptReminder.pack_propagate(False)


    confirmButton = tk.Button(clickPage, text = 'Confirm', bg = '#68b27b', height = 1, command = lambda: [cleanAll(), confirmButtonClick(), reminderClick()], activebackground = '#68b27b')
    confirmButton.pack(padx = 10, pady = 5, anchor = 'e', side = tk.RIGHT)
    confirmButton.pack_propagate(False)

    cancelButton = tk.Button(clickPage, text = 'Cancel', bg = '#7f5c47', height = 1, command = lambda: [cleanAll(), reminderClick()], activebackground = '#7f5c47')
    cancelButton.pack(padx = 10, pady = 5, anchor = 'w', side = tk.LEFT)
    cancelButton.pack_propagate(False)

def confirmButtonClick():
    global reminders
    try:
        reminderYear = int(entryYearV.get())
        reminderMonth = int(entryMonthV.get())
        reminderDate = int(entryDateV.get())
        reminderHour = int(entryHourV.get())
        reminderMinute = int(entryMinuteV.get())

    except: 
        messagebox.showwarning("Warning", "The date must be numbers (refer to example)")
        return

    if not (year <= reminderYear <= 9999):
        messagebox.showwarning("Warning", 'Invalid year (year must be 4 digit, and in the current or future)')
        return
    elif not(1 <= reminderMonth <= 12):
        messagebox.showwarning("Warning", "Invalid month, (month must be between 1 ~ 12, refer to the example)")
        return
    elif not (1 <= reminderDate <= 31): #im not goign to check if for example feb 31st exists since codes already long
        messagebox.showwarning("Warning", "Invalid date, (date must be between 1 ~ 31, refer to the example)")
        return
    elif not (1 <= reminderHour <= 23):
        messagebox.showwarning("Warning", "Invalid hour, (hour must be in military time, refer to the example)")
        return
    elif not (0 <= reminderMinute <= 60):
        messagebox.showwarning("Warning", "Invalid minutes, (minutes must be between 0 ~ 60, refer to the example)")
        return

    #reminders = {datetime.datetime(2025, 9, 15, 23, 00): "Birthday", datetime.datetime(2025, 12, 25): "Christmas"}

    description = descriptReminder.get("1.0", tk.END)
    description = description.replace("\n", "")

    #add the new reminder to the dictionary
    reminders[datetime.datetime(reminderYear, reminderMonth, reminderDate, reminderHour, reminderMinute)] = description


    #sort the dictioanry 
    reminders = modifiedInsertionSort(reminders)

def modifiedInsertionSort(array): #dictionaries only
    sortedArray = {}
    while array != {}:
        earliest = next(iter(array))
        for n in array:
            if n < earliest:
                earliest = n
        sortedArray[earliest] = array[earliest]
        del array[earliest]
    array = sortedArray
    return array
            
def editReminderClick():
    editReminder.config(image = editIcon)

    selected = reminderAccess.curselection()

    if selected:
        selected_value = reminderAccess.get(selected)
        reminderName = (selected_value.split(','))[0]

        for date, name in reminders.items():
            if name == reminderName:
                del reminders[date]
                create.config(image = createNewIcon)
                reminderPage.pack_forget()
                bigButtons.pack_forget()
                reminderClick()
                break
    else:
        print("nothing")

    


    


#other functoins

def homeButtonClick():


    try: 
        invBackground.pack_forget()
    except:
        pass

    homeButton.config(image = homeIcon)

    settingDisplay.pack_forget()
    cleanAll()
    
    homeWelcome.pack(fill = tk.X)
    homeWelcome.pack_propagate(False)

    bigButtons.pack(fill = tk.BOTH, expand = True, side =tk.BOTTOM)

    seperator.pack(side =tk.BOTTOM, fill = tk.X)
    seperator.pack_propagate(False)

    clickPageInventory.pack_forget()


    print("Home button clicked")
 
def settingsButtonClick():
    global settingDisplay, user, chosenBottom, chosenBottomV, chosenLeftV, chosenRightV, user_name, usernameE
    settingsButton.config(image = settingsIcon)

    try: 
        invBackground.pack_forget(), clickPageInventory.pack_forget(), settingDisplay.pack_forget()
    except:
        pass

    cleanAll()

    settingDisplay = tk.Frame(app, bg = '#68b27b')
    settingDisplay.pack(fill = tk.BOTH)

    #my account settings
    myAccount = tk.LabelFrame(settingDisplay, text = 'User Settings: ', bg = '#8edba2',font = ('Times New Roman', 12))
    myAccount.pack(side = tk.TOP, anchor = 'nw', fill = tk.X, pady = 20)

    username = tk.Label(myAccount, text = 'Username: ', width = 25, bg = '#8edba2',font = ('Times New Roman', 10))
    username.grid(row = 0, column = 0)

    user_name = tk.StringVar()
    usernameE = tk.Entry(myAccount, textvariable=user_name, bg = '#cfffdc')
    usernameE.insert(0, user)
    usernameE.grid(row = 0, column =1)

    
    #customize widget section
    customizeWidget = tk.LabelFrame(settingDisplay, text = "Customize Widgets: (Blank = none)", bg = '#8edba2',font = ('Times New Roman', 12))
    customizeWidget.pack(side = tk.TOP, anchor = 'nw', fill = tk.X, pady = 5)

    customizeWelcomeWidgets = tk.Label(customizeWidget, text = 'Bottom widget: ', width = 25, bg = '#8edba2',font = ('Times New Roman', 10))
    customizeWelcomeWidgets.grid(row = 0, column = 0)

    customizeWelcomeWidgetsR = tk.Label(customizeWidget, text = 'Right widget: ', bg = '#8edba2',font = ('Times New Roman', 10))
    customizeWelcomeWidgetsR.grid(row = 1, column = 0)

    customizeWelcomeWidgetsL = tk.Label(customizeWidget, text = 'Left widget: ', bg = '#8edba2',font = ('Times New Roman', 10))
    customizeWelcomeWidgetsL.grid(row = 2, column = 0)

    #style for combobox
    style= ttk.Style()
    style.configure("TCombobox", fieldbackground = '#cfffdc', foreground = '#8edba2')

    #customize bottom widget
    chosenBottomV = tk.StringVar()
    chooseBottomWidget = ttk.Combobox(customizeWidget, width = 25, textvariable = chosenBottomV, style = "TCombobox")

    chooseBottomWidget['values'] = ('ReminderWidget', 'calendarWidgetDisplay', 'cutecat')
    chooseBottomWidget.grid(row = 0, column = 1)

    #customize right widget
    chosenRightV = tk.StringVar()
    chooseRightWidget = ttk.Combobox(customizeWidget, width = 25, textvariable = chosenRightV, style = "TCombobox")

    chooseRightWidget['values'] = ('ReminderWidget', 'calendarWidgetDisplay', 'cutecat')
    chooseRightWidget.grid(row = 1, column = 1)

    #customize left widget
    chosenLeftV = tk.StringVar()
    chooseLeftWidget = ttk.Combobox(customizeWidget, width = 25, textvariable = chosenLeftV, style = "TCombobox")

    chooseLeftWidget['values'] = ('ReminderWidget', 'calendarWidgetDisplay', 'cutecat')
    chooseLeftWidget.grid(row = 2, column = 1)


        
        

    #save button
    saveButton = tk.Button(settingDisplay, text = 'Save changes', command =saveButtonClicked)
    saveButton.pack(side = tk.BOTTOM, anchor = 'se', padx = 5, pady =5)

def saveButtonClicked():
    global chosenBottom, chosenBottomV, chooseBottomWidget, user_name, usernameE, user

    #for widget customization
    newBotWidget = chosenBottomV.get()   
    newRigWidget = chosenRightV.get()
    newLefWidget = chosenLeftV.get()

    preferedWidgets(bottomWidget, newBotWidget)
    preferedWidgets(topRightWidget, newRigWidget)
    preferedWidgets(topLeftWidget, newLefWidget)

    #initialization of widget
    preferedWidgets(app, newBotWidget)

    #for username change
    user = user_name.get()
    usernameE.delete(0, tk.END)
    usernameE.insert(0, user)

    homeButtonClick()

def inventoryButtonClick():
    global invBackground, inventory, createInventory, editInventory, itemDisplay, buttonArea, display

    homeWelcome.pack_forget()
    leafDisplay.pack_forget()
    seperator.pack_forget()

    try: 
        invBackground.pack_forget(), clickPageInventory.pack_forget()
    except:
        pass

    inventoryButton.config(image = inventoryIcon)
    settingDisplay.pack_forget()


    invBackground = tk.Frame(app, height = 500, width = 375, bg = '#68b27b')
    invBackground.pack(fill = tk.X)
    invBackground.pack_propagate(False)
    
    display = tk.LabelFrame(invBackground, text = 'Inventory: ', bg = '#68b27b', height = 500, font = ('Times New Roman', 18), relief = 'flat')
    display.pack(fill = tk.X, side = tk.BOTTOM, padx = 20, pady = 30)
    display.pack_propagate(False)

    itemDisplay = tk.LabelFrame(display, bg = '#cfffdc', height = 500)
    itemDisplay.pack(fill = tk.X, pady = 5)
    itemDisplay.pack_propagate(False)

    #the create and edit button
    buttonArea = tk.Frame(itemDisplay, height = 60, bg = '#cfffdc')
    buttonArea.pack(side = tk.BOTTOM, fill = tk.X)
    buttonArea.pack_propagate(False)

    createInventory = tk.Button(buttonArea, bg = '#cfffdc', activebackground = '#cfffdc', image = createNewIcon, command = inventoryCreate, relief = 'flat', height = 50, width = 101, padx = 5, pady = 5)
    createInventory.pack(side = tk.RIGHT)
    
    '''
    editInventory = tk.Button(buttonArea, bg = '#cfffdc', activebackground = '#cfffdc', image = editIcon, command = editInventoryClick, relief = 'flat', height = 50, width = 101, padx = 5, pady = 5)
    editInventory.pack(side = tk.RIGHT)
    '''
     

    for item, detail in inventory.items():
        inventoryItem = tk.Label(itemDisplay, text = f'{item}  \nDescription: {detail[0]}   \nFor sale? {detail[1]}', anchor = 'w', wraplength = 325, font = ('Times New Roman', 12), justify = 'left', bg = '#8edba2', relief = 'groove') #.insert(i, f'{item} | Description: {detail[0]} |  For sale? {detail[1]}')
        inventoryItem.pack(fill = tk.X, anchor = 'w')
    cleanAll()

'''
def editInventoryClick():
    global editInventory
    editInventory.config(image = editIcon)

    itemDisplay.pack_forget()
    display.config(text = 'Which item?')

    displayElement = tk.LabelFrame(display, bg = '#cfffdc', height = 500)
    displayElement.pack(fill = tk.X, pady = 5)
    displayElement.pack_propagate(False)


    items = list(inventory.keys())
    for item in items:
        inventoryItemName = tk.StringVar()
        inventoryItemName.set(item)
        inventoryItemSelect = tk.Button(displayElement, textvariable = item, activebackground = '#cfffdc', bg = '#cfffdc', command = inventoryItemSelect.destroy())
        inventoryItemSelect.pack(fill = tk.X, anchor = 'w')

    def invClick(item):
        print(item)'''



def inventoryCreate():
    global clickPageInventory, saleToggle, itemNameV, itemDescriptionV, saleToggle

    create.config(image = createNewIcon)
    invBackground.pack_forget()

    clickPageInventory = tk.Frame(app, bg = '#68b27b', height = 500, relief = 'flat')
    clickPageInventory.pack(fill = tk.X, padx = 20, pady = 30)
    

    entryAreaInventory = tk.LabelFrame(clickPageInventory, text = "New item: ", font = ('Times New Roman', 18), bg = '#68b27b', height =250)
    entryAreaInventory.pack(pady = 10, fill = tk.BOTH, side = tk.TOP)
    entryAreaInventory.pack_propagate(False)

    itemName = tk.Label(entryAreaInventory, text = "Item name: ", bg = '#68b27b', font = ('Times New Roman', 14))
    itemName.grid(row = 1, column = 0, sticky = 'w', pady = 5, padx  = 5)
    itemNameV = tk.StringVar()
    itemNameE = tk.Entry(entryAreaInventory, bg = '#68b27b', font = ('Times New Roman', 14), textvariable = itemNameV, width = 18)
    itemNameE.grid(row = 1, column = 1, sticky = 'w', pady = 5, padx  = 5)

    itemDescription = tk.Label(entryAreaInventory, text = "Item description: ", bg = '#68b27b', font = ('Times New Roman', 14))
    itemDescription.grid(row = 2, column = 0, sticky = 'w', pady = 5, padx  = 5)
    itemDescriptionV = tk.StringVar()
    itemDescriptionE = tk.Entry(entryAreaInventory, text = "Item description: ", bg = '#68b27b', font = ('Times New Roman', 14), textvariable = itemDescriptionV, width = 18)
    itemDescriptionE.grid(row = 2, column = 1, sticky = 'w', pady = 5, padx  = 5)

    sellingStatus = tk.Label(entryAreaInventory, text = "For sale?: ", bg = '#68b27b', font = ('Times New Roman', 14))
    sellingStatus.grid(row = 3, column = 0, sticky = 'w', pady = 5, padx  = 5)
    saleToggle = tk.Button(entryAreaInventory, text = "Yes", bg = '#cfffdc', font = ('Times New Roman', 14), command = sellingToggle)
    saleToggle.grid(row = 3, column = 1, sticky = 'w', pady = 5, padx  = 5)

    createInventory = tk.Button(entryAreaInventory, text = "Submit", bg = '#cfffdc', command = submitInventory)
    createInventory.grid(row = 4, column = 1, sticky = 'e', pady = 5, padx = 5)

def sellingToggle():
    if saleToggle.cget('text') == 'Yes':
        saleToggle.config(text = "No")
        saleToggle.config(bg = '#b97a56')
    elif saleToggle.cget('text') == 'No':
        saleToggle.config(text = "Yes")
        saleToggle.config(bg = '#cfffdc')

def submitInventory():

    emptyname = tk.StringVar()
    emptyname = emptyname.get()
    item_name = itemNameV.get()
    item_description = itemDescriptionV.get()

    if saleToggle.cget('text') == 'Yes':
        sell_toggle = True
    elif saleToggle.cget('text') == 'No':
        sell_toggle = False


    #validation
    if item_name == emptyname:
        messagebox.showwarning("Warning", "Name cannot be empty!")
        return


    inventory[item_name] = [item_description, sell_toggle]

    inventoryButtonClick()


def CloseOpenIconClick():  #for closing and opening the bottom menu bar
    global hght, count, status
    if status == False: #if closed
        homeButton.grid_forget()
        settingsButton.grid_forget()
        inventoryButton.grid_forget()
        if count < 60:
            hght += 1
            bottomFrame.config(height = hght)
            count += 1
            app.after(7, CloseOpenIconClick)
            
        elif count == 60:
            status = True
            closeOpen.config(image = closeIcon)
            count = 0
            homeButton.grid(row = 0, column = 0, padx = 20)
            homeButton.grid_columnconfigure(0, weight = 0)
            settingsButton.grid(row = 0, column = 1, padx = 20)
            settingsButton.grid_columnconfigure(1, weight = 0)
            inventoryButton.grid(row = 0, column = 2, padx = 20)
            inventoryButton.grid_columnconfigure(1, weight = 0)
            print(count, status)


    elif status == True: #if open 
        homeButton.grid_forget()
        settingsButton.grid_forget()
        inventoryButton.grid_forget()
        if count < 60:
            hght -= 1
            bottomFrame.config(height = hght)
            count += 1
            app.after(7, CloseOpenIconClick)
        elif count == 60:
            status = False
            closeOpen.config(image = openIcon)
            count = 0
            print(count, status)

def click(event): #the function that runs whenver a click is regeisted 

    if event.widget is homeButton: #if the click was on the home button
        event.widget.config(relief = 'flat')
        event.widget.config(image = homeIconClicked)
    elif event.widget is reminderScreenButton:
        event.widget.config(relief = 'flat')
        event.widget.config(image = reminderScreenButtonIconClicked)
    elif event.widget is create:
        event.widget.config(relief = 'flat')
        event.widget.config(image = createNewIconClick)
    elif event.widget is createInventory:
        event.widget.config(relief = 'flat')
        event.widget.config(image = createNewIconClick)
    elif event.widget is settingsButton:
        event.widget.config(relief = 'flat')
        event.widget.config(image = settingsIconClicked)
    elif event.widget is closeOpen:
        event.widget.config(relief = 'flat')
    elif event.widget is inventoryButton:
        event.widget.config(relief = 'flat')
        event.widget.config(image = inventoryIconClick)
    elif event.widget is editReminder:
        event.widget.config(relief = 'flat')
        event.widget.config(image = editIconClick)


def cleanAll(): #function to leave blank screen (except for menu bar which will always be there)

    homeWelcome.pack_forget()
    reminderPage.pack_forget()
    Wtext.config(text = f'Hi {user}', font = ('Times New Roman', 15))
    clickPage.pack_forget()
    calendarWidget.pack_forget()
    reminderWindow.pack_forget()
    seperator.pack_forget()

def preferedWidgets(location, widget):

    #initialization 
    ReminderWidget(location)
    calendarWidgetDisplay(location)

    #this runs if location is bottom widget
    if location == bottomWidget:
        for widgets in bottomWidget.winfo_children():
            widgets.destroy()

    
        if widget == 'ReminderWidget':
            chosenBottom = ReminderWidget
            ReminderWidget(bottomWidget)
        

        elif widget == 'calendarWidgetDisplay':
            chosenBottom = calendarWidgetDisplay
            calendarWidgetDisplay(bottomWidget)

        elif widget == 'cutecat':
            chosenBottom = cutecat
            cutecat(bottomWidget)

        

    #this runs if location is top left widget
    if location == topLeftWidget:
        for widgets in topLeftWidget.winfo_children():
            widgets.destroy()


        if widget == 'ReminderWidget':
            chosenLeft = ReminderWidget
            ReminderWidget(topLeftWidget)
    

        elif widget == 'calendarWidgetDisplay':
            chosenLeft = calendarWidgetDisplay
            calendarWidgetDisplay(topLeftWidget)

        elif widget == 'cutecat':
            chosenLeft = cutecat
            cutecat(topLeftWidget)

    #this runs if location is top right widget
    if location == topRightWidget:
        for widgets in topRightWidget.winfo_children():
            widgets.destroy()


        if widget == 'ReminderWidget':
            chosenRight = ReminderWidget
            ReminderWidget(topRightWidget)
    

        elif widget == 'calendarWidgetDisplay':
            chosenRight = calendarWidgetDisplay
            calendarWidgetDisplay(topRightWidget)

        elif widget == 'cutecat':
            chosenRight = cutecat
            cutecat(topRightWidget)





    
        


#main application background
app = tk.Tk()
app.title("Plant app")
app.configure(bg = '#68b27b')
app.geometry("375x667") # 375 x 667 for a iphone screen size

app.bind('<Button-1>', click) #this runs the function click everytime button1 is registered


#All the photo icons
reminderScreenButtonIcon = tk.PhotoImage(file = 'iconImages/reminder2.png')
reminderScreenButtonIconClicked = tk.PhotoImage(file = 'iconImages/reminder.png')

homeIcon = tk.PhotoImage(file = 'iconImages/homeicon2.png')
homeIconClicked = tk.PhotoImage(file = 'iconImages/homeicon.png')

settingsIcon = tk.PhotoImage(file = 'iconImages/cogicon2.png')
settingsIconClicked = tk.PhotoImage(file = 'iconImages/cogicon.png')

createNewIcon = tk.PhotoImage(file = 'iconImages/createNewIcon.png')
createNewIconClick = tk.PhotoImage(file = 'iconImages/createNewIconClick.png')

editIcon = tk.PhotoImage(file = 'iconImages/editIcon.png')
editIconClick = tk.PhotoImage(file = 'iconImages/editIconClick.png')

inventoryIcon = tk.PhotoImage(file = 'iconImages/inventory.png')
inventoryIconClick = tk.PhotoImage(file = 'iconImages/inventoryClick.png')

leaf = tk.PhotoImage(file = 'iconImages/leaf.png')
leaf2 = tk.PhotoImage(file = 'iconImages/leaf2.png')

closeIcon = tk.PhotoImage(file = 'iconImages/close.png')
openIcon = tk.PhotoImage(file = 'iconImages/open.png')

test = tk.PhotoImage(file = 'iconImages/test.png')


#menu bar
count = 0
hght = 60
bottomFrame = tk.LabelFrame(app, bg = '#b97a56', height = 60, relief = 'flat')
bottomFrame.pack(fill = tk.X, side = tk.BOTTOM)
bottomFrame.pack_propagate(False)

#the side button that closes and opens the menu bar
status = True #true = open, false = close
closeOpen = tk.Button(app, command = CloseOpenIconClick, relief = 'flat', image = closeIcon, height = 5, bg = '#7f5c47', activebackground='#7f5c47', highlightthickness=0)
closeOpen.pack(side = tk.BOTTOM, fill = tk.X)

#home button
homeButton = tk.Button(bottomFrame, command = homeButtonClick,  image = homeIcon, bg = '#b97a56', relief = 'flat', activebackground='#b97a56', width = 45) 
homeButton.grid(row = 0, column = 0, padx = 20)
homeButton.grid_columnconfigure(0, weight = 0)

#settings button
settingsButton = tk.Button(bottomFrame, command = settingsButtonClick,  image = settingsIcon, bg = '#b97a56', relief = 'flat', activebackground='#b97a56', width = 45) 
settingsButton.grid(row = 0, column = 1, padx = 20)
settingsButton.grid_columnconfigure(1, weight = 0)

#inventory button
inventoryButton = tk.Button(bottomFrame, command = inventoryButtonClick,  image = inventoryIcon, bg = '#b97a56', relief = 'flat', activebackground='#b97a56', width = 45) 
inventoryButton.grid(row = 0, column = 2, padx = 20)
inventoryButton.grid_columnconfigure(1, weight = 0)



#top welcome screen light green one
homeWelcome = tk.Frame(app, bg = '#cfffdc', height = 350, relief = 'flat')
homeWelcome.pack(fill = tk.BOTH)
homeWelcome.pack_propagate(False)

#very top bar
topBar = tk.LabelFrame(homeWelcome, bg = '#cfffdc', relief = 'flat')
topBar.pack(side = tk.TOP, fill = tk.X)

Wtext = tk.Label(topBar, text = f"Welcome {user}", font = ('Times New Roman', 20), bg = '#cfffdc')
Wtext.pack(side = tk.RIGHT, anchor = 'ne', padx =10, pady = 20)

#leaf
leafDisplay = tk.Label(topBar, image = leaf, relief = 'flat', borderwidth=0)
leafDisplay.pack(side = tk.LEFT, anchor = 'w')






#widget frame thats customizable part below

#the bottom widget (biggest)
bighomeWidget = tk.LabelFrame(homeWelcome, bg = '#8edba2', height = 150, width = 375, relief = 'flat', highlightthickness=0)
bighomeWidget.pack(side = tk.BOTTOM, fill = tk.X, padx =5)
bighomeWidget.pack_propagate(False)

bottomWidget = tk.Frame(bighomeWidget, bg = '#8edba2', height = 150, width = 375)
bottomWidget.pack(anchor = 's',side = tk.BOTTOM, fill = tk.BOTH)
bottomWidget.pack_propagate(False)

#the topright and topleft widgets thats smaller than the bottom one
homeWidgets = tk.LabelFrame(homeWelcome, bg = '#8edba2', height = 200, width = 375, relief = 'flat', highlightthickness=0)
homeWidgets.pack(side = tk.BOTTOM, fill = tk.X, padx =5)
homeWidgets.pack_propagate(False)

topLeftWidget = tk.Frame(homeWidgets, bg = '#8edba2', width = 188, height = 100)
topLeftWidget.pack(anchor = 'nw', side = tk.LEFT)
topLeftWidget.pack_propagate(False)

topRightWidget = tk.Frame(homeWidgets, bg = '#8edba2', width = 187, height = 100)
topRightWidget.pack(anchor = 'ne', side = tk.RIGHT)
topRightWidget.pack_propagate(False)


#bottom darker green frame bit
bigButtons = tk.Frame(app, bg = '#68b27b', relief = 'flat')
bigButtons.pack(fill = tk.BOTH, expand = True, side =tk.BOTTOM)


#leaf
leafDisplay = tk.Label(bigButtons, image = leaf2, relief = 'flat', borderwidth=0, anchor ='s', bg = '#68b27b')
leafDisplay.pack(expand = True, side = tk.RIGHT, anchor = 'se')

#seperator between dark green and light green part
seperator = tk.Frame(app, bg = '#8edba2', height = 12)
temp = tk.Label(seperator, height =12, bg = '#8edba2')
temp.pack(fill = tk.X)
temp.pack_propagate(False)



#initialization 
ReminderWidget(bottomWidget)
reminderWindow.pack_forget()
reminderClick()
reminderPage.pack_forget()
createClick()
clickPage.pack_forget()

calendarWidgetDisplay(bottomWidget)
calendarWidget.pack_forget()

chosenBottomV = tk.StringVar()
chosenBottom = (ReminderWidget)

chosenRightV = tk.StringVar()
chosenRight = (calendarWidgetDisplay)

chosenLeftV = tk.StringVar()
chosenLeft = (calendarWidgetDisplay)
#calendarWidgetDisplay
#ReminderWidget

settingsButtonClick()
settingDisplay.pack_forget()
settingDisplay.pack_forget()

inventoryButtonClick()
invBackground.pack_forget()

inventoryCreate()
clickPageInventory.pack_forget()
#editInventoryClick()


Wtext.config(text = f"Welcome {user}", font = ('Times New Roman', 15))
homeWelcome.pack(fill = tk.X)
homeWelcome.pack_propagate(False)
bigButtons.pack(fill = tk.BOTH, expand = True, side =tk.BOTTOM)
seperator.pack(side =tk.BOTTOM, fill = tk.X)
seperator.pack_propagate(False)

#


app.mainloop()


