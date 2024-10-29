import pygame
import random
from pyvirtualdisplay import Display

# Set up virtual display for Colab
display = Display(visible=0, size=(800, 600))
display.start()

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 100
car = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car.fill(RED)
car_x, car_y = WIDTH // 2, HEIGHT - CAR_HEIGHT - 10
car_speed = 5

# Obstacle settings
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 100
obstacle = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle.fill(BLACK)
obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
obstacle_y = -OBSTACLE_HEIGHT
obstacle_speed = 7

clock = pygame.time.Clock()

# Main game loop
def game_loop():
    global car_x, car_y, obstacle_x, obstacle_y, obstacle_speed
    running = True
    while running:
        SCREEN.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
            car_x += car_speed

        # Move obstacle
        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_y = -OBSTACLE_HEIGHT
            obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)

        # Collision detection
        car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        if car_rect.colliderect(obstacle_rect):
            running = False

        # Draw car and obstacle
        SCREEN.blit(car, (car_x, car_y))
        SCREEN.blit(obstacle, (obstacle_x, obstacle_y))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

game_loop()


import streamlit as st
from PIL import Image
import io

st.title("2D Racing Game")

# Function to run the game and stream frames
def run_game():
    # Call game_loop and save frame as image, send to Streamlit every frame
    pass  # Placeholder: use a frame capture solution if using with Colab

if st.button("Start Game"):
    run_game()
