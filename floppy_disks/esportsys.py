import datetime
import random
import json
menu = """\n
=----= Campus E-Sports Event Management System =----=
@[Manage Events]
[1] Add New Event
[2] Update Event
[3] Delete Event
[4] Display All Events
@[Manage Participants]
[5] Add Participant
[6] Update Participant's Details
[7] Delete Participants
[8] Display Participants for an Event
[9] Exit System
"""

# File to store all data
events_file = "events_data.json"
eventsTemp_file = "eventsTemp_data.json"
eventsIDTemp_file = "eventsIDTemp_data.json"

participants_file = "participants_data.json"
participantsTemp_file = "pTemp_data.json"

# Load events and participants data if file exists
# eventsStorage (Stores all the events and its full details)
try:
    with open(events_file, "r") as f:
        eventsStorage = json.load(f)
        f.close()
except FileNotFoundError:
    eventsStorage = []

# eventTempList (Stores event name, reference for eventID())
try:
    with open(eventsTemp_file, "r") as f:
        eventTempList = json.load(f)
        f.close()
except FileNotFoundError:
    eventTempList = []

# eventIDTemp (Stores event ID, for the system to search before updating/removing an event)
try:
    with open(eventsIDTemp_file, "r") as f:
        eventIDTemp = json.load(f)
        f.close()
except FileNotFoundError:
    eventIDTemp = []

# participantsStorage (Stores all participants and its full details)
try:
    with open(participants_file, "r") as f:
        participantsStorage = json.load(f)
        f.close()
except FileNotFoundError:
    participantsStorage = []

# participantsNameTemp (Stores participant name, for reference)
try:
    with open(participantsTemp_file, "r") as f:
        participantNameTemp = json.load(f)
        f.close()
except FileNotFoundError:
    participantNameTemp = []

def save_data():
    with open(events_file, "w") as f:
        json.dump(eventsStorage, f, indent=4)
        f.close()
        
    with open(eventsTemp_file, "w") as f:
        json.dump(eventTempList, f, indent=4)
        f.close()

    with open(eventsIDTemp_file, "w") as f:
        json.dump(eventIDTemp, f, indent=4)
        f.close()

    with open(participants_file, "w") as f:
        json.dump(participantsStorage, f, indent=4)
        f.close()

    with open(participantsTemp_file, "w") as f:
        json.dump(participantNameTemp, f, indent=4)
        f.close()

# ========== Event Registration ========== 

# eventID generator
def eventID():
    i = len(eventTempList)
    evID = 1000 + i
    return f"E{str(evID)}"

# Validate with datetime
def validDate(a):
    try:
        datetime.date.fromisoformat(a)
        return True
    except(ValueError):
        return False

