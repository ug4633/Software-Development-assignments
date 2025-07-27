import tkinter as tk
from tkinter import messagebox

dayData = {}
#statistics functions 
def findAverage(array):
    total = 0

    for value in array:
        total = int(total) + int(value)

    average = total/len(array)
    return average
def findMinimum(array):
    for values in array:
        if 'minimum' in locals():
            if int(values) < minimum:
                minimum = int(values)
        else:
            minimum = int(values)
    return minimum
def findMaximum(array):
    for values in array:
        if 'maximum' in locals():
            if int(values) > maximum:
                maximum = int(values)
        else:
            maximum = int(values)
    return maximum

#function for making the day rows
def createRow(name):
    back = tk.Frame(days)
    back.pack(fill = tk.X)

    #name of the day
    day = tk.LabelFrame(back, text = name, relief = 'flat')  
    day.pack(side = tk.LEFT, fill = tk.X)

    dayLabel = tk.Label(day, anchor = 'n').grid(row = 1, column = 0)

    #statistic stuff
    stats = tk.LabelFrame(back, relief = 'flat') 
    stats.pack(side = tk.RIGHT, fill = tk.X, pady = 10)

    seperator = tk.Label(stats, padx = 10).grid(row = 0, column = 0)

    name_min_value = tk.StringVar()
    dayMinT = tk.Label(stats, text = 'Min: ', padx = 50, pady = 10, anchor = 'e').grid(row = 0, column = 1)
    dayMinE = tk.Entry(stats, textvariable = name_min_value).grid(row = 0, column = 2)

    seperator = tk.Label(stats, padx = 50).grid(row = 0, column = 3)

    name_max_value = tk.StringVar()
    dayMaxT = tk.Label(stats, text = 'Max: ', pady = 10, anchor = 'e').grid(row = 0, column = 4)
    dayMaxE = tk.Entry(stats, textvariable = name_max_value).grid(row = 0, column = 5)

    dayData[name] = name_min_value, name_max_value

def click():
    minArray = []
    maxArray = []
    
    #Validation part
    for mini, maxi in dayData.values():
        if (mini and maxi):
            try:
                mini = int(mini.get())
                maxi = int(maxi.get())
            except:
                messagebox.showwarning("Warning", "Temperatures must be a number")
                return

            if mini <= 55:
                if mini <= maxi:
                    minArray.append(mini)
                    maxArray.append(maxi)
                else:
                    messagebox.showwarning("Warning", "Minimum temperature must be less than maximum temperature")
                    return
            else:
                messagebox.showwarning("Warning", "Temperateus must be in Celsius (range between [-25, 55])")
                return

                

        else:
            messagebox.showwarning("Warning", "Temperatures cannot be empty")
            return
    
    
    avgMinTemp = findAverage(minArray)
    avgMaxTemp = findAverage(maxArray)

    lowMinTemp = findMinimum(minArray)
    lowMaxTemp = findMinimum(maxArray)

    maxMinTemp = findMaximum(minArray)
    maxMaxTemp = findMaximum(maxArray)

    #file writing and reading part
    with open('dailyTemperatures.txt', 'w') as file:
        file.write(f"Input values were: \n\nMonday \nMin: {dayData['Monday'][0].get()} Max: {dayData['Monday'][1].get()} \n\n")
        file.write(f"Tuesday \nMin: {dayData['Tuesday'][0].get()} Max: {dayData['Tuesday'][1].get()} \n\n")
        file.write(f"Wednesday \nMin: {dayData['Wednesday'][0].get()} Max: {dayData['Wednesday'][1].get()} \n\n")
        file.write(f"Thursday \nMin: {dayData['Thursday'][0].get()} Max: {dayData['Thursday'][1].get()} \n\n")
        file.write(f"Friday \nMin: {dayData['Friday'][0].get()} Max: {dayData['Friday'][1].get()} \n\n")

        file.write(f"The average minimum temperature was: {avgMinTemp} Celsius\n")
        file.write(f"The average maximum temperature was: {avgMaxTemp} Celsius\n\n")

        file.write(f"The average maximum temperature was: {avgMaxTemp} Celsius\n\n")
        file.write(f"The highest minimum temperature was: {maxMinTemp} Celsius\n\n")

        file.write(f"The lowest maximum temperature was: {lowMaxTemp} Celsius\n")
        file.write(f"The highest maximum temperature was: {maxMaxTemp} Celsius\n\n")

    #prints after writing
    print(open('dailyTemperatures.txt', 'r').read())



#gui design
main = tk.Tk()
main.title("Temperature Entry GUI")

#top instruction bit
window = tk.Frame(main)
window.pack(fill = tk.X)

instructions = tk.Label(window, text = 'Please enter the minimum and maximum temperatures for each day: ', pady = 10, font = ('utopia', 12)).grid(row = 0)


days = tk.Frame(main)
days.pack(fill = tk.X)

#making the day rows easier
createRow('Monday')
createRow('Tuesday')
createRow('Wednesday')
createRow('Thursday')
createRow('Friday')

#submit button
submitButton = tk.Button(days, text = 'Submit', command = click)
submitButton.pack(side = tk.BOTTOM, pady = 35)

main.mainloop()

