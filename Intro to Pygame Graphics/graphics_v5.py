import pygame
import math
import random


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
        pygame.draw.line(screen, WHITE, [384 + (i*4), 140], [384 + (i * 4), 200], 1)
    for i in range(13):
        pygame.draw.line(screen, WHITE, [325 + (i*5), 140], [341 + (i * 3), 200], 1)
        pygame.draw.line(screen, WHITE, [424 + (i*5), 140], [423 + (i * 3), 200], 1)
        # Back of net horizontal
        pygame.draw.line(screen, WHITE, [324, 144 + (i*4)], [476, 144 + (i*4)], 1)

    # Net left and right
    for i in range(7):
        pygame.draw.line(screen, WHITE, [320, 140], [324 + (i * 2), 216 - (i*2)], 1)
        pygame.draw.line(screen, WHITE, [480, 140], [476 - (i * 2), 216 - (i*2)], 1)


def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


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

# Fonts
myfont = pygame.font.SysFont("monospace", 14)
smallerfont = pygame.font.SysFont("monospace", 10)
largefont = pygame.font.SysFont("monospace", 22)
numbersfont = pygame.font.SysFont("impact", 12)
largenumberfont = pygame.font.SysFont("impact", 30)
scorefont = pygame.font.SysFont("impact", 20)

# Images
img = pygame.image.load("Intro to Pygame Graphics\major league soccer animation\goalie.png")
img_b = pygame.image.load("Intro to Pygame Graphics\soccer_ball.png")

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

seconds = 45 * 60
ticks = 0

home_shots = 0
guest_shots = 0
home_saves = 0
guest_saves = 0
home_score = 0
guest_score = 0
goalie_x = 350
goalie_y = 150
ball_x = 400
ball_y = 400
    
