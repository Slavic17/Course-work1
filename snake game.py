import pygame
import sys
import random


pygame.init()
FPS = 15
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
VELOCITY = 10
SNAKE_WIDTH = 25
APPLE_SIZE = 40
TOP_WIDTH = 80
small_font = pygame.font.SysFont('Calibri', 35)
medium_font = pygame.font.SysFont('Courier New', 30, True)
large_font = pygame.font.SysFont('Courier New', 40, True, True)
clock = pygame.time.Clock()
pygame.mixer.init()
music = pygame.mixer.music.load(r'C:\Users\slava\python\snake\music\Snake.mp3')
pygame.mixer.music.play(-1)

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
snake_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\head.png'), (80, 110))
apple_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\apple.png'), (APPLE_SIZE, APPLE_SIZE))
body_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\body13.png'), (110, 140))
head_width, head_height = snake_img.get_size()
music_button_image = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\music.png'), (40, 40))
music_button_rect = music_button_image.get_rect(topleft=(WINDOW_WIDTH - 130, 17))
def load_background(screen_width, screen_height):
    background_image = pygame.image.load(r"C:\Users\slava\python\snake\Photo\menu.png")
    return pygame.transform.scale(background_image, (screen_width, screen_height))

def load_settings_background(screen_width, screen_height):
    background_image = pygame.image.load(r"C:\Users\slava\python\snake\Photo\back.png")
    return pygame.transform.scale(background_image, (1080, 720))
def start_game():
    background_image = load_background(WINDOW_WIDTH, WINDOW_HEIGHT)
    canvas.blit(background_image, (0, 0))
    music_button_image = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\music.png'),  (60, 60))
    music_button_rect = music_button_image.get_rect(topleft=(WINDOW_WIDTH - 140, 6))
    start_font1 = large_font.render("Snake game", True,(37,40,55))  # Оставляем надпись "Snake game"
    start_font2 = medium_font.render("Play Game", True, (33, 205, 31), (95, 235, 200))
    start_font3 = medium_font.render("Settings", True, (33, 205, 31), (95, 235, 200))
    start_font4 = medium_font.render("Quit", True, (33, 205, 31),(95, 235, 200))

    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()

    start_font1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)

    # Выравнивание кнопок по центру
    start_font2_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    start_font3_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50)
    start_font4_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 100)
    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_font3_rect.collidepoint(x, y):
                    start_inst(start_font1, start_font1_rect)
                if start_font2_rect.collidepoint(x, y):
                    gameloop()
                if start_font4_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

                pygame.display.update()



def start_inst(start_font1, start_font1_rect):
    global snake_img, body_img
    background_image = load_settings_background(WINDOW_WIDTH, WINDOW_HEIGHT)
    canvas.blit(background_image, (0, 0))


    button_width = 90
    button_height = 150
    button_margin = 20
    total_buttons_width = button_width * 3 + button_margin * 2
    button_x = (WINDOW_WIDTH - total_buttons_width) // 2
    button1_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\headmenu.png'), (button_width, button_height))
    button2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\headmenu1.png'), (button_width, button_height))
    button3_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\headmenu2.png'), (button_width, button_height))

    button1_x = (WINDOW_WIDTH - total_buttons_width) // 1.8
    button2_x = button1_x + button_width + button_margin
    button3_x = button2_x + button_width + button_margin

    button1_rect = button1_img.get_rect(center=(button1_x, WINDOW_HEIGHT / 2.3))
    button2_rect = button2_img.get_rect(center=(button2_x, WINDOW_HEIGHT / 2.3))
    button3_rect = button3_img.get_rect(center=(button3_x, WINDOW_HEIGHT / 2.3))

    canvas.blit(button1_img, button1_rect)
    canvas.blit(button2_img, button2_rect)
    canvas.blit(button3_img, button3_rect)

    start_inst5 = medium_font.render("Back", True, (33, 205, 31), (95, 235, 200))
    start_inst5_rect = start_inst5.get_rect(center=(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100))
    canvas.blit(start_inst5, start_inst5_rect)

    skin_label = medium_font.render("Skin", True, (33, 205, 31), (95, 235, 200))
    skin_label_rect = skin_label.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 150))
    canvas.blit(skin_label, skin_label_rect)

    music_button_image = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\music.png'), (50, 50))
    music_button_rect = music_button_image.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5 + 150))
    canvas.blit(music_button_image, music_button_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
                if button1_rect.collidepoint(x, y):  # If the first button is clicked
                    snake_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\head.png'), (80, 110))
                    body_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\body13.png'), (110, 140))
                elif button2_rect.collidepoint(x, y):  # If the second button is clicked
                    snake_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\head1.png'), (90, 120))
                    body_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\body1.png'), (105, 135))
                elif button3_rect.collidepoint(x, y):  # If the third button is clicked
                    snake_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\head2.png'), (100, 120))
                    body_img = pygame.transform.scale(pygame.image.load(r'C:\Users\slava\python\snake\Photo\body2.png'), (100, 130))
                if music_button_rect.collidepoint(x, y):  # If the music button is clicked
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

def gameover():
    canvas.fill(BLACK)
    font_gameover1 = large_font.render('GAME OVER', True,RED)
    font_gameover2 = medium_font.render("Play Again", True,(33, 205, 31), (95, 235, 200))
    font_gameover3 = medium_font.render("Return to menu", True, (33, 205, 31), (95, 235, 200))
    font_gameover1_rect = font_gameover1.get_rect()
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover3_rect = font_gameover3.get_rect()
    font_gameover1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
    font_gameover2_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    font_gameover3_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50)

    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if font_gameover2_rect.collidepoint(x, y):
                    gameloop()
                if font_gameover3_rect.collidepoint(x, y):
                    start_game()
                    return
        pygame.display.update()


