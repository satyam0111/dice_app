import random
import streamlit as st

# Set up player names
player1 = st.text_input("Enter Player 1 name:")
player2 = st.text_input("Enter Player 2 name:")

# Define function to roll dice
def roll_dice():
    roll = random.randint(1, 6)
    return roll

# Create button to roll dice for player 1
if st.button(f"{player1}, Roll Dice!"):
    roll1 = roll_dice()
    st.write(f"{player1} rolled a {roll1}")

# Create button to roll dice for player 2
if st.button(f"{player2}, Roll Dice!"):
    roll2 = roll_dice()
    st.write(f"{player2} rolled a {roll2}")

if roll1 > roll2:
    st.write(f"{player1} WINS !!")
elif roll1==roll2:
    st.write("No one WINS !!")
else:
    st.write(f"{player2} WINS !!")
