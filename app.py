import streamlit as st
import random

st.title("2D Racing Game - Simplified Simulation")

# Initialize game variables in session state
if "initialized" not in st.session_state:
    st.session_state.car_x = 5
    st.session_state.car_y = 10
    st.session_state.grid_width = 10
    st.session_state.obstacle_x = random.randint(0, st.session_state.grid_width)
    st.session_state.obstacle_y = 0
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.initialized = True  # Flag to indicate initialization

# Display game state
st.write(f"Score: {st.session_state.score}")
st.write(f"🚗 Car Position: ({st.session_state.car_x}, {st.session_state.car_y})")
st.write(f"🚧 Obstacle Position: ({st.session_state.obstacle_x}, {st.session_state.obstacle_y})")

# Move car based on button clicks if the game is not over
if not st.session_state.game_over:
    if st.button("Move Left") and st.session_state.car_x > 0:
        st.session_state.car_x -= 1
    if st.button("Move Right") and st.session_state.car_x < st.session_state.grid_width:
        st.session_state.car_x += 1

    # Move obstacle down
    st.session_state.obstacle_y += 1
    if st.session_state.obstacle_y > 10:  # Reset obstacle when it goes off screen
        st.session_state.obstacle_y = 0
        st.session_state.obstacle_x = random.randint(0, st.session_state.grid_width)
        st.session_state.score += 1

    # Check collision
    if (
        st.session_state.car_x == st.session_state.obstacle_x
        and st.session_state.car_y == st.session_state.obstacle_y
    ):
        st.session_state.game_over = True
        st.write("💥 Collision Detected! Game Over.")
    else:
        st.write("Keep going!")  # Only shows when the game is still on
else:
    st.write("💥 Collision Detected! Game Over.")
