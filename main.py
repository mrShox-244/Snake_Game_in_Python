import pygame
import sys
import os
from snake import Snake
from food import Food

pygame.init()

WIDTH, HEIGHT = 600, 600
SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Importing .png's files
snake_img = pygame.image.load("snake.png")
snake_img = pygame.transform.scale(snake_img, (SIZE, SIZE))

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (SIZE, SIZE))

RECORD_FILE = "records.txt"
if not os.path.exists(RECORD_FILE):
    with open(RECORD_FILE, "w") as f:
        f.write("0")


with open(RECORD_FILE, "r") as f:
    best_score = int(f.read())

font_score = pygame.font.SysFont(None, 40)

def draw_score(score):
    text = font_score.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_loop():
    global best_score
    #Creating the Snake and Food
    snake = Snake(SIZE, 100, 100)
    food = Food(WIDTH, HEIGHT, SIZE)
    score = 0#The score in the start of the game

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # keybinding
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.change_direction("LEFT")
        if keys[pygame.K_RIGHT]:
            snake.change_direction("RIGHT")
        if keys[pygame.K_UP]:
            snake.change_direction("UP")
        if keys[pygame.K_DOWN]:
            snake.change_direction("DOWN")

        snake.move()

        # Checking the collision
        head_x, head_y = snake.segments[0]
        #Collision with walls
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            break
        # Collision with snake
        if snake.segments[0] in snake.segments[1:]:
            break

        # Проверка еды
        if snake.get_head_rect().colliderect(food.get_rect()):
            snake.grow = True
            food.respawn()
            score += 1
            if score > best_score:
                best_score = score
                with open(RECORD_FILE, "w") as f:
                    f.write(str(best_score))

        #Creating the area
        screen.fill((40, 40, 40))
        for x, y in snake.segments:
            screen.blit(snake_img, (x, y))
        screen.blit(apple_img, (food.x, food.y))
        draw_score(score)

        pygame.display.flip()
        clock.tick(15)

    # Game Over экран
    font = pygame.font.SysFont(None, 70)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.fill((20, 20, 20))
    screen.blit(text, (150, 250))
    pygame.display.flip()
    pygame.time.wait(2000)


def menu():
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 40)

    while True:
        screen.fill((30, 30, 30))
        title = font.render("SNAKE GAME", True, (0, 255, 0))
        play_btn = small_font.render("1. PLAY", True, (255, 255, 255))
        exit_btn = small_font.render("2. EXIT", True, (255, 255, 255))
        record_btn = small_font.render("3. RECORD", True, (255, 255, 255))

        screen.blit(title, (180, 150))
        screen.blit(play_btn, (240, 300))
        screen.blit(exit_btn, (240, 360))
        screen.blit(record_btn, (240, 420))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "play"
                if event.key == pygame.K_2:
                    return "exit"
                if event.key == pygame.K_3:
                    return "record"

def show_record():
    screen.fill((20, 20, 30))
    font = pygame.font.SysFont(None, 60)
    text = font.render(f"BEST SCORE: {best_score}", True, (255, 255, 255))
    screen.blit(text, (150, 250))
    pygame.display.flip()
    pygame.time.wait(2000)


# Main Loop
while True:
    choice = menu()
    if choice == "play":
        game_loop()
    elif choice == "record":
        show_record()
    elif choice == "exit":
        pygame.quit()
        sys.exit()















