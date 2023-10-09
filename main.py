import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Minecraft")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100

    def update(self):
        # Player movement logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Player collision with monsters
        if pygame.sprite.spritecollide(self, monsters, True):
            self.health -= 10

        # Player health bar
        pygame.draw.rect(win, RED, (self.rect.x, self.rect.y - 10, 30, 5))
        pygame.draw.rect(win, WHITE, (self.rect.x, self.rect.y - 10, self.health / 100 * 30, 5))

# Monster class
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Monster movement logic
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)

# Create sprite groups
all_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()

# Create player and monsters
player = Player(100, 100)
all_sprites.add(player)

for _ in range(5):
    monster = Monster(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(monster)
    monsters.add(monster)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Render
    win.fill(WHITE)
    all_sprites.draw(win)
    pygame.display.flip()

# Quit the game
pygame.quit()
