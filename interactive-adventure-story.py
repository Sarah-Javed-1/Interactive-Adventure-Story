#importing the turtle and time libraries
import turtle
import time
from cryptography.fernet import Fernet

#SECURITY MEASURE 1: USERNAME AND PASSWORD
#Asking the user for the password and username
print(
    "To access your interactive story, please enter your username and password!"
)
username = input("Username: ")
password = input("Password: ")
correctPass = "Spaceship29"
#encrypting the correct password as a security measure

key = Fernet.generate_key()
code = Fernet(key)
correctPass = code.encrypt(b"Spaceship29")
decoded = code.decrypt(correctPass)

#while loop that asks the user to re-enter the password until they get it right.
while password != decoded.decode():  #the password is Spaceship29
    print("Looks like the password you entered is incorrect.")
    password = input("Please try again: ")

#lets the user know that they entered the right password
print("Correct password!")

#SECURITY MEASURE 2: BIRTHDAY
#asks the user for their birthday and casts the string into an integer
bday = int(input("Please enter the year you were born"))
#makes sure that the year the person has entered is in between 1900 and 2022
while bday > 2022 or bday < 1900:
    bday = int(
        input(
            "You entered an invalid year, please enter a year between 1900 and 2022 "
        ))
#if the birth year is after 2013, the user will not be allowed to read the story and the program will end.
if bday >= 2013:
    print("Sorry! You are too young to read this story.")
    exit()
#if the birth year is before 2013, the user will be allowed to read the story
else:
    print("Congrats, you are old enough to read the maze cave story!")
    time.sleep(1)

#initializing different turtles for the drawings.
#flyer
water = turtle.Turtle()
semisun = turtle.Turtle()
heading = turtle.Turtle()
info = turtle.Turtle()
cave = turtle.Turtle()
bird = turtle.Turtle()

#map
maps = turtle.Turtle()
wall = turtle.Turtle()
symbol = turtle.Turtle()
lines = turtle.Turtle()


#creating a function for the first picture (the flyer)
def flyer():

    #setting up the screen background color and turtle speeds
    turtle.bgcolor('skyblue')
    turtle.speed(10)
    water.speed(10)
    cave.speed(10)

    #sea/water
    #creates a list called seaSize that stores the values for the circle sizes in the following for loop
    seaSize = [50, 45]
    #sets the turtle's position to (-150, -175)
    water.pu()
    water.setpos(-150, -175)
    water.pd()
    #changes the turtle's color to blue and begins a fill
    water.color("blue")
    #creates a for loop for the sea. 2 different sizes of circles are made 10 times wiht a space in between each circle. Draws a total of 10 circles.
    for i in range(5):
        for circle in seaSize:
            water.begin_fill()
            water.circle(circle)
            water.end_fill()
            water.fd(45)
    #stops the fill

    #sun
    #sets the turtle position to (-30. 185)
    semisun.pu()
    semisun.goto(-30, 185)
    semisun.pd()
    #changes the direction/angle of the turtle so that the sun is created the right way.
    semisun.lt(90)
    #sets the color of the turtle to gold and begins a fill
    semisun.color('gold')
    semisun.begin_fill()
    #makes a semi circle with a 50 px radius
    semisun.circle(50, 180)
    semisun.end_fill()

    #cloud
    #makes a list with numbers for the sizes of the circles that make the cloud
    cloudsizes = [10, 20, 20, 10]
    #sets the position of the turtle to (-150, 175)
    turtle.pu()
    turtle.setpos(-150, 175)
    turtle.pd()
    #sets the turtle of the color to white and begins a fill
    turtle.color('white')
    #makes 4 circles in different sizes that overlap and repeats it 3 times to make the cloud shape
    for i in range(3):
        for circles in cloudsizes:
            turtle.begin_fill()
            turtle.circle(circles)
            turtle.end_fill()
            turtle.pu()
            turtle.fd(15)
            turtle.pd()
        #stops the fill
    turtle.end_fill()

    #heading/title
    #sets the turtle position to (-150, 115)
    heading.pu()
    heading.setpos(-150, 150)
    heading.pd()
    #makes the turtle color orange
    heading.color("orange")
    #makes the turtle write in a specific font
    heading.write("Welcome to...", font=("Goudy Old Style", 9))
    #moves the turtle down to make space for more words
    heading.rt(90)
    heading.pu()
    heading.fd(200)
    heading.pd()
    #sets the turtle color to black
    heading.color("black")
    #the turtle writes the words in a specific font
    heading.write("MAZE\nCAVE", font=("Goudy Old Style", 35, 'bold'))
    #moving the heading turtle so that it is not ontop of the words
    heading.pu()

    #promo words on the top right corner
    #sets the turtle position to (250, 185)
    info.pu()
    info.setpos(330, 130)
    info.pd()
    #makes the turtle color orange
    info.color("orange")
    #the turtle writes some information about the Maze cave
    info.write(
        "THE\nmost famous attraction.\nThe puzzles are sure to \nget you wondering how to escape!",
        align='right',
        font=("Goudy Old Style", 8))

    #cave
    #sets the turtle position to (300, -100)
    cave.pu()
    cave.setpos(330, -100)
    cave.pd()
    #grey semicircle / main part of the cave
    cave.color('darkslategrey')
    cave.begin_fill()
    cave.pensize(25)
    cave.lt(90)
    cave.circle(125, 180)
    cave.lt(90)
    cave.fd(250)
    cave.end_fill()
    #Cave details (Vertical line and smaller semicircle)
    cave.pu()
    cave.color("orange")
    cave.pensize(3)
    cave.setpos(205, -100)
    cave.lt(90)
    cave.pd()
    cave.fd(125)
    cave.pu()
    cave.setpos(80, -100)
    cave.pd()
    cave.rt(90)
    cave.fd(250)
    cave.lt(90)
    cave.circle(125, 180)

    #birds
    #moves the turtle to the right spot and stamps the turtle shape onto the screen
    bird.pu()
    bird.fd(270)
    bird.lt(90)
    bird.fd(40)
    bird.pd()
    bird.setheading(315)
    bird.stamp()
    bird.pu()
    #moves the turtle and stamps it again to make another bird shape
    bird.setpos(220, 80)
    bird.stamp()
    #hiding the turtles
    water.hideturtle()
    semisun.hideturtle()
    heading.hideturtle()
    info.hideturtle()
    cave.hideturtle()
    bird.hideturtle()
    turtle.hideturtle()


