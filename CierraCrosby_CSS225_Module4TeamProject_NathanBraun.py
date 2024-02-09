#Cierra Crosby
#2/9/2024
#Instructor Nathan Braun
#CSS 225
#This program allows you to choose options from 0-8 using numbers only
#This program prints a statement when a user choose a option from the list below:
#This program uses the list to print a statement 
# Please choose an option from the list below
# 0. Exit the door
# 1. Bake a cake
# 2. Go running
# 3. Eat lunch
# 4. Take a shower
# 5. Clean room
# 6. Go to sleep
# 7. Play outside
# 8. Make me a burger


print("Please Choose your option from the list below:(using only the numbers 0-8)")
print("0. Exit the door")
print("1. Bake a cake")
print("2. Go running")
print("3. Eat lunch")
print("4. Take a shower")
print("5. Clean room")
print("6. Go to sleep")
print("7. Play outside")
print("8.Make me a burger")

option = input("Enter option here: ")
Exit = "0"
cake = "1"
run = "2"
lunch = "3"
shower = "4"
room = "5"
sleep = "6"
playoutside = "7"
burger = "8"

if option == Exit:
    print("You chose option 0: Exit the door")
    print("Get out!")
elif option == cake:
    print("You chose option 1: Bake a cake")
    print(" First we need to start by gathering the ingredients.")
elif option == run:
    print("You chose option 2: Go running")
    print("Now where did I put my running shoes?")
elif option == lunch:
    print("You choose option 3: Eat Lunch")
    print("First I need to see what I have for leftover.")
elif option == shower:
    print("You choose option 4: Take a shower")
    print("Now am I going to wash my hair today?.")
elif option == room:
    print("You choose option 5: Clean Room")
    print("Where am I going to start?")
elif option == sleep:
    print("You choose option 6: Go to sleep")
    print("I need to bring my heating pad before I get into bed.")
elif option == playoutside:
    print("You choose option 7: play outside")
    print("Let's go play.")
elif option == burger:
    print("You choose option 8: Make me a burger")
    print("Where is the kitchen?")
else:
    print("That is not an option!")