# Add New Event
def addEvent():
    global eventFullList
    eventTuple = ()
    eventList = list(eventTuple)
    break2 = True
    break3 = True
    while True:
        print("[Event name] -> Event date -> Event venue and ticket price")
        inp = input("Enter the name of the event: ").title()
        evName = " ".join(inp.split())
        if len(evName) == 0:
            print("Sorry, you cannot leave a blank input. Please try again.\n")
        elif evName == 'Cancel':
            print("Returning to menu...")
            break
        else:
            eventTempList.append(evName)
            eventIDTemp.append(eventID())
            eventList.append(eventID())
            eventList.append(evName)
            break2 = False
            print(f"Event successfully added and is assigned to ID: {eventID()}\n")
            break

    while break2 == False:
        print("Event name -> [Event date] -> Event venue and ticket price")
        evYear = input("Enter the year for the event: ")
        if evYear == "cancel":
            eventList.remove(eventID())
            eventList.remove(evName)
            eventTempList.remove(evName)
            print("Returning to menu...")
            break
        evMonth = input("Enter the month for the event: ")
        if evMonth == "cancel":
            eventList.remove(eventID())
            eventList.remove(evName)
            eventTempList.remove(evName)
            print("Returning to menu...")
            break
        evDay = input("Enter the day for the event: ")
        if evDay == "cancel":
            print("Returning to menu...")
            break
        evDate = f"{evYear}-{evMonth}-{evDay}"
        if validDate(evDate) == False:
            print("Invalid date format. Please try again.\n")
        else:
            eventList.append(evDate)
            print("Event date successfully assigned!\n")
            break3 = False
            break

    while break3 == False:
        print("Event name -> Event date -> [Event venue and ticket price]")
        venue = input("Enter the venue name for the event: ").title()
        if venue == "Cancel":
            eventList.remove(eventID())
            eventList.remove(evName)
            eventTempList.remove(evName)
            eventList.remove(evDate)
            print("Returning to menu...")
            break
        ticketPrice = input("Enter the ticket price for the event: ")
        if ticketPrice == "cancel":
            eventList.remove(eventID())
            eventList.remove(evName)
            eventTempList.remove(evName)
            eventList.remove(evDate)
            print("Returning to menu...")
            break
        elif len(venue) == 0 or len(ticketPrice) == 0:
            print("Sorry, you cannot leave a blank input. Please try again.")
        else:
            try:
                eventList.append(venue)
                eventList.append(f"{float(ticketPrice):.2f}")
                print("Venue and ticket price successfully assigned!\n")
                print("Storing all information into system...")
                eventFullList = tuple(eventList)
                eventDictionary = {}
                eventDictionary["Event ID"] = eventFullList[0]
                eventDictionary["Name"] = eventFullList[1]
                eventDictionary["Date"] = eventFullList[2]
                eventDictionary["Venue"] = eventFullList[3]
                eventDictionary["Ticket Price"] = f"RM{str(eventFullList[4])}"
                eventsStorage.append(eventDictionary)
                
                print("New event successfully stored into the system!\n")
                print(f"ID: {eventDictionary["Event ID"]} | Event Name: {eventDictionary["Name"]} | "
                      f"Date: {eventDictionary["Date"]} | Venue: {eventDictionary["Venue"]} | "
                      f"Ticket Price: {eventDictionary["Ticket Price"]}\n")
                break
            except(ValueError):
                eventList.remove(venue)
                print("Error! Please try again and only input numbers for the ticket price.\n")

# Update an Event
def updateEvent():
    break_all = False
    while break_all == False:
        upd = str(input("Enter the event ID of an event that you want to update: ")).upper()
        if upd in eventIDTemp:
            updIndex = eventIDTemp.index(upd)
            update = input(f"Editing: {upd} | Which one do you want to update? (name/date/venue/pricing): ").lower()
            if update == "name":
                while True:
                    updName = input("Enter the updated event name: ").title()
                    newName = " ".join(updName.split())
                    if newName == "Cancel":
                        print("Returning to menu...")
                        break_all = True
                        break
                    elif len(newName) != 0:
                        eventsStorage[updIndex]["Name"] = newName
                        print(f"Event name for {upd} has been successfully updated!")
                        break_all = True
                        break
                    else:
                        print("Sorry, you cannot leave a blank input. Please try again.\n")
            elif update == "date":
                while True:
                    newYear = input("Enter the updated year for the event: ")
                    if newYear == "cancel":
                        print("Returning to menu...")
                        break_all = True
                        break
                    newMonth = input("Enter the updated month for the event: ")
                    if newMonth == "cancel":
                        print("Returning to menu...")
                        break_all = True
                        break
                    newDay = input("Enter the updated day for the event: ")
                    if newDay == "cancel":
                        print("Returning to menu...")
                        break_all = True
                        break
                    newDate = f"{newYear}-{newMonth}-{newDay}"
                    if validDate(newDate) == False:
                        print("Invalid date format. Please try again.\n")
                    else:
                        eventsStorage[updIndex]["Date"] = newDate
                        print(f"Event date for {upd} has been successfully updated!")
                        break_all = True
                        break
            elif update == "venue":
                while True:
                    updVenue = input("Enter the updated event venue: ").title()
                    if updVenue == "Cancel":
                        print("Returning to menu...")
                        break_all = True
                        break
                    elif len(updVenue) != 0:
                        eventsStorage[updIndex]["Venue"] = updVenue
                        print(f"Event venue for {upd} has been successfully updated!")
                        break_all = True
                        break
                    else:
                        print("Sorry, you cannot leave a blank input. Please try again.\n")
            elif update == "pricing":
                while True:
                    updPrice = input("Enter the updated event ticket price: ")
                    if updPrice == "Cancel":
                        print("Returning to menu...")
                        break_all = True
                        break
                    elif len(updPrice) == 0:
                        print("Sorry, you cannot leave a blank input. Please try again.\n")
                    else:
                        try:
                            newPrice = f"{float(updPrice):.2f}"
                            eventsStorage[updIndex]["Ticket Price"] = f"RM{str(newPrice)}"
                            print(f"Ticket price for {upd} has been successfully updated!")
                            break_all = True
                            break
                        except (ValueError):
                            print("Error! Please try again and only input numbers for the ticket price.\n")
            elif update == "cancel":
                print("Returning to menu...")
                break
            else:
                print("Invalid choice, please try again.\n") 
        elif upd == "CANCEL":
            print("Returning to menu...")
            break
        else:
            print("Event ID not found! Please try again.\n")