flyer()


#creating a function for the second picture (the map)
def drawMap():
    global maps
    global wall
    global symbol
    global lines

    global location1
    global loc2
    global loc3
    #setting the screen color to burly wood
    turtle.bgcolor("burlywood")

    #creating a variable for the font
    fontstyle = 'Goudy Old Style', 30, 'bold'
    wall.speed(10)

    #walls
    #setting the turtle color to brown
    wall.color("brown")
    #making the pensize bigger
    wall.pensize(10)
    #setting the position of the turtle to (160, -200)
    wall.pu()
    wall.setpos(160, -200)
    wall.pd()

    #making the turtle face the right way and using circle and forward commands to make the walls on the left side
    wall.rt(205)
    wall.fd(275)
    wall.circle(-70, 180)
    wall.fd(50)
    wall.circle(50, 180)
    wall.fd(40)
    wall.circle(-50, 180)
    wall.fd(40)
    wall.circle(30, 180)
    #setting the position of the turtle to (160, 0)
    wall.pu()
    wall.setpos(160, 0)
    wall.pd()
    #making the walls on the right side using circle and forward commands
    wall.lt(90)
    wall.fd(90)
    wall.circle(-60, 180)
    wall.rt(90)
    wall.circle(90, 180)
    wall.circle(-10, 180)
    wall.circle(50, 180)
    #setting the turtle position to (-250, 100)
    maps.pu()
    maps.setpos(-250, 70)
    #making the turtle write the heading using the fontstyle font
    maps.write("MAZE \nCAVE", font=fontstyle)
    maps.rt(90)
    maps.fd(25)
    maps.write("directory", align=("left"), font=('Goudy Old Style', 20))
    #making a variable called legFont to hold font details for the legend
    legFont = "Goudy Old Style", 10

    #making a function called legend for the legend spacing
    def legend():
        maps.pu()
        maps.fd(30)
        maps.pd()

    #setting the turtle.position to (-250, -100)
    maps.pu()
    maps.setpos(-250, -100)
    maps.pd()
    #making the turtle write the legend heading
    maps.write("Legend", font=('Goudy Old Style', 15))
    #writing the parts of the legend (i.e. water and wall)
    legend()
    maps.write("Water", align='left', font=legFont)
    legend()
    maps.write("Wall", align='left', font=legFont)
    legend()
    #creating the "3-sided rectangle" for the scale
    maps.fd(10)
    maps.lt(90)
    maps.fd(25)
    maps.lt(90)
    maps.fd(10)
    #setting the turtle position to (-250, -185)
    maps.pu()
    maps.setpos(-250, -185)
    maps.pd()
    #turning the turtle face the right direction and writing the word scale
    maps.rt(90)
    maps.write("Scale: 1km", font=legFont)
    maps.rt(90)
    #setting the maps position to (-270, -60)
    maps.pu()
    maps.setpos(-270, -60)
    maps.pd()
    #making the rectangle/border around the legend
    for i in range(0, 4):
        maps.fd(150)
        maps.lt(90)
    #Location 1: clover-like shape
    #Setting the turtle position to (150, -150)
    maps.pu()
    maps.setpos(150, -150)
    maps.pd()
    #setting the turtle color to black
    maps.color("black")
    #creating a loop with different sized circles to create the clover shape
    for i in range(0, 3):
        maps.circle(40, 180)
        maps.rt(200)
        maps.circle(25, 180)
        maps.rt(45)
    #making the turtle label the first location
    maps.write(location1)
    #triangle
    #setting the turtle to the position (100, 190)
    maps.pu()
    maps.setpos(100, 190)
    maps.pd()
    #setting the turtle color to blue
    maps.color("blue")
    #makes the triangle using a for loop
    for i in range(0, 3):
        maps.fd(80)
        maps.rt(120)
    maps.pu()
    maps.fd(30)
    maps.pd()
    maps.write(loc3)
    #Circle
    #sets the turtle position to (-100, -10)
    maps.pu()
    maps.setpos(-100, -10)
    maps.pd()

    maps.color('black')
    maps.circle(50)
    maps.pu()
    maps.fd(10)
    maps.pd()
    maps.write(loc2)
    #Exit
    #set the turtle color to red
    maps.color('red')
    #set the turtle position to (140, 180)
    maps.pu()
    maps.setpos(140, 180)
    maps.pd()
    #make the turtle write the word exit
    maps.write("EXIT", font=('Goudy Old Style', 10))
    #blue and brown lines (in the legend)
    #set the position of the turtle to (-200, -120)
    lines.pu()
    lines.setpos(-200, -120)
    lines.pd()
    #set the turtle color to blue
    lines.color("blue")
    lines.fd(30)
    #moving the turtle down to lower position to make the brown line
    lines.fd(20)
    lines.rt(90)
    lines.pu()
    lines.fd(30)
    lines.pd()
    lines.rt(90)
    #set the turtle color to brown
    lines.color("brown")
    #make the turtle size 10
    lines.pensize(10)
    #draw the brown line
    lines.fd(50)


