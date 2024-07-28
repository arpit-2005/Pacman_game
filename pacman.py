import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set up the player and ghost positions
player = [300, 300]
ghosts = [[100, 100], [500, 100], [100, 500], [500, 500]]

# Set up the dot positions
dots = [[random.randint(0, 790), random.randint(0, 590)] for _ in range(10)]

# Set up the game variables
score = 0
lives = 3

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player[0] -= 5
    if keys[pygame.K_RIGHT]:
        player[0] += 5
    if keys[pygame.K_UP]:
        player[1] -= 5
    if keys[pygame.K_DOWN]:
        player[1] += 5

    # Keep the player on the screen
    player[0] = max(0, min(player[0], 790))
    player[1] = max(0, min(player[1], 590))

    # Move the ghosts
    for ghost in ghosts:
        ghost[0] += random.choice([-3, 3])
        ghost[1] += random.choice([-3, 3])

        # Keep the ghosts on the screen
        ghost[0] = max(0, min(ghost[0], 790))
        ghost[1] = max(0, min(ghost[1], 590))

    # Check for collisions with dots
    for dot in dots:
        if abs(player[0] - dot[0]) < 20 and abs(player[1] - dot[1]) < 20:
            score += 1
            dots.remove(dot)

    # Check for collisions with ghosts
    for ghost in ghosts:
        if abs(player[0] - ghost[0]) < 20 and abs(player[1] - ghost[1]) < 20:
            lives -= 1
            player = [300, 300]

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), (player[0], player[1], 20, 20))
    for ghost in ghosts:
        pygame.draw.rect(screen, (255, 0, 0), (ghost[0], ghost[1], 20, 20))
    for dot in dots:
        pygame.draw.rect(screen, (255, 255, 255), (dot[0], dot[1], 10, 10))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)