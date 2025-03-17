print("Task 1a:\n")
#Task 1a
for i in range(0,10):
    print(i+1)
    
print("\nTask 2a:\n")
#Task 2a
def bodyMassIndex(weight, height):
    return (weight/height**2)

person1Data = ['Bartholomew', 1.78, 80]
person2Data = ['Petal', 1.67, 71]
person3Data = ["Joe", 1.68, 55]

for i in range(1,4):
    data = globals()[f'person{i}Data']
    weight = data[2]
    height = data[1]
    
    BMI = bodyMassIndex(weight, height)
    
    if BMI < 18.5:
        weightClass = 'Underweight' 
    elif 18.5 <= BMI < 25:
        weightClass = 'Normal weight'
    elif 25 <= BMI < 30:
        weightClass = 'Overweight'
    elif BMI >= 30:
        weightClass = 'Obesity'
        
    print(f"person n.{i} weighs " + str(weight) + " kilos and is " + str(height) + " metres tall. \n" + f"person n.{i}'s BMI is " + str(round(BMI,1)) + " which classifies them as " + weightClass + '\n') 

print("\nTask 2c:\n")
#Task 2c
Array_A = {
    'Red':'#FF0000',
    'White':'#FFFFFF',
    'Green':'#008000',
    'Blue':'#0000FF'
}

Array_B = [22.7, 28.5, 22.1]

for key, value in Array_A.items():
    print(key, value)

print()

for i in range(len(Array_B)):
    print(Array_B[i])