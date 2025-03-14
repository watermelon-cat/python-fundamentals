
import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("fish mouse imput")

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
chest = 1
ticker = 0
fish = 1

#load in the image and make transparent
chestImg1 = pygame.image.load("chest1.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg1, [255,0,255])
#load in the image and make transparent
chestImg2 = pygame.image.load("chest2.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg2, [255,0,255])

fish1 = pygame.image.load("fishsilver.png").convert_alpha()
fish1 = pygame.transform.scale(fish1, (40,40))
pygame.Surface.set_colorkey (fish1, [255,0,255])
fish2 = pygame.image.load("fishsilverupsidedown.png").convert_alpha()
fish2 = pygame.transform.scale(fish2, (40,40))
pygame.Surface.set_colorkey (fish2, [255,0,255])




while 1: #game loop###########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        print(mousePos) #this is to help you know where to set these boundaries
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #check if you've clicked on the chest
            if mousePos[0]>238 and mousePos[0] < 355 and mousePos[1]>130 and mousePos[1]<230:
               chest = 2
            
            if mousePos[0]>398 and mousePos[0] < 448 and mousePos[1]>190 and mousePos[1]< 250:
                fish = 2
            
         
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos        
    
    #update/physics section----------------------

    #keep chest open for 50 game loops:
    if chest == 2:
        ticker+=1
        if ticker >= 200:
            ticker = 0
            chest = 1
            
    if fish == 2:
        ticker+=1
        if ticker >= 2000:
            ticker = 0
            fish = 1


    #render section------------------------------
    
    screen.fill((0,0,180))# Clear the screen
    
    #draw background image
    if chest == 1:
        screen.blit(chestImg1, (240, 140))
    elif chest ==2: 
        screen.blit(chestImg2, (240, 140))
    
    if fish == 1:
        screen.blit(fish1, (400, 200))
    elif fish == 2:
        screen.blit(fish2, (400, 200))
    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()

