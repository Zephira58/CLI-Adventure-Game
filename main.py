

from colorama import Fore, Back, Style
from playsound import playsound
from threading import Thread
import keyboard, time, os, requests, random, sys

def t5():
    time.sleep(.5)

def t():
    time.sleep(5)

def cls():
    os.system('cls||clear')

def enter():
    print("\n")

def tc():
    time.sleep(5)
    os.system('cls||clear')

def intro():
    print("")

def credits():
    cls()
    print("Made by Xanthus In my spare time")
    enter()
    print("Check out my other works at https://github.com/Xanthus58")
    enter()
    print("Email me on 'Xanthus58@protonmail.com'")
    enter()
    print("Feel free to fork; submit issues; and otherwise interact with the project here!")
    print("https://github.com/Xanthus58/CLI-Adventure-Game")
    enter()
    input("Press Enter to return to the main menu: ")
    cls()
    intro()

def scroll(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.03)

cellactions = ["inv","Inv","Inventory","inventory","help","Help","Lamp","lamp","Look","look","Search","search","bed","Bed","Use","use","Drink", "drink","Bucket","bucket","Gate","gate","escape","Escape"]
#-Helplist-
Cellarhelplist = ["> Lamp\n","> Bed\n","> Bucket\n","> Gate\n",]
#-Inventory-
lamp = 0
CellKey = 0
#-Code-
cls()
scroll("You slowly awaken to the moist sounds of water dripping onto stone; the roar of thunder is deafening\n")
t5()
scroll("It's dark, but you can see from the dimly lit lamp in the corner that you are in a dungeon.\n")
t5()
scroll("What do you do: ")
response = input()

while True:

    actions = ["inv","Inv","Inventory","inventory"]
    for x in actions:
        if x in response:
            cls()
            scroll("-Items-\n")
            if lamp == 1:
                scroll("> Lamp\n")
            if CellKey == 1:
                scroll("> Cell Key\n")
            scroll("What do you do: ")
            response = input()

    actions = ["help","Help"]
    for x in actions:
        if response in x:
            for x in Cellarhelplist:
                cls()
                scroll("Thease are the items/actions you can perform and interact with. In this room\n")
                scroll(Cellarhelplist)
                scroll("What do you do: ")
                response = input()
                break
                
    actions = ["Lamp","lamp"]
    for x in actions:
        if lamp == 0:
            if x in response:
                cls()
                scroll("You move closer to the lamp it's dim light makes it easier to see.\n")
                t5()
                scroll("You grab the lamp; the subtle warmth makes you feel at ease.\n")
                scroll("You found a "+Fore.YELLOW+"Lamp!\n"+Fore.WHITE)
                lamp = 1
                scroll("What do you do: ")
                response = input()
                
    actions = ["Look","look","Search","search"]
    for x in actions:
        if x in response:
            cls()
            scroll("You're in A dark moist dungeon. The sounds of water hitting stone echos troughout the halls\n")
            scroll("Theres an iron gate in front of you; too tight to squeeze trough.\nTheres a small bed made of hay in the corner of the room\n")
            if lamp == 1:
                scroll("With the light of the lamp you can see a brown bucket; filld with a discusting mixture of brown sludge and yellow water\n")
            else:
                scroll("You see a bucket by your bed; but its to dark to make out whats inside of it.\n")
                scroll("You also see a dimly lit lamp in the corner of the cell\n")
            scroll("What do you do: ")
            response = input()
            
    actions = ["bed","Bed"]
    for x in actions:
        if CellKey == 0:
            if x in response:
                cls()
                scroll("You lay down on the bed it's uncomfterble.\n")
                scroll("As you take a deep breath laying on the bed; you feel a sharp pain stabbing into your back\n")
                scroll("You get out of the bed and feel around the hay pile.. You found a "+Fore.YELLOW +"Cell Key!\n"+Fore.WHITE)
                CellKey = 1
                scroll("What do you do: ")
                response = input()
         
        elif CellKey == 1:
            if x in response:
                cls()
                scroll("You lay onto the bed; its still as uncomfterble as you remember.\n")
                scroll("You're eyes grow heavy, and you slowly drift off into sleep\n")
                scroll("You slowly awaken; its still the same dark cell you went to sleep in. \n")
                scroll("What do you do: ")
                response = input()
            
    actions = ["Use","use"]
    for x in actions:
        if x in response:
            cls()
            scroll("You can not use this at this time.\n")
            scroll("What do you do: ")
            input()
            
    actions = ["Drink", "drink","Bucket","bucket"]
    for x in actions:
        if x in response:
            cls()
            scroll("You pick up the bucket, it smeels like rot.\n")
            scroll("You take a deep breath and gulp down the contents of the bucket\n")
            scroll("You collapse onto the floor, vomiting. As death firmly graps you.\n")
            scroll(Fore.RED+"You have perrished. Please try again"+Fore.WHITE)
            t()
            credits()
            os._exit()

    actions = ["Gate","gate","escape","Escape"]
    for x in actions:
        if CellKey == 1:
            if x in response:
                cls()
                scroll("You use the key to unlock the cell gate and step outside \n")
                CellKey = 0
                scroll(Fore.GREEN+"Succsess you beat the demo! Please tell me what you think! as this is only a proof of concept."+Fore.WHITE)
                t()
                credits()
                os._exit()

        elif CellKey == 0:
            if x in response:
                cls()
                scroll("The gate is locked shut no amount of bashing; pulling; and punching will open it. There must be another way\n")
                scroll("What do you do: ")
                response = input()

    if response != "inv" and response != "Inv" and response != "Inventory" and response != "inventory" and response != "help" and response != "Help" and response != "Lamp" and response != "lamp" and response != "Look" and response != "look" and response != "Search" and response != "search" and response != "bed" and response != "Bed" and response != "Use" and response != "use" and response != "Drink" and response !=  "drink" and response != "Bucket" and response != "bucket" and response != "Gate" and response != "gate" and response != "escape" and response != "Escape":
        cls()
        scroll(Fore.RED+ "Invalid Input; please enter again.\n"+Fore.WHITE)
        scroll("What do you do: ")
        response = input()
        print(response) 
   