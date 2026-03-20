menu = """
===Travel Destination Planner===
1. Add a destination
2. Update a destination
3. Delete a destination
4. View all destinations
5. Exit
"""
destination = []

while True:
    break_all = False # This is added so that all loops will end if there's 2 or more loops
    print(menu)
    opt = input("Choose an option (1-5): ")

    # Option 1
    if opt == "1":
        while True:
            add = input("Enter a new destination (Type \"cancel\" to abort): ").title() # Enter new destination, the .title() will make the first alphabet on the word automatically uppercased
            if len(add) == 0: # When the input is empty, will loop to the input above
                print("Please enter an appropriate destination.\n")
            elif add in destination: # When the destination typed is already exists, will loop to the input above
                print("Destination already exists. Please add a new destination.\n")
            elif add == "Cancel": # Cancel operation, breaks loop and goes back to menu
                print("Process canceled.\n")
                break
            else: # Successful addition of new destination, breaks loop and goes back to menu
                destination.append(add)
                print("New destination successfully added!")
                print("Updated list of destinations: " + ", ".join(destination) + "\n") # The ", ".join(destination) means it will print out the list without brackets and quotation marks
                break
    
    # Option 2
    elif opt == "2":
        while break_all == False:
            choose = input("Which destination do you want to update? (Type \"cancel\" to abort): ").title()
            if choose in destination:
                while True:
                    update = input("Enter an updated version of \"" + choose + "\" (Type \"cancel\" to abort): ").title() # Literally a copy paste from the code above
                    if len(update) == 0:
                        print("Please enter an appropriate destination.\n")
                    elif update in destination:
                        print('The destination you are trying to update already exists. Please try again or cancel.\n')
                    elif update == "Cancel":
                        print('Process canceled.\n')
                        break_all = True
                        break
                    else:
                        destination.remove(choose) # The old destination will be removed first,
                        destination.append(update) # then the new one will be added (very weird method of updating, yeah)
                        print("\"" + choose + "\" has been successfully updated to \"" + update + "\"!\n")
                        break_all = True
                        break
            else:
                print("Sorry, destination not found. Please try again.\n")
    
    # Option 3
    elif opt == "3":
        while break_all == False:
            delete = input("Which destination do you want to remove? (Type \"cancel\" to abort): ").title() # Same as above
            if delete in destination:
                destination.remove(delete)
                print("\""+ delete +"\" has been successfully removed!\n")
                break_all = True
            elif delete == "Cancel":
                print("Process canceled.\n")
                break
            else:
                print("Sorry, destination not found. Please try again.\n")

    # Option 4
    elif opt == "4":
        if len(destination) != 0: # If the list is not empty
            print("List of available destinations:")
            print(", ".join(destination) + "\n")
        else:
            print("No destinations in the list yet.\n")

    # Option 5
    elif opt == "5": # Breaks the loop
        print("Trip planning ended. Safe travels!")
        break
    
    # Invalid input
    else:
        print("Invalid choice. Please try again.\n") # Will loop to the menu
