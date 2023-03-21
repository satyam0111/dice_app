import random
import streamlit as st

global_roll1 = 0
global_roll2 = 0

# Set up player names
player1 = st.text_input("Enter Player 1 name:")
player2 = st.text_input("Enter Player 2 name:")

# Define function to roll dice
def roll_dice():
    roll = random.randint(1, 6)
    return roll

def update_rolls():
    global global_roll1, global_roll2
    global_roll1 = roll_dice()
    global_roll2 = roll_dice()
    
update_rolls()

st.write(f"{player1} rolled a {global_roll1}")
st.write(f"{player2} rolled a {global_roll2}")

if global_roll1 > global_roll2:
    st.write(f"{player1} WINS !!")
else:
    st.write(f"{player2} WINS !!")
