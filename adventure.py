__author__ = 'Les Pounder'

"""
    The lines below import modules of code into our game,
    in particular these import time functions allow us to pause and stop the game,
    and random provides a method of choosing random numbers or characters.
"""
from time import *
from random import *
import os,sys
from art import *

"""
    Simple function that clears the terminal screen
"""
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def title():
    print(text2art('Earth', font='alpha'))
    print(text2art('  Lab', font='alpha'))
    print(text2art(' Hero', font='alpha'))

def north():
    print ("To go north press n then enter")

def east():
    print ("To go east press e then enter")

def south():
    print ("to go south press s then enter")

def west():
    print ("To go west press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    global weapons
    global text2art
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name, gingerbread person?")
    #randint is a great way of adding some variety to your players statistics through randomness
    HP = randint(20,50)
    MP = randint(20,50)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,10)
    enemyMP = randint(10,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemynamechoice = ["Chocolate Blob Bob", "Hot Fudge Sludge", "Bad Mad Rad Chocolate Dad", "Annoying Big Ball of Chocolate"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(enemynamechoice)
    enemyname = enemynamechoice [0]
    print ("\nSuddenly you hear a gurgle, and from the shadows you see "+enemyname+" rolling straight at you....")
    #print enemyname
    print (""+enemyname+" has %s Health Points" % str(enemyHP))
    print ("Your enemy has %s Magic Points" % str(enemyMP))


def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global responses
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Beware the chocolate Ogre he haunts this beautiful and delicious town", "Are you a hero?", "There has been a chocolate ogre terrorizing the village"]
    npcnamechoice = ["Oreo", "Hot Sauce", "Sandwich", "Pasta"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the oompa loompa")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)
    print ("If you want to learn more about the chocolate ogre ask the oompa loompa by pressing c and enter. If you want to ignore the oompa loompa and continue on your journey, press i and continue")
    if input() == "c":
        print (""+npcname+" then explains to you how the chocolate ogre is named "+enemyname+" and recently came upon their town and has been sleeping in their sacred chocolate river. He is starting to kill all of his oompa loompa's friends and they are continously begging him to leave but no one is brave enough to stop him. You then explain to him how you will keep a look out and be careful incase you come across the ogre.")
    
    if input() == "i":
        print ("Thanks for the warning, but I'm sure I will be fine.")


"""
    We now use our functions in the game code, we call functions title() and setup() for our character.
"""
clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
enemyname = None
name = None
MP = None
print ("Welcome to the Safe Haven of Delicacies, %s" % name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(HP))
print ("Your magic skill is" + " " + str(MP))



print ("Would you like to venture out into the Haven? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    weapons = []
    weapons.append("baguette")
    weapons.append("pizza")
    weapons.append("marshmallow gun")
    print ("You are in your burger shaped home that you built to express your love for burgers. You are seated in a comfy marshmallow chair with your hot dog dog on your lap. There is a roaring graham cracker fireplace in front of you, and above the fire you can see your baguette, pizza and marshmallow gun.")
    print ("Would you like to take your baguette and pizza or would you like to take your marshmallow gun? To take your baguette and pizza, press y then enter to continue. If you want to take the marshmallow gun press m and enter to continue.")
    weapon = input()
    if weapon == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        print ("You are now carrying your %s and your %s" % (weapons[0], weapons[1]))
        print ("Armed with your %s and %s you swing open the door to your delicious burger home and see a vast vally of licorice string gleaming in the sunshine." % (weapons[0], weapons[1]))
    elif weapon == "m":
        print("debugger")
        print ("You are now carrying your %s" % (weapons[2]))
        print ("Armed with your %s you swing open the door to your delicous burger home and see a vast valley of licorice string gleaming in the sunshine." % (weapons[2]))
    else:
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, You swing open the door to see a green valley full of licorice awaiting you.")
else:
    print ("You stay at home, sat in your favourite marshmallow chair with your hot dog dog watching the fire grow colder. The Safe Haven of Delacacies no longer has a hero.")
    print ("Game Over")
    sys.exit(0)
print ("In the distance to the north you can see a small with little people that you have never gotten a chance to visit, to the east you can see a chocolate river and to the west a field of wild french fries.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A oompa loompa is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou walk to the chocolate river which lies to the east of your home.")
    print ("A oompa loompa is in your path and greets you")
elif move == 'w':
    print ("\nYou walk to the field of wild french fries, stopping to chomp on a few")
    print ("A oompa loompa is in your path and greets you\n")

villager()

print ("After leaving the oompa loompa to do some more exploring you walk around until you come across a strange dark hole that had a latter leading down")
print ("Looking for adventure you climb down the latter to see if perhaps there was a tunnel leading to more delicious foods.")
print ("Soon you realize... that the tunnel is made out of...black licorice. Then you realize that this tunnel could possibly be the towns sewage system and simply brush off the thought in hopes of uncovering a new realm.")
enemy()
sleep(3)

fight = input("Do you wish to fight? To fight the ogre press y and enter to continue. " )

if fight == "y":
    while HP > -5:
#This loop will only work while our characters HP is greater than -5.
        hit = randint(10,20)
        print ("You use your weapon and cause %s of damage" % str(hit))
        enemyHP = enemyHP - hit
        print (enemyHP)
        enemyhit = randint(0,1)
        print ("The ogre swings a club at you and causes %s of damage" % str(enemyhit))
        HP = HP - enemyhit
        print (HP)
else:
    print ("You turn and run away from "+enemyname+"")

if enemyHP < 1:
    print ("You have finally killed the menacing and evil "+enemyname+" and the Safe Haven of Delacacies has returned to peace.")
    print ("As you walk through the village on your way home you tell the oompa loompa's of your battle. They cheer in excitement and gratitude and invite you to a delicious buffet down by the Chocolate River, with your favorite food... Burgers. ")
    print ("As you walk down to the River where your delicious dinner awaits you get to talking to the oopma loompas and find your friend "+npcname+" and you become bestfriends")
    print ("Then you live happily ever after with your oompa loompa friends, in the Safe Haven you now call home.")
else :
    print("YOU HAVE FAILED YOUR OOMPA LOOMPA FRIENDS AND NOW THEY WILL ALL DIE BECAUSE YOU WERE TOO SCARED TO KILL "+enemyname+"")

print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|)")

print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/)")

print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")