# Delete an event
def deleteEvent():
    break_all = False
    while break_all == False:
        delEvent = str(input("Enter the event ID of an event that you want to delete: ")).upper()
        if delEvent in eventIDTemp:
            while True:
                indexref = eventIDTemp.index(delEvent)
                ref = eventsStorage[indexref]
                print(f"\n{ref}")
                confirm = input("Are you sure you want to delete this event? (Y/N): ").upper()
                if confirm == "Y":
                    eventIDTemp.pop(indexref)
                    eventTempList.pop(indexref)
                    eventsStorage.pop(indexref)
                    print(f"Event from ID: {delEvent} has been deleted successfully.")
                    break_all = True
                    break
                elif confirm == "N":
                    print("Returning to menu...")
                    break_all = True
                    break
                else:
                    print("Invalid input, please try again.\n")
        elif delEvent == "CANCEL":
            print("Returning to menu...")
            break
        else:
            print("Event ID not found! Please try again.\n")


# View all events
def viewEvents():
    print("\n[Full list of Events]")
    for i, info in enumerate(eventsStorage):
        print(f"({i+1}) Event ID: {info['Event ID']} | Name: {info['Name']} | Date: {info['Date']} | Venue: {info['Venue']} | Ticket Price: {info['Ticket Price']}")

# ========== Participant Registration ========== 

# Receipt Generation
def generate_receipt(event, name, vip, tickets, totalcost):
    # Serial number for receipt reference
    serialno = random.randint(1000000,9999999)
    # Formated datetime
    timenow = datetime.datetime.today().strftime("%I:%M %p")
    datenow = datetime.date.today().strftime("%d-%m-%Y")

    evindex = eventIDTemp.index(event)
    eventName = eventsStorage[evindex]["Name"]
    with open(f"receipt.txt", "a") as f:
        f.write(f"---- Ticket Receipt as of {datenow}, {timenow} ----\n")
        f.write(f"Serial No.: ES{serialno}\n")
        f.write(f"Event: {event} - {eventName}\n")
        f.write(f"Participant: {name}\n")
        f.write(f"VIP Status: {vip}\n")
        f.write(f"Tickets: {tickets}\n")
        f.write(f"Total Cost: {totalcost}\n")
        f.write("\n")
    print("Receipt generated: receipt.txt")

