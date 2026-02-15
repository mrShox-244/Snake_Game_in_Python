import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Menu")

font_big = pygame.font.SysFont(None, 80)
font_small = pygame.font.SysFont(None, 40)

WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
DARK_GRAY = (60, 60, 60)
LIGHT_BLUE = (50, 150, 255)

clock = pygame.time.Clock()


def draw_text(text, font, color, x, y):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(x, y))
    screen.blit(surf, rect)


def button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # наведение мыши
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, LIGHT_BLUE, (x, y, w, h), border_radius=10)
        hover = True
    else:
        pygame.draw.rect(screen, DARK_GRAY, (x, y, w, h), border_radius=10)
        hover = False

    draw_text(text, font_small, WHITE, x + w//2, y + h//2)

    if hover and click[0] == 1:
        return True

    return False


def show_records():
    screen.fill((20, 20, 30))

    draw_text("RECORDS", font_big, WHITE, WIDTH//2, 80)

    if not os.path.exists("records.txt"):
        draw_text("No records yet", font_small, WHITE, WIDTH//2, 200)
    else:
        with open("records.txt", "r") as f:
            score = f.read()

        draw_text(f"BEST SCORE: {score}", font_small, WHITE, WIDTH//2, 200)

    draw_text("Press ESC to return", font_small, GRAY, WIDTH//2, 550)

    pygame.display.flip()

    # ожидание выхода
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return


def main_menu():
    while True:
        screen.fill((20, 20, 30))

        draw_text("SNAKE", font_big, WHITE, WIDTH//2, 120)

        if button("PLAY", 200, 250, 200, 60):
            return "play"

        if button("RECORDS", 200, 350, 200, 60):
            show_records()

        if button("EXIT", 200, 450, 200, 60):
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)
