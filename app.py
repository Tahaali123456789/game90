import streamlit as st
import random

st.title("2D Racing Game - Simplified Simulation")

# Initialize game variables in session state if not already set
if "game_data" not in st.session_state:
    st.session_state.game_data = {
        "car_x": 5,
        "car_y": 10,
        "grid_width": 10,
        "obstacle_x": random.randint(0, 10),
        "obstacle_y": 0,
        "score": 0,
        "game_over": False
    }

game_data = st.session_state.game_data

# Display game state
st.write(f"Score: {game_data['score']}")
st.write(f"🚗 Car Position: ({game_data['car_x']}, {game_data['car_y']})")
st.write(f"🚧 Obstacle Position: ({game_data['obstacle_x']}, {game_data['obstacle_y']})")

# Update car position based on button click if the game is not over
if not game_data["game_over"]:
    if st.button("Move Left") and game_data["car_x"] > 0:
        game_data["car_x"] -= 1
    if st.button("Move Right") and game_data["car_x"] < game_data["grid_width"]:
        game_data["car_x"] += 1

    # Move obstacle down
    game_data["obstacle_y"] += 1
    if game_data["obstacle_y"] > 10:  # Reset obstacle when it goes off screen
        game_data["obstacle_y"] = 0
        game_data["obstacle_x"] = random.randint(0, game_data["grid_width"])
        game_data["score"] += 1

    # Check for collision
    if game_data["car_x"] == game_data["obstacle_x"] and game_data["car_y"] == game_data["obstacle_y"]:
        game_data["game_over"] = True

# Display game status
if game_data["game_over"]:
    st.write("💥 Collision Detected! Game Over.")
else:
    st.write("Keep going!")  # Only shows when the game is still on
