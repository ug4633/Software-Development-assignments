import math


def binarySearch(list, target):
    L = 0
    R = len(list) - 1
    comparisons = 0
    while L <= R:
        comparisons = comparisons + 1
        m = L + math.ceil((R-L) / 2)
        if m < target:
            L = m + 1
        elif m > target:
            R = m - 1
        else:
            return m, list[m], comparisons
    return "Unsuccessful"

nameList = [
'Agapi',
'Andrew',
'Bonnie',
'Cathy',
'Dominic',
'Edward',
'Huang',
'Jordon',
'Joshua',
'Le',
'Mason',
'Ngor',
'Oscar',
'Tim',
'Ursula',
'Vicky',
'Vinnie'
]

print(binarySearch(nameList, nameList.index('Vinnie')))
print(binarySearch(nameList, nameList.index('Agapi')))
print(binarySearch(nameList, nameList.index('Joshua')))
