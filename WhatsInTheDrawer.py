
""""
Name : Muhammad Shahmeer Khan
Due Date : 07/01/2026
Title : Whats in the drawer
Description : A program to play the game "Whats in the drawer" that uses list to function. 

"""

item = ["pens","pencils","eraser","paper clips","sticky notes","scissors","tape","stapler","rubber bands","notepad","highlighter","marker","glue stick","sharpener","ruler","flash drive","coins","keys","batteries","safety pins","calculator","envelopes","stickers","old receipts","small notebook","thumbtacks","cable clips","magnets","chapstick","snacks","gum","hair tie","paper knife","postcards","photos","small toy","buttons","nail clippers"]

# Get Yes or No (Y/R) Function
def getYorN(question): 
    """Asks the user with a yes or no question and keeps asking until a valid response ('y' or 'n') is entered.
    
    Argument:
        question: the question to display to the user
    
    Returns:
        response: The input/response that the user gives
    """

    # Keep looping until the user enters a valid response
    while True: 

        # Ask the user the question and convert input to lowercase
        response = input(question + " (y/n): ").lower() 

        # Check if the response is valid
        if response == "y" or response == "n": 
            return response 
        else: 
            # Display error message for invalid input
            print("Invalid input, please enter 'y' or 'n'.") 


# Looking through the list for an item
def itemLookFor(item, list):
    """
    Searches a list for a specified item and prints a message if found.

    Argument
        item: The item to search for.
        list: The list to search through.
    """
    # Declare variables
    value = False
    count = 0
    
    #Run a loop to go through list and find the specific item that the user is looking for
    for i in range(len(list)):
        # If Matches
        if list[i] == item:
            print()
            print("There is a {} in the drawer".format(item))
            value = True
            return
        
    # If item not found
    print()
    print("There is no {} in the drawer.".format(item))
                

def countList(list):
    """
    Counts the number of items in a list and prints the total.

    Arguments:
        list: The list to be counted.
    """
    # Declare variable
    count = 0
    # Start a loop to count the number of items
    for i in range(len(list)):
        count += 1
    print("There are {} items in the list".format(count))


def showList(list):
    """
    Displays all items in a list with their index numbers.

    Arguments:
        list: The list to be displayed.
    """
    # Printing the whole list
    for i in range(len(list)):
        print(i + 1,":",list[i])

def removeItem(list):
    """
    Removes a specified item from a list based on user input.
    Arguments:
        list: The list from which an item will be removed.
    """
    # Ask for the item to remove
    item = str(input("Enter the item you want to remove: "))
    
    # Start a loop to look through the list for the item
    for i in range(len(list)):
        if list[i] == item:
            list.remove(item)
            print()
            print("Item removed successfully")
            return
    
    # If item is not in the list
    print()
    print("The {} is not in the list.".format(item))


def addItem(list):
    """
    Adds an item to a list, checking for duplicates before appending.
    Arguments:
        list: The list to which the item will be added.
    """
    # Ask the user for an item to add
    item = input("Enter the item you want to add: ")
    # Search through the list if the item is already there or isnt
    for i in range(len(list)):
        # If the item is in the list
        if list[i] == item:
            # Ask user if they still want to append
            choice = getYorN("The item is in the list already. Do you still want to continue")
            # Yes choice
            if choice == "y":
                list.append(item)
                print()
                print("Item added successfully")
                return
            # No Choice
            else:
                print()
                print("Going back to main program")
                return
    # Append if it was not in the list
    else: 
        list.append(item)
        print()
        print("Item added successfully")
    

#                                                           --------------
#                                                            Main Program
#                                                           --------------
 
print("What's in the drawer")
print("Type '?' to get a full guide of the program.")

while True:
    # Ask user for input
    look_for_item = input("What are you looking for? ").strip()

    # If user wants to see the whole list
    if look_for_item == "":
        print()
        print("This can not be left empty. Please try again")
    # Shows the whole list
    elif look_for_item == "LIST":
        showList(item)
    # If user wants to stop
    elif look_for_item == "STOP":
        print()
        print("Good Bye!")
        break
    # User wants to count the number of items
    elif look_for_item == "COUNT":
        countList(item)
    # User wants to remove an item
    elif look_for_item == "GET":
        removeItem(item)
    # Append to the list at the end
    elif look_for_item == "PUT":
        addItem(item)
    # Show the user the guide
    elif look_for_item == "?":
        print("""Brief Explanation:
    1. LIST  : Lists all the items in the list
    2. COUNT : Tells you the number of items present in the list
    3. STOP  : End the program
    4. GET   : Remove an item from the list
    5. PUT   : Add an item to the list
    """)
    # Look through the list for the item
    else:
        itemLookFor(look_for_item, item)