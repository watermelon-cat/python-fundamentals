import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load("dog.jpg")
img = pygame.transform.scale(img, (800, 300))

class Heart:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        
        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)
class Flower:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self, surface):
        pygame. draw. rect(screen, (0,150, 0), (self.x+10, self.y+40, 15, 100))
        pygame. draw. circle(screen, (self.color), (self.x, self.y + 40), 20)
        pygame. draw. circle(screen, (self.color), (self.x, self.y), 20) #Base x = 580 base y = 180
        pygame. draw. circle(screen, (self.color), (self.x+40, self.y+40), 20)
        pygame. draw. circle(screen, (self.color), (self.x+40, self.y), 20)
        pygame. draw. circle(screen, (200, 100, 0), (self.x+20, self.y+20), 20)

# Create instances of Heart
heart1 = Heart(200, 200, (250, 0, 0))
heart2 = Heart(400, 200, (250, 0, 0))  # You can ask students to change positions and colors
heart3 = Heart(600, 200, (247, 104, 207))
heart4 = Heart(100, 700, (250, 0, 0))
heart5 = Heart(600, 500, (250, 0, 0))
heart6 = Heart(700, 600, (247, 104, 207))

flower1 = Flower(200, 400, (247, 104, 207))
flower2 = Flower(600, 350, (247, 104, 207))
flower3 = Flower(100, 400, (255, 255, 255))
flower4 = Flower(500, 200, (255, 255, 255))



text1 = font.render('I Love sleep', True, (250, 100, 100))
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200, 150, 150))
screen.blit(text1, (200, 100))
screen.blit(text2, (400, 300))
screen.blit(img, (0, 400))

#draw everything
heart1.draw(screen)
heart2.draw(screen)
heart3.draw(screen)
heart4.draw(screen)
heart5.draw(screen)
heart6.draw(screen)

flower1.draw(screen)
flower2.draw(screen)
flower3.draw(screen)
flower4.draw(screen)


pygame.display.flip()
pygame.time.wait(5000)

