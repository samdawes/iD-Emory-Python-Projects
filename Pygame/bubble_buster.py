import pygame
import sys
from pygame.locals import *
pygame.init()

#Initialize display size, caption, score counter, and color
screen = pygame.display.set_mode((640, 460))
pygame.display.set_caption("Bubble Buster!!!")
font = pygame.font.SysFont(None, 36)
screen.fill((0, 128, 128))

#Main clock (for consistent FPS)
main_clock = pygame.time.Clock()

#Score
score = 0
#Lives
lives = 0
alive = True

#Player paddle
player= pygame.Rect(300, 400, 60, 10)
move_left = False
move_right = False
player_speed = 8

#Funcs for redrawing player and screen
def draw_player():
    pygame.draw.rect(screen, (0, 0, 0), player)
    
def draw_screen():
    screen.fill((0, 128, 128))

#Ball
x_position = 320
y_position = 380
last_x = x_position
last_y = y_position
ball_can_move = False
speed = [5, -5]

#values for all bubbles to use
all_bubbles = []
bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 70
bubble_spacing = 60

#Bubble funcs
def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position

    for rows in range(0, 3):
        for columns in range(0, 10):
            bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble_x, bubble_y), bubble_radius, bubble_edge)
            bubble_x += bubble_spacing
            all_bubbles.append(bubble)
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position

create_bubbles()

def draw_bubbles():
    for bubble in all_bubbles:
        bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble.x, bubble.y), bubble_radius, bubble_edge) 

#func for score counter
def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

#Main Game Loop, check for events here
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Keyboard input for players
        if event.type == KEYDOWN:       #key pressed down
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_right = True
                move_left = False
        if event.type == KEYUP:         #key released
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if alive:
                if event.key == K_SPACE:
                    ball_can_move = True
            if not alive:
                if event.key == K_RETURN:
                    lives = 3
                    alive = True
                    score = 0
                    ball_can_move = False
                    for x in range(0, len(all_bubbles)):
                        all_bubbles.pop()
                    create_bubbles()
            if event.key == K_SPACE:
                ball_can_move = True

    #Ensure consistent frames per second
    main_clock.tick(50)

    #checks if left/right movement detected, adjust position on screen
    if move_left and player.left > 0:
        player.x -= player_speed
    if move_right and player.right < 640:
        player.x += player_speed

    #Code for ball motion
    if ball_can_move:
        last_x = x_position
        last_y = y_position

        x_position += speed[0]
        y_position += speed[1]

        #check boundaries
        if ball.x <= 0:
            x_position = 15
            speed[0] = -speed[0]
        if ball.x >= 640:
            x_position = 625
            speed[0] = -speed[0]
        if ball.y <= 0:
            y_position = 15
            speed[1] = -speed[1]
        #Subtracting lives
        elif ball.y >= 460:
            lives -= 1
            ball_can_move = False

        #collisions with player
        if ball.colliderect(player):
            y_position -= 15
            speed[1] = -speed[1]

        #move direction vector
        move_direction = ((x_position - last_x), (y_position - last_y))

        #Test collisions with the bubbles
        for bubble in all_bubbles:
            if ball.colliderect(bubble):
                if move_direction[1] > 0:
                    speed[1] = -speed[1]
                    y_position -= 10
                elif move_direction[1] < 0:
                    speed[1] = -speed[1]
                    y_position += 10
                all_bubbles.remove(bubble)
                score += 100
                break
            
    else: #if the player hasn't started the game yet
        x_position = player.x + 30
        y_position = 380

    if lives <= 0:
        alive = False
    
    draw_screen()
    draw_player()
    draw_bubbles()
    ball = pygame.draw.circle(screen, (0, 0, 0), (x_position, y_position), 5, 0)

    if alive:
        draw_text("Score: %s" % (score), font, screen, 5, 5)
        draw_text("Lives: %s" % (lives), font, screen, 540, 5)
    elif len(all_bubbles) == 0:
        draw_text("You're a winner!", font, screen, 255, 5)
        ball_can_move = False
        alive = False
        lives = 0
    else:
        draw_text("Game Over", font, screen, 255, 5)
        draw_text("Press Enter to Play Again", font, screen, 180, 50)
    
    pygame.display.update()

    


