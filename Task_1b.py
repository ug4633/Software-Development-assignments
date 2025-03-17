def rectangleArea(length,width):
    try:                                                 # if length and width is a number, it calculates result via width*length like normal
        area = float(length)*float(width)
        return area
    except:                                              # however if one of length or width is an unknown variable like x, it will return result with the unknown varibale.
        if length == width:                              # and if length and width is the same variable, will return squared version of it.
            area = (length + "^2")
            return area
        else: 
            area = length+width
            return area
        
leng = input("Enter length of rectangle: ")              # gets the length of an rectangle
widt = input("Enter width of rectangle: ")               # gets the width of an rectangle
result = rectangleArea(leng,widt)
print("Area of the rectangle is {}. ".format(result))    # prints the resulting area of rectangle