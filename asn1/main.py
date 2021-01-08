#AUTHOR: Hadi El-Kadri
#CONSTANTS
EGG = .99
BACON = .49
SAUSAGE = 1.49
HASHBROWN = 1.19
TOAST = .79
COFFEE = 1.09
TEA = .89

#BREAKFASTS
SBreakfast = EGG + HASHBROWN + TOAST*2 + BACON*2 + SAUSAGE
RBreakfast = EGG*2 + HASHBROWN + TOAST*2 + BACON*4 + SAUSAGE*2
BBreakfast = EGG*3 + HASHBROWN*2 + TOAST*4 + BACON*6 + SAUSAGE*3

#INITIALIZE VARIABLES TAX QUANTITY AND COST
TAX = 1.13
totalCOST= 0
quantity = 0
listofitemsonmenu = ("coffee", "tea", "hashbrown", "bacon", "sausage", "egg", "toast", "smallbreakfast", "regularbreakfast", "bigbreakfast")

#INTRODUCTION TO THE RESTAURANT AND MENU ITEMS + PRICES
print("Welcome to Abou Arab's breakfast!")
print("Please take a look at our menu!\n")
print("MENU:")
print("Egg = $.99, Bacon = $.49 Sausage = $1.49 Hashbrown = $1.19 Toast = $.79 Coffee = $1.09 Tea = $.89 \nSmall Breakfast = $"+str(round(SBreakfast,2)),"Regular Breakfast = $" + str(round(RBreakfast,2)),"Big Breakfast = $" + str(round(BBreakfast,2)) + "\n")

#ASKING FOR THE ORDER OF THE CUSTOMER
order = (input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: "))

#TAKING IN ANY INPUT AND LOWERCASING AND TAKING AWAY WHITESPACES NO MATTER THE INPUT
order = order.lower().strip()
wordList = order.split()
order = "".join(wordList)

#AS LONG AS THE CUSTOMER DOES NOT INPUT Q THE FOLLOWING CODE WILL EXECUTE
while order != "q":
    order = order.lower().strip()
    wordList = order.split()
    order = "".join(wordList)

#IF THE CUSTOMER ENTERS AN INVALID ORDER
    if order not in listofitemsonmenu:
        print("You have entered an invalid item!")
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

#IF THE CUSTOMER WANTS INDIVIDUAL ITEM EGG
    if order == "egg":
        #ASKS FOR THE QUANTITY OF EGG
        quantity = input("Please enter an amount: ")
        #IN AN INVALID QUANTITY WAS INPUT
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        #THE CHOSEN ITEM IS ADDED TO THE TOTAL COST OF THE WHOLE ORDER
        totalCOST = totalCOST + EGG * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

#IF THE CUSTOMER WANTS INDIVIDUAL ITEM BACON
    if order == "bacon":
        quantity = input("Please enter an amount: ")
        #IN AN INVALID QUANTITY WAS INPUT
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        #THE CHOSEN ITEM IS ADDED TO THE TOTAL COST OF THE WHOLE ORDER
        totalCOST = totalCOST + BACON * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "hashbrown":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + HASHBROWN * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "sausage":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + SAUSAGE * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "toast":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + TOAST * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "coffee":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + COFFEE * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "tea":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + TEA * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "smallbreakfast":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + SBreakfast * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "regularbreakfast":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + RBreakfast * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    if order == "bigbreakfast":
        quantity = input("Please enter an amount: ")
        while quantity.isnumeric() is False:
            print("You have entered an invalid quantity. Please try again.")
            quantity = input("Please enter an amount: ")
        totalCOST = totalCOST + BBreakfast * float(quantity)
        order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

#THE COST IS CALCULATED AND SHOWN TO THE CUSTOMER
print("Thank you for ordering! Your total is: " + "\n")
print("Pre total:" + str((round(totalCOST, 2))))
print("Tax:" + str(round(totalCOST * TAX - totalCOST, 2)))
print("Grand total:" + str(round(totalCOST * TAX, 2)))
