print("Hello and welcome to Suhurrith's Restaurant Chatbot!!")

print("")

name = input("What is your name?: ")

restaurant = input("Hello " + name + ", what is the desired restaurant?: ")

dish = input(f"What would you like from this restaurant: {restaurant}")

print("")

print("Please choose from the following options: ")
print("1. Print your restaurant ")
print("2. Print your dish. ")
print("3. Call the restaurant to check on the dish. ")
print("4. Exit the chatbot. ")

print("")


response = int(input("Enter the number of your decision: "))

if (response == 1):
    print("The name of the restaurant is " + restaurant +".")
elif (response == 2):
    print("The name of the dish you ordered is *" + dish + "* Have a great meal.")
elif (response == 3):
    print(f"Calling this restaurant: *{restaurant}* . Beep....")
elif (response == 4):
    print("Bye, bye " + name +"! " + "You have successfully exited the Restaurant chatbot.")
    exit()
else:
    print("You have entered the wrong input, please enter a number from 1-4. ")

