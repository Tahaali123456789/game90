import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.title("2D Racing Game - Canvas Simulation")

# Set up canvas
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=2,
    stroke_color="black",
    background_color="#DDD",
    width=500,
    height=700,
    drawing_mode="none",
    key="canvas",
)

# Game Variables
car_x, car_y = 225, 600  # Car starting position
obstacle_x = random.randint(0, 450)  # Random obstacle position
obstacle_y = 0
obstacle_speed = 5

# Display car and obstacle
st.write("🚗 Car Position:", car_x, car_y)
st.write("🚧 Obstacle Position:", obstacle_x, obstacle_y)

# Game loop
if st.button("Move Left"):
    car_x -= 10
if st.button("Move Right"):
    car_x += 10

# Move obstacle
obstacle_y += obstacle_speed
if obstacle_y > 700:
    obstacle_y = 0
    obstacle_x = random.randint(0, 450)

# Detect collision
if abs(car_x - obstacle_x) < 50 and abs(car_y - obstacle_y) < 50:
    st.write("Collision Detected! Game Over.")