#THE STORY
#welcomes the user
print(
    "************************\nWELCOME TO THE MAZE CAVE\n************************"
)
print(
    "Dear", username,
    "do you think you have what it takes to find your way through the maze? Let's find out..."
)
time.sleep(3)
#asking the user to enter some location details for some of the blanks and storing it in variables named park, loc2 and loc3.
park = input("Which park does your story take place in? ")
loc2 = input("Choose a name for one of the places on the map. ")
loc3 = input("Choose a name for another place on the map. ")

print(
    "\nYou went to explore in", park,
    ",but had fallen asleep and lost your way in the middle of some sort of cave. Now, you need to find your way out before your uber driver arrives in 30 minutes."
)
time.sleep(6)
print(
    "Firstly, you try to contact your driver, but notice that there is no cell service. \nNext, you look through your backpack."
)
#asking the user to enter one thing they would like to include in their backpack.
item = input("Choose 1 item that you would like to have in your backpack. ")
print(
    "Inside your backpack, there is an empty water bottle, a first aid kit, and",
    item)
time.sleep(4)
print(
    "Just as you are about to zip your bag, you see a piece of rolled up paper that looks like a brocheure.\nThe picture above depicts what it looks like"
)

#TURTLE DRAWING 1: THE BROCHEURE
flyer()

time.sleep(4)
print(
    "It turns out that you are in the most famous - and hardest to navigate - tourist destination in",
    park,
    "! The 'Cave Maze' is supposed to have some really hard riddles that must be completed in time before the huge metal doors shut and trap you inside!"
)
time.sleep(5)

print(
    "You decide to wander around for a while in hopes to find your way out, when you suddenly hear some movement towards the right"
)
#Asking the user whether they would like to continue moving forward or turn right and storing that information in a variable called movementChoice
movementChoice = input(
    "do you (a) move towards the noise or (b) keep walking straight")
#if the user does not enter a or b, they will be asked to enter a valid choice until they choose a or b.
while not (movementChoice == "b" or movementChoice == "a"):
    movementChoice = input("please type a or b")
if movementChoice == "b":
    #if the user chooses to keep going forward, they will be prompted with this message and forced to turn right
    print(
        " you walk for 200 metres before you hit a dead end and retrace your steps back. It looks like you will have to turn right."
    )
print(
    "You cautiously approach the noise and notice that it sounds like someone is walking."
)
#asks the user to enter the name of the person they are about to meet and stores the name in a variable called friend. Then the program uses that name to introduce the friend.
friend = input("What is the name of the person you approach? ")
print("You break into a run and find out that it is", friend,
      "from your earlier tour group!")