# Add Participant
def add_participant():
    participant = {}

    while True:
        name = input("Enter participant name: ").upper()
        if name.lower() == "cancel":
            print("Returning to menu...\n")
            return
        elif len(name) == 0:
            print("Sorry, you cannot leave a blank space. Try again.\n")
        else:
            participantNameTemp.append(name)
            participant["Name"] = name
            break

    while True:
        evID = input("Enter Event ID to register for: ").upper()
        if evID.lower() == "cancel":
            print("Returning to menu...\n")
            return
        elif evID not in eventIDTemp:
            print("Event ID not found. Try again.\n")
        else:
            participant["Event ID"] = evID
            break

    while True:
        tickets = input("Enter number of ticket(s): ")
        if tickets.lower() == "cancel":
            print("Returning to menu...\n")
            return
        try:
            tickets = int(tickets)
            if tickets <= 0:
                print("Please enter a valid positive number.\n")
            else:
                participant["Tickets"] = tickets
                break
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")

    evIndex = eventIDTemp.index(participant["Event ID"])
    ticket_price_str = str(eventsStorage[evIndex]["Ticket Price"]).replace("RM", "")
    ticket_price = float(ticket_price_str)
    total_cost = ticket_price * tickets

    if tickets > 3 and total_cost < 50.00:
        participant["VIP Status"] = True
        stat = True
        total_cost *= 0.9  # 10% discount
        participant["Total Cost"] = f"RM{total_cost:.2f}"
    else:
        participant["VIP Status"] = False
        stat = False
        participant["Total Cost"] = f"RM{total_cost:.2f}"

    participantsStorage.append(participant)

    print("\nParticipant successfully registered!")
    print(f"Name: {participant['Name']} | Event ID: {participant['Event ID']} | "
          f"Tickets: {participant['Tickets']} | Total Cost: {participant['Total Cost']} | "
          f"VIP Status: {participant['VIP Status']}\n")
    
    generate_receipt(evID, name, stat, tickets, f"RM{total_cost:.2f}")

# Update Partipant's Details
def updateParticipant():
    while True:
        upd = input("Enter the name of the participant that you want to update: ").upper()
        if upd in participantNameTemp:
            updIndex = participantNameTemp.index(upd)
            break
        elif upd == "CANCEL":
            print("Returning to menu...")
            return
        else:
            print("Participant name not found. Please try again.")
    
    while True:
        updselect = input(f"Editing: {upd} | Which one do you want to update? (name/event/ticket): ").lower()
        if updselect == "name" or updselect == "event" or updselect == "ticket":
            break
        elif updselect == "cancel":
            print("Returning to menu...")
            return
        else:
            print("Invalid input. Please try again.")

    if updselect == "name":
        while True:
            name = input("Enter the updated name: ").upper()
            if name.lower() == "cancel":
                print("Returning to menu...\n")
                return
            elif len(name) == 0:
                print("Sorry, you cannot leave a blank space. Try again.\n")
            else:
                participantNameTemp.append(name)
                participantsStorage[updIndex]["Name"] = name
                print(f"Participant '{upd}' has been successfully updated to '{name}'!")
                break
    elif updselect == "event":
        while True:
            event = input("Enter the updated event ID: ").upper()
            if event == "CANCEL":
                print("Returning to menu...")
                return
            elif event in eventIDTemp:
                for ref in participantsStorage:
                    if ref['Name'] == upd:
                        ref['Event ID'] = event
                        evIndex = eventIDTemp.index(ref["Event ID"])
                        ticket_price_str = str(eventsStorage[evIndex]["Ticket Price"]).replace("RM", "")
                        ticket_price = float(ticket_price_str)
                        total_cost = ticket_price * ref['Tickets']

                        if ref['Tickets'] > 3 and total_cost < 50.00:
                            ref["VIP Status"] = True
                            total_cost *= 0.9  # 10% discount
                            ref["Total Cost"] = f"RM{total_cost:.2f}"
                        else:
                            ref["VIP Status"] = False
                            ref["Total Cost"] = f"RM{total_cost:.2f}"
                print(f"Event ID for {upd} has been successfully updated!")
                break
            else:
                print("Sorry, event ID not found. Please try again.")
    elif updselect == "ticket":
        while True:
            ticket = input("Enter the updated number of ticket(s): ")
            if ticket.lower() == "cancel":
                print("Returning to menu...\n")
                return
            try:
                ticket = int(ticket)
                if ticket <= 0:
                    print("Please enter a valid positive number.\n")
                else:
                    for ref in participantsStorage:
                        if ref['Name'] == upd:
                            ref['Tickets'] = ticket
                            evIndex = eventIDTemp.index(ref["Event ID"])
                            ticket_price_str = str(eventsStorage[evIndex]["Ticket Price"]).replace("RM", "")
                            ticket_price = float(ticket_price_str)
                            total_cost = ticket_price * ticket

                            if ref['Tickets'] > 3 and total_cost < 50.00:
                                ref["VIP Status"] = True
                                total_cost *= 0.9  # 10% discount
                                ref["Total Cost"] = f"RM{total_cost:.2f}"
                            else:
                                ref["VIP Status"] = False
                                ref["Total Cost"] = f"RM{total_cost:.2f}"
                    print(f"Number of ticket(s) for {upd} has been successfully updated!")
                    break
            except ValueError:
                print("Invalid input! Please enter numbers only.\n")

