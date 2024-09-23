print("Hello and welcome to Suhurrith's Chatbot!!")

print("")

name = input("What is your name?: ")

age = int(input("Hello " + name + ", what is your age?: "))

print("")

print("I can almost reminsice about my days when i was " + str(age) + ", Mr. " + name)

print("")

print("Please choose from the following options: ")
print("1. Print your name. ")
print("2. Print your age. ")
print("3. Print your name and age. ")
print("4. Exit the chatbot. ")

print("")

response = int(input("Enter the number of your decision: "))

if (response == 1):
    print("Your name is " + name +".")
elif (response == 2):
    print("Your age is " + str(age) + ".")
elif (response == 3):
    print("Your name is " + name + " and your age is " + str(age) + ".")
elif (response == 4):
    print("Bye, bye " + name +"! " + "You have successfully exited the chatbot.")
    exit()
else:
    print("You have entered the wrong input, please enter a number from 1-4. ")

