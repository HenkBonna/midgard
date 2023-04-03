import pygame
import random

# Define the generate_circles() function
def generate_circles(num_circles, min_size, max_size):
    circles = []
    for i in range(num_circles):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        size = random.randint(min_size, max_size)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = {'x': x, 'y': y, 'size': size, 'color': color}
        circles.append(circle)
    return circles

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Clicker")

# Set up the circle parameters
num_circles = 10
min_size, max_size = 10, 50
circles = generate_circles(num_circles, min_size, max_size)

# Set up the player parameters
player_size = 50
player_color = (0, 255, 0)
player_speed = 5
player_x = screen_width // 2
player_y = screen_height // 2
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
    elif keys[pygame.K_UP]:
        player_y -= player_speed
    elif keys[pygame.K_DOWN]:
        player_y += player_speed

    # Check for collisions between player and circles
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for circle in circles:
        circle_rect = pygame.Rect(circle['x'], circle['y'], circle['size'], circle['size'])
        if player_rect.colliderect(circle_rect):
            circles.remove(circle)
            score += 1

    # Draw everything
    screen.fill((255, 255, 255))  # White background
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], (circle['x'], circle['y']), circle['size'])
    pygame.draw.rect(screen, player_color, player_rect)
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Keep the player within the screen bounds
    player_x = max(0, min(player_x, screen_width - player_size))
    player_y = max(0, min(player_y, screen_height - player_size))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
