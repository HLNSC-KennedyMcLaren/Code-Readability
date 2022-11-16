#Lawn cutting simulator
name = str(input("Please input your name.\n-"))
address = str(input("Please input your address.\n-"))
phone = input("Please input your phone number.\n-")
#input and validation for width and length
while True:
    width = float(input("Please enter the width of your lawn in meters to the 2nd decimal place\n-"))
    length = float(input("Please enter the length of your lawn in meters to the 2nd decimal place\n-"))
    if width < 2.0 or width > 30.0 or length < 2.0 or length > 50:
        print("Sorry, that's an unavailable size. Please try a different size")
    else:
        break
#calculate area
area = width * length

#lawn care go brr (calculate lawn care quality if any)
economy = 1.45
standard = 1.80
luxury = 2.15
lawn_care = input("Please input the quality of your lawn care. 0 = none, 1 = economy, 2 = standard, 3 = luxury\n-")
if lawn_care == '1':
    area_value = economy * area
elif lawn_care == '2':
    area_value = standard * area
elif lawn_care == '3':
    area_value = luxury * area
else:
    area_value = area

#end ish (totals)
labour = area * 1.50
total = labour + area_value
totalVAT = total * 1.2
totalVAT = round(totalVAT, 2)
total = round(total, 2)

#actual end (print the bill)
print("Here is your bill:")
print("Name:", name)
print("Address:", address)
print("Phone number:", phone)
print("Area of lawn:", area)
print("labour:", labour)
if lawn_care == '0':
    pass
else:
    print("Lawn care:", lawn_care, "value:",area_value)
print("Total:", totalVAT)
print("Total before VAT:", total)
#3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