time.sleep(4)
print(friend, "exclaims", '"', username,
      "help me! I fell and scraped my knee!'")
#gives the user the option to help the person
aid = input("Do you want to help? Type yes or no. ")
#if the user chooses not to help the friend, they will be asked to reconsider until they agree to helping
while aid.lower() != "yes":
    print("I really think you should help", friend)
    aid = input("Type 'yes' if you want to help ")
print(
    "You pull out a first aid kit from your bag and help patch them up.\n",
    friend,
    "thanks you for your help and reveals that they have a map on their phone of the area, but were not sure where to go.\nYou remember having seen a sign saying that you were in..."
)
time.sleep(5)
#asks the user to make up the name of the place they are currently at
location1 = input("What is the name of the location you are at right now? ")

#TURTLE DRAWING 2: THE MAP
turtle.clear()
water.clear()
semisun.clear()
heading.clear()
info.clear()
cave.clear()
bird.clear()
drawMap()

print(
    "Based on this information, you look at the map and know exactly which place to go to in order to reach the exit."
)
#asks the user to guess which place they need to go to based on the map
location2 = input("Which location should you go to? ")
#until the user gets the right place, the computer will keep asking them to re-enter the location
while location2 != loc2:
    location2 = input("I think you got the wrong location. Try again! ")

print("You point towards", location2,
      "and the two of you begin to head there.")
time.sleep(5)
print(
    "At", location2,
    "you notice that there is no way to go forward as there are walls on all 4 sides. \n",
    friend, "points out that there is a carving on the wall saying")
time.sleep(3)
print(
    "“What has roots that nobody sees, \nIs taller than trees, \nUp, up it goes, \nAnd yet never grows?”"
)
time.sleep(6)
#asks the user to answer the riddle and stores their answer in a variable called answer
answer = input("What is the answer to this riddle? ")
#until the user gets the right answer, they will be asked to keep guessing
while answer.lower() != "mountain":
    answer = input("Not quite! Try again: ")
print("Correct! The answer is mountain!")
time.sleep(3)

print(
    "When you say your answer out loud, the wall splits open and you start to head towards..."
)
#asks the user to enter the name of the location they need to go to next
location3 = input("Which location do you need to go to next? ")
#until the user gets the right place, the computer will keep asking them to re-enter the location
while location3.lower() != loc3:
    location3 = input("I think you chose the wrong location, try again! ")
print(
    "You finally make it to", location3,
    "but quickly realize there is a problem. The area is full of water and neither of you know how to swim."
)
time.sleep(6)
print(
    "You and friend are thirsty, so you use this as a chance to collect some water to drink while you think of ideas to get past this. As you bend down to fill your water bottle, you notice a series of numbers around the basin of water. \nUsing your phone flashlight, you see that it is a pattern of numbers and one of the numbers is missing."
)
time.sleep(7)
#prints the list of numbers that are stored in the nums list
nums = [0, 3, 6, 12, 15]
print(nums)
#asks the user to enter the missing number and stores their answer in num
num = int(input("Which number is missing? "))
#until the user enters the right answer, which is 9, they will be asked to keep guessing until they get it right
while num != 9:
    num = int(input("Not quite! Try again: "))
print(
    "You guessed correctly, but you aren't sure how to enter or write the number! You and",
    friend,
    "look around and the two of you find a piece of chalk on the far edge of the area. "
)
time.sleep(4)

#asks the user to enter what they think shows up
cross = input(
    "What do you think shows up when you write out the answer using the chalk? "
)
if cross != "boat":
    print("You guessed wrong but that's okay! The correct answer was a boat.")
elif cross == "a boat":
    print("Correct!")
print(
    "You write '9' in the missing space and a boat suddenly appears. Onwards to the exit!"
)
time.sleep(7)

print(
    "\n\n You and", friend,
    "finally reach the exit. You are exhausted and are ready to go back home, when the opening to leave the cave is shut by huge, metal doors. It turns out that you did not finish the maze in time! \nSuddenly a few musical notes begin to play, but end quickly. Luckily,",
    friend, "is a musical prodigy and remembers the notes perfectly.")
time.sleep(10)
#asks the user to enter any musical note and stores their answer in note
note = input(
    "Type a musical note that was played (you can choose any note you want) ")
time.sleep(0.5)
print(
    "Unfortunately, you are not sure what to do with that information until you find an indent in the metal door. You lift up the panel and see a small keypad with musical notes written in it. \nYour friend enters",
    note, "and the metal doors open.")
time.sleep(7)
print("The two of you can finally go home!")
print("*******\nTHE END\n*******")
