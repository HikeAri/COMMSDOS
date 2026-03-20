import time
from time import sleep
import sys

print("🔐 Welcome to the Haunted House Escape Room Challenge! 🔐")

while True:  # main game loop
    print("\nChoose a level to play:")
    print("\n1. Easy (Level 1 Example)")
    print("2. Medium (Level 2)")
    print("3. Hard (Level 3)")
    print("4. Immersive mode (Level 4)")
    print("5. Exit Game")

    choice = input("\nEnter your choice (1-5): ")

    # ---------------- Level 1 (Example, DO NOT EDIT) ----------------
    if choice == "1":
        while True:  # level loop
            print("\n---------------- Level 1 ----------------")
            print("\nYou wake up in a dark, locked room.")
            print("There is a dusty box on the table. You think it might have a key inside...")
            print("On the wall, you notice some numbers scratched faintly: 7 4 5")
            print("Maybe it's the combination to the box lock?")

            code = int(input("\nEnter the 3-digit combination to unlock the box: "))

            if code == 745:  # correct code
                print("\n✅ T he box clicks open! Inside you find a shiny key...")
                print("\nYou try it on the door, and it unlocks. 🎉 YOU ESCAPED LEVEL 1!")
                print("\n🔙  Returning to main menu...")
                break  # success → back to menu
            else:
                print("\n❌ T he box stays locked. The lights flicker and a cold wind blows...")
                print("It seems you entered the wrong code. Try again carefully.")
                retry = input("\nDo you want to try again? (yes/no): ")
                if retry.lower() != "yes":
                    print("\n🔙  Returning to main menu...")
                    break
                # if yes → loop continues, restart Level 1

    # ---------------- Level 2 (Students create puzzle) ----------------
    elif choice == "2":
        while True:
            print("\n---------------- Level 2 ----------------")
            print("\n There is a house in the dark of the forest---")
            print("\n You tried to sneak to the house through the door---")
            print("\n Suddenly the door close itself once you enter the house !")
            print("\n You tried to open the door but it stuck---")
            print("\n There was a key hole that needs a special key")
            print("\n You found a secret door inside the house")
            print("\n but there was a question...")

            riddle = input("\n 'What would you find in the middle of house?'")  # riddle

            if riddle.lower() == "the letter u" or riddle.lower() == "u" or riddle.lower() == "letter u" or riddle.lower() == "a letter u":  # answer
                print("\n The door is open and you get a key inside the room")
                print("\n The ghost is chasing you!, hurry up and use the key to unlock the main door!")
                print("\n You win the level 2!")  # win
                break

            else:
                print("Your answer is wrong! THE GHOST FOUND YOU!")  # lose
                break

    # ---------------- Level 3 (Students create puzzle) ----------------
    elif choice == "3":
        while True:
            print("---------------- Level 3 ----------------")
            print("You are trapped in a haunted house.")
            print("You wake up in a room with stained blood all over the place.")
            print("""There are 3 doors in front of you, the first one has a weird smell,
            second one has dried puddle of blood on the floor and the third one has an ominous atmosphere""")
            a1 = input("Choose a door [first/second/third]: ")
            if a1.lower() == "first":
                print("Upon entering the first door, you see a bunch of piled meat on the ground.")
                print("A bloody figure sees you enter the room, and immediately chased you.")
                print("You became it's next victim!")
                r1 = input("Do you want to try again? (Y/N): ")
                if r1.lower() != "y":
                    print("Returning to main menu...")
                    break
            elif a1.lower() == "second":
                print("upon entering the second door, you see a silhouette.")
                print("Suddenly, a dark figure starts chasing you.")
                print("You've been caught!")
                r2 = input("Do you want to try again? (Y/N): ")
                if r2.lower() != "y":
                    print("Returning to main menu...")
                    break
            elif a1.lower() == "third":
                print("Upon entering the third door, you continue on a narrow hallway...")
                print("As you walk in, you found yourself in a puzzle room.")
                print(
                    "The wall has a text scribbled on it, saying \"Choose an animal that is considered a predator\". ")
                print("On the same wall, there are 3 buttons are labelled 'Wolf', 'Cheetah', 'Rabbit' ")
                a2 = input("Choose a button: ")
                if a2.lower() == "wolf" or a2.lower() == "cheetah":
                    print("A hidden door is unlocked.")
                    print("You rush through it and escaped the house!")
                    print("Congratulations, you've won!"), time.sleep(2)
                    break
                else:
                    print("Unfortunately, that's the incorrect button. A hidden trap opens below you and you fell.")
                    r3 = input("Do you want to try again? (Y/N): ")
                    if r3.lower() != "y":
                        print("Returning to main menu...")
                        break
            else:
                print("Invalid input!")

    # ---------------- Level 4 (Students create puzzle) ----------------
    elif choice == "4":
        print("\n\n\n--- Level 4: Immersive Mode ---")
        time.sleep(0.5)
        print("""\033[33mNote: In this level, you are required to input something inside a file.
        The file should be named 'code_input.txt' and is already created inside the coding file.
        Lastly, look out for 'Journal Entries'. You should be able to see the written entry inside
        a file named 'journal.txt'. A message should be shown to inform you that the journal has updated.
        Close and reopen the file to see the updated entries.\n""")
        time.sleep(1.5)
        print("\033[32mGood luck and have fun!\n")
        time.sleep(2)

        while True:
            p1 = "\n\n\033[39m=--------------= LEVEL 4 =--------------=\n"
            for x in p1:
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
            time.sleep(0.5)
            print(
                "\033[36mYou wake up on a dark room filled with insects. Beside you is an empty journal."), time.sleep(
                1)
            print("You quickly grab it then head outside the room, only to stumble upon two doors ."), time.sleep(1)
            # Journal Entry Update 1
            with open("journal.txt", "w") as file:
                file.write("Note #1\n")
                file.write("To anybody who reads this, find a way to escape.\n")
                file.write("121998 is the code for-")

            print("\033[33m[ <!> Journal Entry Updated ]"), time.sleep(0.5)
            print("\033[36mBoth doors are locked, and you found a note laying on the floor."), time.sleep(1)
            while True:
                in1 = input("\033[34m[Try the first door / Try the second door]:\033[39m ")
                if in1.lower() == "try the first door" or in1.lower() == "try the second door":
                    break
                else:
                    print("\033[31m[ <!> Invalid Input ]")

            if in1.lower() == "try the first door":
                print("\033[36mThere seems to be a 6-digit lock combination."), time.sleep(1)
                input("\033[34mEnter the code: ")
                print("\033[36mUh oh, seems like the code is for another door."), time.sleep(1)
                in2 = input("\033[33mDo you want to try again? (Y/N): ")
                if in2.lower() != "y":
                    print("-Returning to the main menu-\n\n\033[39m"), time.sleep(1)
                    break
            elif in1.lower() == "try the second door":
                print("\033[36mYou decided to try the second door instead."), time.sleep(1)
                print("There seems to be a 6-digit lock combination."), time.sleep(1)
                in3 = int(input("\033[34mEnter the code: "))
                if in3 == 121998:
                    print("\033[36mYou put in the code and the door is now unlocked."), time.sleep(1)
                    print("Going inside, you are greeted with a small living room.")
                    # Journal Entry Update 2
                    with open("journal.txt", "a") as file:
                        file.write("\n\nNote #2\n")
                        file.write("Triangle represents 5\n")
                        file.write("Square represents 2\n")
                        file.write("Circle represents 6")

                    print("\033[33m[ <!> Journal Entry Updated ]"), time.sleep(0.5)
                    print("\033[36mYou search the coffee table and found a crumbled piece of note."), time.sleep(1)
                    print("Without wasting any time, you take the staircase and encounter a puzzle."), time.sleep(1)
                    print(
                        "There are two podiums and a question written on the wall. On your side is a table with small wooden ")
                    print("statues that are shaped like a dog, a cat, a cow, and a rabbit"), time.sleep(1)
                    print(
                        "The question reads, \"We are very useful, but only have impacts on your emotions.\""), time.sleep(
                        1)
                    print("\033[34m[Put one statue on each podiums by typing the animal name]")
                    inp4 = input("Podium 1 [Dog/Cat]: ")
                    inp5 = input("Podium 2 [Cow/Rabbit]: ")
                    if inp4.lower() == "cat" and inp5.lower() == "rabbit":
                        print("\033[36mYou heard some kind of a click sound."), time.sleep(1)
                        print(
                            "The wall on your right opens up, and you head towards it, meeting a narrow hallway."), time.sleep(
                            1)
                        print("You stumble upon three doors, right is silent, middle has some kind of weird smell, ")
                        print("and left has a dried puddle of blood on the floor."), time.sleep(1)
                        in6 = input("\033[34m[Choose a door; right, middle, or left]: ")
                        if in6 == "left":
                            print(
                                "\033[36mUpon entering the left door, you suddenly feel a hand grabbing you into the room."), time.sleep(
                                1)
                            print("You have been consumed by the darkness."), time.sleep(1)
                            in2 = input("\033[33mDo you want to try again? (Y/N): ")
                            if in2.lower() != "y":
                                print("-Returning to the main menu-\n\n\033[39m"), time.sleep(1)
                                break
                        elif in6 == "right" or in6 == "middle":
                            while True:
                                if in6 == "right":
                                    print("\033[36mYou decided to go inside the right room. ")
                                    break
                                elif in6 == "middle":
                                    print(
                                        "\033[36mUpon opening the middle door, you found out that it is a built-in closet."), time.sleep(
                                        1)
                                    # Create card.txt
                                    with open("card.txt", "w") as file:
                                        file.write("[Erase then type your code here]")
                                    # Journal Entry Update 3
                                    with open("journal.txt", "a") as file:
                                        file.write("\n\nNote #3\n")
                                        file.write("The code for the second door is written in a MM/YYYY format.\n")
                                        file.write("Write the year on the card. (modify the card.txt file)\n")
                                        file.write("Avoid going inside the left room.")

                                    print("\033[33m[ <!> Journal Entry Updated ]"), time.sleep(0.5)
                                    print("\033[36mInside the closet is a blank card and a note."), time.sleep(1)
                                    print("You then proceed to enter the right room."), time.sleep(1)
                                    break
                            print(
                                "\033[36mYou are greeted with another door, this time with a keypad and a card reader."), time.sleep(
                                1)
                            print(
                                "The wall is scribbled with shapes; 3 squares, 4 triangles, and 1 semicircle"), time.sleep(
                                1)
                            print("After a minute, you decided to try unlocking the door.")
                            in7 = int(input("\033[34mKeypad (integers only): "))
                            if in7 == 29:
                                with open("card.txt", "r") as file:
                                    card = int(file.read())

                                if card == 1998:
                                    print(
                                        "\033[36mThe code and card is accepted, and the door is now unlocked, revealing the outside."), time.sleep(
                                        1)
                                    print("You quickly get out of the house."), time.sleep(1)
                                    print("\033[32mCongratulations! You've escaped the house!\n\n\033[39m"), time.sleep(2)
                                    break
                                else:
                                    print("\033[36mUh oh, seems like the code on your card is incorrect"), time.sleep(1)
                                    in2 = input("\033[33mDo you want to try again? (Y/N): ")
                                    if in2.lower() != "y":
                                        print("-Returning to the main menu-\n\n\033[39m"), time.sleep(1)
                                        break
                            else:
                                print("\033[36mUh oh, seems like the code is incorrect"), time.sleep(1)
                                in2 = input("\033[33mDo you want to try again? (Y/N): ")
                                if in2.lower() != "y":
                                    print("-Returning to the main menu-\n\n\033[39m"), time.sleep(1)
                                    break

                    else:
                        print("\033[36mUh oh, seems like it's incorrect"), time.sleep(1)
                        in2 = input("\033[33mDo you want to try again? (Y/N): ")
                        if in2.lower() != "y":
                            print("-Returning to the main menu-\n\n\033[39m"), time.sleep(1)
                            break
                else:
                    print("\033[36mUh oh, seems like the code is incorrect."), time.sleep(1)
                    in2 = input("\033[33mDo you want to try again? (Y/N): ")
                    if in2.lower() != "y":
                        print("-Returning to the main menu-\n\n\033[39m"), time.sleep(1)
                        break

    # ---------------- Exit ----------------
    elif choice == "5":
        print("\nThanks for playing! Goodbye 👋")
        break

    else:
        print("\n❌ Invalid choice. Please try again.")
