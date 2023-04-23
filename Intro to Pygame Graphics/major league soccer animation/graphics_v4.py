# Imports
import pygame
import math
import random


def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


def draw_court():
    # 6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

    # 18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    # safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    # arc at the top of the goal box
    pygame.draw.arc(
        screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

    # out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    # left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    # right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)


def draw_flag(flag_color, flag_points, pole_color, pole_top, pole_bottom, pole_width):
    pygame.draw.line(screen, pole_color, pole_top, pole_bottom, pole_width)
    pygame.draw.polygon(screen, flag_color, flag_points)


def draw_goal():
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

    # Back of net vertical
    for i in range(10):
        pygame.draw.line(
            screen, WHITE, [384 + (i*4), 140], [384 + (i * 4), 200], 1)
    for i in range(13):
        pygame.draw.line(
            screen, WHITE, [325 + (i*5), 140], [341 + (i * 3), 200], 1)
        pygame.draw.line(
            screen, WHITE, [424 + (i*5), 140], [423 + (i * 3), 200], 1)
        # Back of net horizontal
        pygame.draw.line(
            screen, WHITE, [324, 144 + (i*4)], [476, 144 + (i*4)], 1)

    # Net left and right
    for i in range(7):
        pygame.draw.line(screen, WHITE, [320, 140], [324 + (i * 2), 216 - (i*2)], 1)
        pygame.draw.line(screen, WHITE, [480, 140], [476 - (i * 2), 216 - (i*2)], 1)


def draw_light_pole(polePosition, lightX, lightY):
    pygame.draw.rect(screen, GRAY, [polePosition, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [polePosition, 195, 20, 10])
    temp_x = lightX
    while (temp_x != lightY):
        pygame.draw.ellipse(screen, light_color, [temp_x, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [temp_x, 20, 20, 20])
        temp_x += 20
    for i in range(3):
        pygame.draw.line(
            screen, GRAY, [lightX, 60 - (i * 20)], [lightY, 60 - (i * 20)], 2)


def draw_stand(barricadeColor, barricade, audienceColor, audience):
    pygame.draw.polygon(screen, barricadeColor, barricade)
    pygame.draw.polygon(screen, audienceColor, audience)


# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

# Config
lights_on = True
day = True

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    clouds.append([x, y])

# Game loop
done = False
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= 0.5
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)

    if not day:
        # stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    pygame.draw.rect(screen, field_color, [0, 180, 800, 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    # Drawing fence
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [
                            [x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40])
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))

    # score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    # score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)
    
    draw_court()

    draw_light_pole(150, 110, 210)
    draw_light_pole(630, 590, 690)

    '''
    def draw_light_pole(x):
        pygame.draw.rect(screen, GRAY, [x, 60, 20, 140])
        pygame.draw.ellipse(screen, GRAY, [x, 195, 20, 10])

    def draw_lights(x, y):
        temp_x = x
        pygame.draw.line(screen, GRAY, [x, 60], [y, 60], 2)
        while temp_x != y:
            pygame.draw.ellipse(screen, light_color, [temp_x, 40, 20, 20])
            temp_x += 20
        pygame.draw.line(screen, GRAY, [x, 40], [y, 40], 2)

        temp_x = x
        while temp_x != y:
            pygame.draw.ellipse(screen, light_color, [temp_x, 20, 20, 20])
            temp_x += 20
        pygame.draw.line(screen, GRAY, [x, 20], [y, 20], 2)

    # Light pole 1
    draw_light_pole(150)
    draw_lights(110, 210)

    # Light pole 2
    draw_light_pole(630)
    draw_lights(590, 690)
    '''

    draw_goal()
    '''
    #goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)


    #net
    pygame.draw.line(screen, WHITE, [325, 140], [341, 200], 1)
    pygame.draw.line(screen, WHITE, [330, 140], [344, 200], 1)
    pygame.draw.line(screen, WHITE, [335, 140], [347, 200], 1)
    pygame.draw.line(screen, WHITE, [340, 140], [350, 200], 1)
    pygame.draw.line(screen, WHITE, [345, 140], [353, 200], 1)
    pygame.draw.line(screen, WHITE, [350, 140], [356, 200], 1)
    pygame.draw.line(screen, WHITE, [355, 140], [359, 200], 1)
    pygame.draw.line(screen, WHITE, [360, 140], [362, 200], 1)
    pygame.draw.line(screen, WHITE, [364, 140], [365, 200], 1)
    pygame.draw.line(screen, WHITE, [368, 140], [369, 200], 1)
    pygame.draw.line(screen, WHITE, [372, 140], [373, 200], 1)
    pygame.draw.line(screen, WHITE, [376, 140], [377, 200], 1)
    pygame.draw.line(screen, WHITE, [380, 140], [380, 200], 1)
    pygame.draw.line(screen, WHITE, [384, 140], [384, 200], 1)
    pygame.draw.line(screen, WHITE, [388, 140], [388, 200], 1)
    pygame.draw.line(screen, WHITE, [392, 140], [392, 200], 1)
    pygame.draw.line(screen, WHITE, [396, 140], [396, 200], 1)
    pygame.draw.line(screen, WHITE, [400, 140], [400, 200], 1)
    pygame.draw.line(screen, WHITE, [404, 140], [404, 200], 1)
    pygame.draw.line(screen, WHITE, [408, 140], [408, 200], 1)
    pygame.draw.line(screen, WHITE, [412, 140], [412, 200], 1)
    pygame.draw.line(screen, WHITE, [416, 140], [416, 200], 1)
    pygame.draw.line(screen, WHITE, [420, 140], [420, 200], 1)
    pygame.draw.line(screen, WHITE, [424, 140], [423, 200], 1)
    pygame.draw.line(screen, WHITE, [428, 140], [427, 200], 1)
    pygame.draw.line(screen, WHITE, [432, 140], [431, 200], 1)
    pygame.draw.line(screen, WHITE, [436, 140], [435, 200], 1)
    pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
    pygame.draw.line(screen, WHITE, [445, 140], [441, 200], 1)
    pygame.draw.line(screen, WHITE, [450, 140], [444, 200], 1)
    pygame.draw.line(screen, WHITE, [455, 140], [447, 200], 1)
    pygame.draw.line(screen, WHITE, [460, 140], [450, 200], 1)
    pygame.draw.line(screen, WHITE, [465, 140], [453, 200], 1)
    pygame.draw.line(screen, WHITE, [470, 140], [456, 200], 1)
    pygame.draw.line(screen, WHITE, [475, 140], [459, 200], 1)

    #net part 2
    pygame.draw.line(screen, WHITE, [320, 140], [324, 216], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [326, 214], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [328, 212], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [330, 210], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [332, 208], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [334, 206], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [336, 204], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [338, 202], 1)

    #net part 3
    pygame.draw.line(screen, WHITE, [480, 140], [476, 216], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [474, 214], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [472, 212], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [470, 210], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [468, 208], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [466, 206], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [464, 204], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [462, 202], 1)

    #net part 4
    pygame.draw.line(screen, WHITE, [324, 144], [476, 144], 1)
    pygame.draw.line(screen, WHITE, [324, 148], [476, 148], 1)
    pygame.draw.line(screen, WHITE, [324, 152], [476, 152], 1)
    pygame.draw.line(screen, WHITE, [324, 156], [476, 156], 1)
    pygame.draw.line(screen, WHITE, [324, 160], [476, 160], 1)
    pygame.draw.line(screen, WHITE, [324, 164], [476, 164], 1)
    pygame.draw.line(screen, WHITE, [324, 168], [476, 168], 1)
    pygame.draw.line(screen, WHITE, [324, 172], [476, 172], 1)
    pygame.draw.line(screen, WHITE, [324, 176], [476, 176], 1)
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    pygame.draw.line(screen, WHITE, [335, 184], [465, 184], 1)
    pygame.draw.line(screen, WHITE, [335, 188], [465, 188], 1)
    pygame.draw.line(screen, WHITE, [335, 192], [465, 192], 1)
    pygame.draw.line(screen, WHITE, [335, 196], [465, 196], 1)
    '''
    # Function to draw stand
    draw_stand(RED, [[680, 220], [800, 340], [800, 290], [680, 180]], WHITE, [[680, 180], [800, 100], [800, 290]])
    draw_stand(RED, [[120, 220], [0, 340], [0, 290], [120, 180]], WHITE, [[120, 180], [0, 100], [0, 290]])

    '''
    # stands right
    pygame.draw.polygon(
        screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

    # stands left
    pygame.draw.polygon(
        screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])
    '''

    # Drawing Flags function

    # Drawing flags
    draw_flag(RED, ([132, 190], [125, 196], [135, 205]),
              BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    draw_flag(RED, ([668, 190], [675, 196], [665, 205]),
              BRIGHT_YELLOW, [660, 220], [665, 190], 3)

    '''
    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 
    '''

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))

    # pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    # pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    # pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
