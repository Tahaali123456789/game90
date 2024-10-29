import streamlit as st
import random
import time

st.title("2D Racing Game - Simplified Simulation")

# Game Variables
car_x, car_y = 5, 10  # Car starting position in a grid format
grid_width = 10
obstacle_x = random.randint(0, grid_width)
obstacle_y = 0
score = 0

# Game Loop
while True:
    # Display game state
    st.write(f"Score: {score}")
    st.write("🚗 Car Position:", (car_x, car_y))
    st.write("🚧 Obstacle Position:", (obstacle_x, obstacle_y))

    # Move car
    move = st.radio("Move Car", ["Left", "Right"], index=1)
    if move == "Left" and car_x > 0:
        car_x -= 1
    elif move == "Right" and car_x < grid_width:
        car_x += 1

    # Move obstacle down
    obstacle_y += 1
    if obstacle_y > 10:  # Reset obstacle when it goes off screen
        obstacle_y = 0
        obstacle_x = random.randint(0, grid_width)
        score += 1

    # Check collision
    if car_x == obstacle_x and car_y == obstacle_y:
        st.write("💥 Collision Detected! Game Over.")
        break

    # Refresh the state
    time.sleep(0.5)
    st.experimental_rerun()
