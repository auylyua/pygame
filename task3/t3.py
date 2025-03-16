import pygame
import sys

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))

ball_color = (255, 0, 0)
bg_color = (255, 255, 255)
ball_radius = 25
ball_x, ball_y = w // 2, h // 2
step = 20

running = True
while running:
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_radius - step >= 0:
                ball_y -= step
            if event.key == pygame.K_DOWN and ball_y + ball_radius + step <= h:
                ball_y += step
            if event.key == pygame.K_LEFT and ball_x - ball_radius - step >= 0:
                ball_x -= step
            if event.key == pygame.K_RIGHT and ball_x + ball_radius + step <= w:
                ball_x += step

    pygame.display.flip()

pygame.quit()
sys.exit()
