#Mandlebrot Set Program
#Graphs the Mandlebrot set iteratively (function is NOT recursive)
import pygame
import math
import cmath

WIDTH = 800
HEIGHT = 800

pygame.init()
pygame.display.set_caption("mandelbrot")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))

def Mandelbrot( c = 0, z = complex(0,0), counter = 0):
    while (abs(z) < 2) and (counter < 80):
        z = z**2 + c
        counter += 1
    else:
        return counter


t = -2 #lower bound for real axis
while t<2: #upper bound for read (horizontal axis)
    t += .0005 #make this sumber smaller to increase picture resolution
    
    m = -2 #lower bound for imaginary axis
    while m<2: #upper bound for imaginary (verticle) axis
        m += .0005 #make this number SMALLER to increase picture resolution
        c = complex(t,m) #create a complex number from interators
        num = Mandelbrot(c); #call the function
        if num < 20:
            screen.set_at((int(t*200+400), int(m*200+400)), (num*2, num*8, num*2))
        elif num < 40:
            screen.set_at((int(t*200+400), int(m*200+400)), (num*2, num/2, num*4))
        elif num == 80:
            screen.set_at((int(t*200+400), int(m*200+400)), (0, 0, 0))
        else:
            screen.set_at((int(t*200+400), int(m*200+400)), (num*2, num/2, num*2))
        #print("num is ", num, " at ", t+400, m+400)
    
    pygame.display.flip()


pygame.time.wait(10000) #pause to see the picture
pygame.quit()
