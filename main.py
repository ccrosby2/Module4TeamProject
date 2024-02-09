# Please choose an option from the list below
# 1. Bake a cake
# 2. Go running
# 3. Eat lunch
# 4. Take a shower
# 5. Clean room
# 6. Go to sleep
# 0. Exit

print("Please Choose your option from the list below:")
print("1. Bake a cake")
print("2. Go running")
print("3. Eat lunch")
print("4. Take a shower")
print("5. Clean room")
print("6. Go to sleep")
print("0. Exit")

option = input("Enter option here: ")
cake = "1"
run = "2"
lunch = "3"
shower = "4"
room = "5"
sleep = "6"
exit = "0"
if option == cake:
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
elif option == exit:
    print("You choose option 0: Exit")
    print("We'll see you next time.")
else:
    print("That is not an option!")

