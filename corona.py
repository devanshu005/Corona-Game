import pygame  # import pygame package

pygame.init()  # initiate package

grey = (0, 168, 243)  # colour code in RBG form
black = (0, 0, 0)  # colour code in RBG form
display = pygame.display.set_mode((1000, 600))  # set width & height of display
pygame.display.set_caption("Corona Game")  # set window name
manimg = pygame.image.load(".vscode\corona\man1.png")  # load image
backgroundleft = pygame.image.load(".vscode\corona\left.png")  # load background left side image
backgroundright = pygame.image.load(".vscode\corona\right1.png")  # load background right side image
man_width = 23
import time  # import the time for restart the game
import random  # import for random position comes


def covid(corona_startx, corona_starty, police):  # define function
    if police == 0:  # at 0 stage
        corona_come = pygame.image.load(".vscode\corona\corona1.png")  
    if police == 1:  # at 1 stage
        corona_come = pygame.image.load(".vscode\corona\corona2.jpg")  
    if police == 2:
        corona_come = pygame.image.load(".vscode\corona\man1.png")  # police man1 come

    display.blit(corona_come, (corona_startx, corona_starty))  # display the police car


def crash():  # create crash function to display this message
    message_display("      YOU GOT CORONA")  # display this message call the message_display function


def message_display(text):  # create function for message edit
    largetext = pygame.font.Font("freesansbold.ttf", 80)  # message in this style and the size will be 80
    textsurf, textrect = text_object(text, largetext)  # create function to edit message
    textrect.center = ((400), (300))  # show the message position in display
    display.blit(textsurf, textrect)  # display this message
    pygame.display.update()  # update display
    time.sleep(3)  # after crashed 3 sec restart the game
    loop()  # call the loop function to restart the game


def text_object(text, font):  # display after crash
    textsurface = font.render(text, True, black)  # display in this colour
    return textsurface, textsurface.get_rect()  # after that restart the game & ready to give some input


def background():
    display.blit(backgroundleft, (0, 0))  # set left side position of background image at x axis & y axis
    display.blit(backgroundright, (700, 0))  # set right side position of background image at x axis & y axis


def man(x, y):  # create  function
    display.blit(manimg, (x, y))  # set position of man


def loop():  # all the function are called using this function
    x = 400  # x axis position 
    y = 540  # y axis position
    x_change = 0  # set x position at x axis
    y_change = 0  # set y position at y axis
    corona_speed = 5  # corona speed
    police = 0  # corona is 0 stage
    corona_startx = random.randrange(130, (700 - man_width))  # corona x axis comes randomly
    corona_starty = -600  # corona comes in y axis -600 becuase opposite side
    corona_width = 23  # corona width
    corona_height = 47  # corona height

    bumped = False  # if game is not any problem to start
    while not bumped:  # game is start
        for event in pygame.event.get():  # if any input is given
            if event.type == pygame.QUIT:  # if quit input is given
                #	bumped=True		#game is stop
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # if any key pressed
                if event.key == pygame.K_LEFT:  # if pressed key is left
                    x_change = -5  # move left side -5
                if event.key == pygame.K_RIGHT:  # if pressed key is right
                    x_change = 5  # move right side +5
            if event.type == pygame.KEYUP:  # if key unpressed then
                x_change = 0
        x += x_change

        display.fill(grey)  # apply colour to display
        background()
        corona_starty -= (corona_speed / 4)  # speed at y axis
        covid(corona_startx, corona_starty, police)  # call covid function
        corona_starty += corona_speed  # corona speed increse
        man(x, y)  # call the function of man
        if x < 130 or x > 700 - man_width:  # if man goes out of this range
            #	bumped=True				#stop the game
            crash()  # call crash function
        if corona_starty > 600:  # corona pass it without crashed
            corona_starty = 0 - corona_height  # only one is crossed
            corona_startx = random.randrange(130, (1000 - 300))  # another 
            police = random.randrange(0, 2)  # diffrent  

        if y < corona_starty + corona_height:  # if corona not pass
            if x > corona_startx and x < corona_startx + corona_width or x + man_width > corona_startx and x + man_width < corona_startx + corona_width:
                crash()  # crash the man

        pygame.display.update()  # update the display


loop()  # call the loop function
pygame.quit()  # package is stop
quit()  # game is stop


