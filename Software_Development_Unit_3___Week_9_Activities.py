car = {
    "8SD453": "Sedan", 
    "8SD421": "Sedan", 
    "7HB443": "SUV", 
    "7HB446": "Wagon", 
    "8SD521": "SUV", 
    "ABC123": "Hatchback"
    }

def linear_search(search_dict, search_key):
    for i in search_dict:
        if i == search_key:
            return search_dict[i]
            break


print(linear_search(car, '7HB446'))
#This is if the give is a dictionary

def selection_sort(search_dict): 
  
    sorted = {}
    temp = []
    

    #This is just beacuse i dont get what it means by ascending order where none of the registration or body type has a form of ranking
    #So intead i grabbed the --LAST 3 NUMBERS-- from each key of car dictionary and use the numbers from that as a ranking
    carNum = {}
    for i in search_dict:
      foo = ''
      carRank = list(i)
      for j in carRank:
          if j.isdigit() and j != carRank[0]:
              foo = foo + j
      carNum[foo] = car[i]
      
    
    #this part sorts the keys
    for i in carNum:
        temp.append(i)
        
    for i in range(len(temp)): #goes through each index of array
      minVal = temp[i] #sets current minimum value as the first index's value
      min = i #sets first min as index of minimum value
    
      for j in range(i+1, len(temp)): #goes through each index of the arraay excluding the current one (i)
          if minVal > temp[j]: #if the value of j is less then the current value then
              minVal = temp[j] #it makes the current minimum value to j's value
              min = j 
      temp[i], temp[min] = temp[min], temp[i] #replaces current position and minimum's position's values
    
    #sorting part of dictionary is here
    listed = list(carNum.keys())  
    listedCar = list(car.keys())
    
    for i in temp:
        
        pos = listed.index(i)
        
        
        
        key = listedCar[pos]
        sorted[key] = car[key]

        
        
    return sorted
    '''print(temp)
    print('\n')
    print(listed)
    print(listedCar)
    print('\n')
    print(carNum)
    print(car)'''
    
print(selection_sort(car))










'''
#This is if the given array is a dictionary
def selection_sort(search_dict, og): 
    #this part sorts the keys
    sorted = {}
    temp = []
    for i in search_dict:
        temp.append(i)
    temp = selection_sort_list(temp)
    
    #sorting part of dictionary is here
    for i in temp:
        sorted[i] = carNum[i]
    print(temp)
    print(sorted)


#This below part is if the given array is a list 
def selection_sort_list(array):
    for i in range(len(array)): #goes through each index of array
        minVal = array[i] #sets current minimum value as the first index's value
        min = i #sets first min as index of minimum value
        
        for j in range(i+1, len(array)): #goes through each index of the array excluding the current one (i)
            if minVal > array[j]: #if the value of j is less then the current value then
                minVal = array[j] #it makes the current minimum value to j's value
                min = j 
        array[i], array[min] = array[min], array[i] #replaces current position and minimum's position's values
    return(array)



#This is just beacuse i dont get what it means by ascending order where none of the registration or body type has a form of ranking
#So intead i grabbed the --LAST 3 NUMBERS-- from each key of car dictionary and use the numbers from that as a ranking
carNum = {}
for i in car:
    temp = ''
    carRank = list(i)
    
    for j in carRank:
        if j.isdigit() and j != carRank[0]:
            temp = temp + j
    carNum[temp] = car[i]
        

print(selection_sort(carNum, car))
'''