def snake(snakelist, direction):
    head_hitbox = pygame.Rect(snakelist[-1][0], snakelist[-1][1], 10, 10)
    body_image = body_img.copy()
    if direction == 'right':
        body_image = pygame.transform.rotate(body_img, 90)
    elif direction == 'left':
        body_image = pygame.transform.rotate(body_img, 270)
    elif direction == 'up':
        body_image = body_img
    elif direction == 'down':
        body_image = pygame.transform.rotate(body_img, 180)
    for i in range(len(snakelist) - 1, 0, -1):
        segment = snakelist[i]
        next_segment = snakelist[i - 1]
        body_rect = body_image.get_rect(center=(segment[0] + SNAKE_WIDTH // 2, segment[1] + SNAKE_WIDTH // 2))
        canvas.blit(body_image, body_rect)
    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
    elif direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
    elif direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)

    head_rect = head.get_rect()
    head_rect.center = (snakelist[-1][0] + SNAKE_WIDTH // 2, snakelist[-1][1] + SNAKE_WIDTH // 2)
    canvas.blit(head, head_rect)

    return head_hitbox

def game_paused():
    paused_font1 = large_font.render("Game Paused", True, RED)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(paused_font1, paused_font_rect1)
    pygame.display.update()
    pygame.mixer.music.pause()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        pygame.mixer.music.unpause()
                        return False
        pygame.display.update()
    return True


def generate_apple():
    half_width = WINDOW_WIDTH // 1
    half_height = WINDOW_HEIGHT // 1
    APPLE_X = random.randint(0, half_width - APPLE_SIZE)
    APPLE_Y = random.randint(TOP_WIDTH, half_height - APPLE_SIZE)
    return APPLE_X, APPLE_Y


def gameloop():

    LEAD_X = 0
    LEAD_Y = 100
    direction = 'right'
    score = small_font.render("Score:0", True, YELLOW)
    APPLE_X, APPLE_Y = generate_apple()
    snakelist = []
    snakelength = 7
    paused = False

    background_image = pygame.transform.scale(pygame.image.load(r"C:\Users\slava\python\snake\Photo\back1.png"), (1080, 720))
    pause_button_image = pygame.transform.scale(pygame.image.load(r"C:\Users\slava\python\snake\Photo\pause.png"), (60, 60))
    pause_button_rect = pause_button_image.get_rect(topleft=(WINDOW_WIDTH - 70, 6 ))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != 'right':
                        direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    if direction != 'left':
                        direction = 'right'
                elif event.key == pygame.K_UP:
                    if direction != 'down':
                        direction = 'up'
                elif event.key == pygame.K_DOWN:
                    if direction != 'up':
                        direction = 'down'
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        game_paused()
                if music_button_rect.collidepoint(pause_xy):
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        if not paused:
            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    gameover()
            elif direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > WINDOW_HEIGHT - SNAKE_WIDTH:
                    gameover()
            elif direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > WINDOW_WIDTH - SNAKE_WIDTH:
                    gameover()
            elif direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    gameover()

            snakehead = [LEAD_X, LEAD_Y]
            snakelist.append(snakehead)

            if len(snakelist) > snakelength:
                del snakelist[0]

            for point in snakelist[:-1]:
                if point == snakehead:
                    gameover()

            canvas.blit(background_image, (0, 0))

            snake(snakelist, direction)

            snake_head_rect = pygame.Rect(snakelist[-1][0], snakelist[-1][1], SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            if snake_head_rect.colliderect(apple_rect):
                APPLE_X, APPLE_Y = generate_apple()
                snakelength += 1
                score = small_font.render("Score:" + str(snakelength - 7), True, YELLOW)
            canvas.blit(score, (20, 20))
            pygame.draw.line(canvas, (0,0,0), (0, TOP_WIDTH - 2), (WINDOW_WIDTH, TOP_WIDTH - 2), 3)
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            canvas.blit(pause_button_image, pause_button_rect.topleft)
            canvas.blit(music_button_image, music_button_rect.topleft)
        else:
            game_paused()
        pygame.display.update()
        clock.tick(FPS)

start_game()
gameloop()
