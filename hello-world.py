import pygame
import random

# Boshlanish
pygame.init()

# Oyna o'lchami
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
BLUE = (50, 150, 255)

# O'yinchi
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Coin (tanga)
coin_radius = 10
coin_x = random.randint(coin_radius, WIDTH - coin_radius)
coin_y = random.randint(coin_radius, HEIGHT - coin_radius)

# Ball
score = 0
font = pygame.font.SysFont("Arial", 30)

# FPS
clock = pygame.time.Clock()

# O'yin sikli
run = True
while run:
    clock.tick(60)
    win.fill(BLACK)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(win, BLUE, player_rect)
    pygame.draw.circle(win, GOLD, (coin_x, coin_y), coin_radius)

    if player_rect.collidepoint(coin_x, coin_y):
        score += 1
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coin_y = random.randint(coin_radius, HEIGHT - coin_radius)

    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