# Delete Participant
def deleteParticipant():
    while True:
        delete = input("Enter the name of the participant that you want to delete: ").upper()
        if delete in participantNameTemp:
            while True:
                indexref = participantNameTemp.index(delete)
                ref = participantsStorage[indexref]
                print(f"\n{ref}")
                confirm = input(f"Are you sure you want to delete this participant? (Y/N): ").upper()
                if confirm == "Y":
                    participantsStorage.pop(indexref)
                    participantNameTemp.pop(indexref)
                    print(f"Participant '{delete}' has been deleted successfully.")
                    return
                elif confirm == "N":
                    print("Returning to menu...")
                    return
                else:
                    print("Invalid input. Please try again.")
        elif delete == "CANCEL":
            print("Returning to menu...")
            return
        else:
            print("Sorry, participant not found. Please try again.")

# Display participants for an Event
def viewParticipants():
    while True:
        evID = input("Enter Event ID to view participants: ").upper()

        if evID.lower() == "cancel":
            print("Returning to menu...")
            return
        elif evID in eventIDTemp:
            print(f"\nParticipants Registered for Event {evID}:\n")
            i = 1
            for info in participantsStorage:
                if info["Event ID"] == evID:
                    print(f"[{i}] Name: {info['Name']} | Total Ticket(s): {info['Tickets']} | Total Ticket Cost: {info['Total Cost']} | VIP Status: {info['VIP Status']}")
                    i += 1
            break
        else:
            print("Sorry, event ID not found. Please try again.")
    

while True:
    print(menu + "\n")
    select = str(input("Choose an option (1-9): "))
    if select == "1":
        print("\nSelected: [1] Add New Event, type 'cancel' anytime to abort.\n")
        addEvent()
    elif select == "2":
        print("\nSelected: [2] Update Event, type 'cancel' anytime to abort.\n")
        updateEvent()
    elif select == "3":
        print("\nSelected: [3] Delete, type 'cancel' to abort.\n")
        deleteEvent()
    elif select == "4":
        if len(eventsStorage) >= 2:
            viewEvents()
        else:
            print("Sorry, insufficient amount of data to be displayed. Please add atleast 2 events and try again.")
    elif select == "5":
        print("\nSelected: [5] Add New Participant, type 'cancel' anytime to abort.\n")
        add_participant()
    elif select == "6":
        print("\nSelected: [6] Update Participant's Details, type 'cancel' anytime to abort.\n")
        updateParticipant()
    elif select == "7":
        deleteParticipant()
    elif select == "8":
        print("\nSelected: [8] Display Participants for an Event, type 'cancel' anytime to abort.\n")
        viewParticipants()
    elif select == "9":
        save_data()
        print("Saving all data and exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
