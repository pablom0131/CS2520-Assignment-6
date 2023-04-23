# Imports
import pygame
import math
import random


# PUBLIC METHODS
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

    # Safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    # Arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

    # Out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    # Left line
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    # Right line
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

    for i in range(13):
        # Back of net vertical
        if i < 10:
            pygame.draw.line(screen, WHITE, [384 + (i * 4), 140], [384 + (i * 4), 200], 1)

        # Back of net horizontal
        pygame.draw.line(screen, WHITE, [325 + (i * 5), 140], [341 + (i * 3), 200], 1)
        pygame.draw.line(screen, WHITE, [424 + (i * 5), 140], [423 + (i * 3), 200], 1)
        pygame.draw.line(screen, WHITE, [324, 144 + (i * 4)], [476, 144 + (i * 4)], 1)

        # Left and right sides of net
        if i < 7:
            pygame.draw.line(screen, WHITE, [320, 140], [324 + (i * 2), 216 - (i * 2)], 1)
            pygame.draw.line(screen, WHITE, [480, 140], [476 - (i * 2), 216 - (i * 2)], 1)


def draw_light_pole(pole_position, x, y):
    pygame.draw.rect(screen, GRAY, [pole_position, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [pole_position, 195, 20, 10])
    temp_x = x
    while temp_x != y:
        pygame.draw.ellipse(screen, light_color, [temp_x, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [temp_x, 20, 20, 20])
        temp_x += 20
    for i in range(3):
        pygame.draw.line(screen, GRAY, [x, 60 - (i*20)], [y, 60 - (i*20)], 2)


def draw_stand(barricade_color, barricade, audience_color, audience):
    pygame.draw.polygon(screen, barricade_color, barricade)
    pygame.draw.polygon(screen, audience_color, audience)


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

    # Drawing code
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)

    if not day:
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    pygame.draw.rect(screen, field_color, [0, 180, 800, 420])   # Draws field with specific color
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])   # Draws field stripe behind goal
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])   # Draws field stripe before goal
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])   # Draws field stripe in middle
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])   # Draws field stripe on bottom

    # Draw fence posts
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])
    # Draw vertical fencing
    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)
    # Draw horizontal fencing
    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    # Draw the sun or moon
    if day:
        # Sun
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        # Moon
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40])
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    # Draw the clouds
    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))

    # Draw score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])
    # Draw score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)

    # Draw court
    draw_court()

    # Draw right light pole
    draw_light_pole(150, 110, 210)
    # Draw left light pole
    draw_light_pole(630, 590, 690)

    draw_goal()

    # Draw right stands
    draw_stand(RED, [[680, 220], [800, 340], [800, 290], [680, 180]], WHITE, [[680, 180], [800, 100], [800, 290]])
    # Draw left stands
    draw_stand(RED, [[120, 220], [0, 340], [0, 290], [120, 180]], WHITE, [[120, 180], [0, 100], [0, 290]])

    # Draw right flag
    draw_flag(RED, ([132, 190], [125, 196], [135, 205]), BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    # Draw left flag
    draw_flag(RED, ([668, 190], [675, 196], [665, 205]), BRIGHT_YELLOW, [660, 220], [665, 190], 3)

    # Changes brightness depending on time of day and lights
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
