import pygame
pygame.init()
pygame.display.set_caption("File IO Platformer Practice")
screen = pygame.display.set_mode((800, 800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

#CONSTANTS
LEFT  = 0
RIGHT = 1
UP    = 2
DOWN  = 3

#player variables
vx   = 0
vy   = 0
keys = [False, False, False, False]
isOnGround = False
score = 0

level = 1

# ── FILE I/O ──────────────────────────────────────────────────────────────

def load_platforms(filename):
    platforms = []                          # start with an empty list
    with open(filename, "r") as f:          # open the file for reading
        for line in f:                      # go through every line in the file
            if line[0] == "#" or line[0] == "\n":  # skip comment lines and blank lines
                continue
            x = int(line)                   # read x
            y = int(f.readline())           # read y
            w = int(f.readline())           # read width
            h = int(f.readline())           # read height
            platforms.append([x, y, w, h]) # add this platform to the list
    return platforms

def load_circles(filename):
    circles = []                          # start with an empty list
    with open(filename, "r") as f:          # open the file for reading
        for line in f:                      # go through every line in the file
            if line[0] == "#" or line[0] == "\n":  # skip comment lines and blank lines
                continue
            x = int(line)                   # read x
            y = int(f.readline())           # read y
            r = int(f.readline())           # read radius
            red = int(f.readline())           # read red color (RGB)
            green = int(f.readline())         # read green color
            blue = int(f.readline())          #read blue color
            circles.append([x, y, r, red, green, blue]) # add this platform to the list
    return circles

def load_score(filename):
    try:                                    # try this -- it might fail if the file doesn't exist yet
        with open(filename, "r") as f:
            return int(f.readline())        # read the score and convert it to an int
    except FileNotFoundError:              # if the file wasn't there, just return 0
        return 0

def save_score(filename, score):
    with open(filename, "w") as f:          # open for writing -- creates the file if needed
        f.write(str(score))                 # write the score (files store text, not numbers)

def load_position(filename):
    try:
        with open(filename, "r") as f:
            x = int(f.readline())
            y = int(f.readline())
            return x, y
    except FileNotFoundError:
        return 0
def save_position(filename, xpos, ypos):
    with open(filename, "w") as f:
        f.write(str(xpos))
        
    with open(filename, "a") as f:
        f.write(str(ypos))


# load platforms from the text file instead of hardcoding them

circles = load_circles("circles.txt")

# load the high score -- returns 0 if highscore.txt doesn't exist yet
high_score = load_score("highscore.txt")

try:
    xpos, ypos = load_position("position.txt")
except:
    xpos = 500
    ypos = 700

font = pygame.font.SysFont("monospace", 24)

while not gameover:
    clock.tick(60)

    #Input Section------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT]  = True
            if event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            if event.key == pygame.K_UP:
                keys[UP]    = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]  = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP]    = False

    if level == 1:
        platforms  = load_platforms("level1.txt")
    elif level == 2:
        platforms  = load_platforms("level2.txt")

    #physics section----------------------------------------------------------
    if keys[LEFT]  == True:   vx = -3
    elif keys[RIGHT] == True: vx =  3
    else:                     vx =  0

    if keys[UP] == True and isOnGround == True:
        vy = -8
        isOnGround = False

    #COLLISION
    isOnGround = False                  # assume we are in the air until proven otherwise
    for p in platforms:                 # check every platform in the list
        px, py, pw, ph = p[0], p[1], p[2], p[3]
        if xpos + 20 > px and xpos < px + pw:       # player overlaps platform horizontally
            if ypos + 40 > py and ypos + 40 < py + ph + 10:  # player's feet near top of platform
                ypos = py - 40          # sit the player on top of the platform
                isOnGround = True
                vy = 0                  # stop falling

    for c in circles:
        cx, cy, cw, ch = c[0]-c[2], c[1]-c[2], c[2]*2, c[2]*2
        if xpos + 20 > cx and xpos < cx + cw and ypos + 40 > cy and ypos < cy + ch: 
            circles.remove(c)
            print("coin collected")

    # stop the player falling through the bottom of the screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760

    #moves to new level
    if ypos < 0:
        level += 1
        ypos = 760

    # only apply gravity when in the air
    if isOnGround == False:
        vy += .2                        # vy grows each frame -- this is acceleration

    xpos += vx
    ypos += vy

    # keep player from walking off the sides of the screen
    if xpos < 0:   xpos = 0
    if xpos > 780: xpos = 780

    # score increases while the player is moving
    if vx != 0:
        score += 1

    # check if we beat the high score and save immediately if so
    if score > high_score:
        high_score = score
        save_score("highscore.txt", high_score)

    #RENDER Section-----------------------------------------------------------
    screen.fill((0,0,0))                # wipe the screen each frame

    # draw every platform from the list
    for p in platforms:
        pygame.draw.rect(screen, (200, 0, 20), (p[0], p[1], p[2], p[3]))

    for c in circles:
        pygame.draw.circle(screen, (c[3], c[4], c[5]), (c[0],c[1]), c[2])

    # draw the player
    pygame.draw.rect(screen, (200, 0, 10), (xpos, ypos, 20, 40))

    # str() converts a number to a string so we can join them with +
    score_text = font.render("Score: " + str(score) + "   Best: " + str(high_score), True, (255,255,255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# save the final score when the game closes
save_score("highscore.txt", high_score)
save_position("position.txt", xpos, ypos)

pygame.quit()