# Game loop
done = False
while not done:
    # Event processing (react to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_n:
                day = not day
    state = pygame.key.get_pressed()

    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]
    a = state[pygame.K_a]
    s = state[pygame.K_s]
    d = state[pygame.K_d]
    w = state[pygame.K_w]

    # Game logic (check for collisions, update points, etc.)
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

    ticks += 1
    if ticks == 60:
        seconds -= 1
        ticks = 0

    if left is True and goalie_x >= 300:
        goalie_x -= 2
    elif right is True and goalie_x <= 400:
        goalie_x += 2

    if a is True and ball_x >=0:
        ball_x -= 4
    elif s is True and ball_y <= 600:
        ball_y += 4
    elif d is True and ball_x <= 750:
        ball_x += 4
    elif w is True and ball_y >= 200:
        ball_y -= 4
        
    # Drawing code (describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
        # Stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

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

    # Banner
    pygame.draw.polygon(screen, BLACK, [[300, 100], [360, 40], [360, 160]])

    # Out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    # Left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    # Right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)

    # Safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    # 18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    # Arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
    
    # Score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    # Score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [300, 40, 200, 90], 2)
    pygame.draw.rect(screen, WHITE, [360, 44, 80, 35], 2)
    # Home score
    pygame.draw.rect(screen, WHITE, [310, 60, 40, 20], 2)
    # Away score
    pygame.draw.rect(screen, WHITE, [450, 60, 40, 20], 2)
    # Half box
    pygame.draw.rect(screen, WHITE, [410, 82, 20, 15], 2)
    # Shots box
    pygame.draw.rect(screen, WHITE, [312, 110, 25, 15], 1)
    pygame.draw.rect(screen, WHITE, [417, 110, 25, 15], 1)
    # Saves box
    pygame.draw.rect(screen, WHITE, [357, 110, 25, 15], 1)
    pygame.draw.rect(screen, WHITE, [462, 110, 25, 15], 1)

    HOME = myfont.render("HOME", 1, (255, 255, 255))
    screen.blit(HOME, (313, 43))

    m = seconds // 60
    s = seconds % 60
    m = str(m)
    if s < 10:
        s = "0" + str(s)
    else:
        s = str(s)
    time_str = m + ":" + s

    # Display timer
    timer = largenumberfont.render(time_str, 1, RED)
    screen.blit(timer, (368, 43))

    if m == 0:
        halfnum = numbersfont.render("2", 1, RED)
    else:
        halfnum = numbersfont.render("1", 1, RED)

    if home_score == 0:
        homenum = scorefont.render("0", 1, RED)
    elif home_score == 1:
        homenum = scorefont.render("1", 1, RED)
    else:
        homenum = scorefont.render("00", 1, RED)
    
    if guest_score == 0:
        guestnum = scorefont.render("0", 1, RED)
    elif guest_score == 1:
        guestnum = scorefont.render("1", 1, RED)
    else:
        guestnum = scorefont.render("00", 1, RED)

    homeshots = numbersfont.render(str(home_shots), 1, RED)
    screen.blit(homeshots, (320, 110))

    screen.blit(guestnum, (477, 57)) 
    screen.blit(homenum, (335, 57))    
    screen.blit(halfnum, (418, 82))
    GUEST = myfont.render("GUEST", 1, (255, 255, 255,))
    screen.blit(GUEST, (450, 43))
    HALF = myfont.render("HALF", 1, WHITE)
    screen.blit(HALF, (370, 82))
    SHOTS = smallerfont.render("SHOTS", 1, WHITE)
    screen.blit(SHOTS, (310, 100))
    screen.blit(SHOTS, (415, 100))
    SAVES = smallerfont.render("SAVES", 1, WHITE)
    screen.blit(SAVES, (355, 100))
    screen.blit(SAVES, (460, 100))

    # 6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)
        
    # Light pole 1
    draw_light_pole(150)
    draw_lights(110, 210)
    
    # Light pole 2
    draw_light_pole(630)
    draw_lights(590, 690)
    
    # Drawing goal
    draw_goal()

    # Goalie
    screen.blit(img,(goalie_x, goalie_y))    

    # Stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

    # Stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])

    # Drawing flags
    draw_flag(RED, ([132, 190], [125, 196], [135, 205]), BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    draw_flag(RED, ([668, 190], [675, 196], [665, 205]), BRIGHT_YELLOW, [660, 220], [665, 190], 3)

    # Soccer-ball
    screen.blit(img_b, (ball_x, ball_y))
    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
"""
pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])
"""
"""
pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
pygame.draw.ellipse(screen, light_color, [110, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [130, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [150, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [170, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [190, 40, 20, 20])
pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
pygame.draw.ellipse(screen, light_color, [110, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [130, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [150, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [170, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [190, 20, 20, 20])
pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)
"""
"""
# Corner flag right
pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

# Corner flag left
pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]])
"""
"""
# Goal
pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

# Net
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

# Net part 2
pygame.draw.line(screen, WHITE, [320, 140], [324, 216], 1)
pygame.draw.line(screen, WHITE, [320, 140], [326, 214], 1)
pygame.draw.line(screen, WHITE, [320, 140], [328, 212], 1)
pygame.draw.line(screen, WHITE, [320, 140], [330, 210], 1)
pygame.draw.line(screen, WHITE, [320, 140], [332, 208], 1)
pygame.draw.line(screen, WHITE, [320, 140], [334, 206], 1)
pygame.draw.line(screen, WHITE, [320, 140], [336, 204], 1)
pygame.draw.line(screen, WHITE, [320, 140], [338, 202], 1)

# Net part 3
pygame.draw.line(screen, WHITE, [480, 140], [476, 216], 1)
pygame.draw.line(screen, WHITE, [480, 140], [474, 214], 1)
pygame.draw.line(screen, WHITE, [480, 140], [472, 212], 1)
pygame.draw.line(screen, WHITE, [480, 140], [470, 210], 1)
pygame.draw.line(screen, WHITE, [480, 140], [468, 208], 1)
pygame.draw.line(screen, WHITE, [480, 140], [466, 206], 1)
pygame.draw.line(screen, WHITE, [480, 140], [464, 204], 1)
pygame.draw.line(screen, WHITE, [480, 140], [462, 202], 1)

# Net part 4
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
"""
"""
pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])
"""
"""
pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
pygame.draw.ellipse(screen, light_color, [590, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [610, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [630, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [650, 40, 20, 20])
pygame.draw.ellipse(screen, light_color, [670, 40, 20, 20])
pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
pygame.draw.ellipse(screen, light_color, [590, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [610, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [630, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [650, 20, 20, 20])
pygame.draw.ellipse(screen, light_color, [670, 20, 20, 20])
pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)
"""