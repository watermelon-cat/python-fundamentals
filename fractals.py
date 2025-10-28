import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fractals")
clock = pygame.time.Clock()
screen.fill((0,0,0))
running = True


def midpoint(x1, x2):
    x = x1 + x2
    midpoint = x/2
    return midpoint

def Sier(x1,y1,x2,y2,x3,y3, counter, isEven = 1):
    counter += 1
    if counter > 8:
        return 0
    
    #draw main triangle (optional)
    #pygame.draw.polygon(screen, (counter*300%255, counter*10%155, counter*20%255), ( (x1, y1),(x2, y2), (x3, y3)))
    pygame.draw.polygon(screen, (counter*60%255, counter*234%255, counter*34%255), ( (x1, y1),(x2, y2), (x3, y3)))
    
    if isEven:
        pygame.draw.polygon(screen, (counter*45%255, counter*12%255, counter*3002%255), ( (midpoint(x1, x2), midpoint(y1, y2)) , (midpoint(x2, x3), midpoint(y2, y3)), (midpoint(x3, x1), midpoint(y3, y1))))
    else:
        pygame.draw.polygon(screen, (0, 0, 0), ( (midpoint(x1, x2), midpoint(y1, y2)) , (midpoint(x2, x3), midpoint(y2, y3)), (midpoint(x3, x1), midpoint(y3, y1))))
        
    pygame.display.flip()
    
    isEven = isEven*-1
    
    #recursive call
    #top
    Sier(x1, y1, midpoint(x1, x2),midpoint(y1, y2), midpoint(x3, x1),midpoint(y3, y1), counter, isEven)
    #left
    Sier(midpoint(x1, x2),midpoint(y1, y2), x2, y2, midpoint(x2, x3),midpoint(y2, y3), counter, isEven)
    #right
    Sier(midpoint(x1, x3),midpoint(y1, y3), midpoint(x2, x3),midpoint(y2, y3) , x3,y3, counter, isEven)
    
while running:
    Sier(400, 0, 0, 800, 800, 800, 0)
    pygame.display.flip()
    pygame.time.wait(10000)

pygame.quit()
