#initialising variables and lists used
items = []
itemCount = 0
#defining a list of possible commands
possibleCommands = ["help", "add item", "delete item", "quit", "list items"]
#printing welcome message along with all possible commands
print("Welcome to the best Item Management System!")
print("Please enter a command, possible commands:",possibleCommands)

#starting a while loop to iterate through commands
while True:
    #converting entered command to lower case
    command = input("Please enter command: ").lower()


    #checking if command is equal to "quit"
    if command == possibleCommands[3]:
        #Displaying "bye" message and closing program

        print("goodbye")
        exit()
