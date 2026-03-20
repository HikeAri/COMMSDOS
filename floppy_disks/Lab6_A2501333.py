menu = """\n
=== Student Information Manager ===
[1] Add a student
[2] Update student info
[3] View all students
[4] Exit program
"""

# Store student names for generating student ID
studentName = []

# For the program to be able to search for student IDs
studIDTemp = []

# Store full student info from studDictionary into a list
studFullList = []

def studentID():
    a = len(studentName)
    no = 250000 + a
    return str(no)

def addStudent():
    global studentFullInfo
    break2 = True
    break3 = True
    while True:
        # StudentID , Name
        name = input("Enter the student's name: ").title()
        if len(name) == 0:
            print("Sorry, you cannot leave a blank input. Please try again.")
        elif name == 'Cancel':
            print("Returning to menu...")
            break
        elif name in studentName:
            print("Sorry, it seems like the student is already added into the list. Please try again.")
        else:
            studentName.append(name)
            studentFullInfo.append(studentID())
            studentFullInfo.append(name)
            studentList = tuple(studentFullInfo)
            studIDTemp.append(studentID())
            print(f"'{name}' successfully added and is assigned to ID: {studentID()}")
            break2 = False
            break
    
    # Birthdate
    while break2 == False:
        birthyear = str(input("Enter the student's birth year: "))
        birthmonth = str(input("Enter the student's birth month: "))
        birthday = str(input("Enter the student's birth day: "))

        if birthyear == 'cancel' or birthmonth == 'cancel' or birthday == 'cancel':
            print("Aborting all operations...")
            studIDTemp.remove(studentID())
            studentList = list(studentFullInfo)
            studentList.remove(studentID())
            studentName.remove(name)
            studentList.remove(name)
            studentFullInfo = tuple(studentList)
            print("Returning to menu...")
            break
        elif birthyear.isdigit() == True and birthmonth.isdigit() == True and birthday.isdigit() == True:
            studentBD = ()
            birthdate = list(studentBD)
            birthdate.append(birthyear)
            birthdate.append(birthmonth)
            birthdate.append(birthday)
            studentBD = tuple(birthdate)
            studentList = list(studentFullInfo)
            studentList.append(studentBD)
            studentFullInfo = tuple(studentList)
            print("Birthdate successfully assigned!")
            break3 = False
            break    
        else:
            print("Sorry, invalid birthdate. Please try again.")

    # Course, CGPA
    while break3 == False:
        course = input("Enter the student's course: ").upper()
        cgpa = input("Enter the student's CGPA: ")

        if course == 'CANCEL' or cgpa == 'cancel':
            print("Aborting all operations...")
            studIDTemp.remove(studentID())
            studentList = list(studentFullInfo)
            studentList.remove(studentID())
            studentName.remove(name)
            studentList.remove(name)
            studentList.remove(studentBD)
            studentFullInfo = tuple(studentList)
            print("Returning to menu...")
            break
        elif len(course) == 0 or len(cgpa) == 0:
            print("Sorry, you cannot leave a blank input. Please try again.")
        else:
            try:
                studDictionary = {}
                studDictionary["ID"] = studentFullInfo[0]
                studDictionary["Name"] = studentFullInfo[1]
                studDictionary["DOB"] = studentFullInfo[2]
                studDictionary["Course"] = course
                studDictionary["CGPA"] = float(cgpa)
                print("Student information stored successfully!")
                studFullList.append(studDictionary)
                break
            except(ValueError):
                print("Error! Please input a number for CGPA and please try again.")

def editStudent():
    while True:
        updID = input("Enter the student ID that you want to update: ")
        if updID == 'cancel':
            print("Returning to menu...")
            break
        if updID in studIDTemp:
            index = studIDTemp.index(updID)
            update = input(f"Editing: {updID} | Which one do you want to update? (Course/CGPA): ").lower()
            if update == 'course':
                courseUpd = input("Enter the updated course: ").upper()
                if courseUpd == 'CANCEL':
                    print("Returning to menu....")
                    break
                elif len(courseUpd) != 0:
                    studFullList[index]['Course'] = courseUpd
                    print(f"Course for {updID} has been successfully updated!")
                    break
                else:
                    print("Sorry, you cannot leave a blank input. Please try again.")
            elif update == 'cgpa':
                cgpaUpd = input("Enter the updated CGPA: ")
                if cgpaUpd == 'cancel':
                    print("Returning to menu...")
                    break
                elif len(cgpaUpd) != 0:
                    studFullList[index]['CGPA'] = float(cgpaUpd)
                    print(f"CGPA for {updID} has been successfully updated!")
                    break
                else:
                    print("Sorry, you cannot leave a blank input. Please try again.")
            elif update == "cancel":
                print("Returning to menu...")
                break
            else:
                print("Invalid input, please try again.")
        else:
            print("Student not found.")

def viewAll():
    for i, info in enumerate(studFullList):
        print(f"({i+1}) ID: {info['ID']} | Name: {info['Name']} | DOB: {info['DOB']} | Course: {info['Course']} | CGPA: {info['CGPA']}")

while True:
    # Store full info of students
    studentFullInfo = []
    print(menu)
    opt = input(str("Choose an option (1-4): "))
    if opt == "1":
        print("\n Selected: [1] Add a student (Type 'cancel' to abort)")
        addStudent()
    elif opt == "2":
        print("\n Selected: [2] Update student info (Type 'cancel' to abort)")
        editStudent()
    elif opt == "3": 
        if len(studentName) != 0:
            viewAll()
        else:
            print("No student records found.")
    elif opt == "4":
        print("\nExiting Student Information Manager... Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
