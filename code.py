import streamlit as st
import time
import random

# --- PAGE CONFIGURATION & PINTEREST-INSPIRED DARK FEMININE THEME ---
st.set_page_config(page_title="✨ study space", page_icon="🥀", layout="centered")

# Custom CSS to completely revamp Streamlit's default look
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #161517;
        color: #E3DCD2;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Style the buttons */
    .stButton>button {
        background-color: #322A2E !important;
        color: #DDA7A5 !important;
        border: 1px solid #4A3E44 !important;
        border-radius: 20px !important;
        padding: 0.5rem 2rem !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #DDA7A5 !important;
        color: #161517 !important;
        border-color: #DDA7A5 !important;
        box-shadow: 0px 0px 10px rgba(221, 167, 165, 0.4);
    }
    /* Elegant text styling */
    h1 {
        color: #DDA7A5 !important;
        font-weight: 300 !important;
        letter-spacing: 2px;
    }
    .quote-box {
        background-color: #1F1C1E;
        border-left: 3px solid #9A8194;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        font-style: italic;
        color: #C3B3A9;
    }
    .break-box {
        background-color: #241E22;
        border: 1px dashed #A78BFA;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        color: #E2D9E2;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATA POOLS ---
MOTIVATIONAL_QUOTES = [
    "“She remembered who she was and the game changed.”",
    "Quietly building your empire. Keep going, lovely.",
    "“The future belongs to those who believe in the beauty of their dreams.” — Eleanor Roosevelt",
    "Romanticize the discipline. The focus looks beautiful on you.",
    "Small steps every single day. You are closer than you were yesterday. ✨",
    "“Energy flows where attention goes.” Focus beautifully.",
    "Prove it to yourself, not to them."
]

BREAK_ACTIVITIES = [
    "☕ Step away and fix yourself a warm cup of matcha or tea.",
    "🧘‍♀️ Do a quick 2-minute shoulder roll and neck stretch.",
    "🌱 Water a plant or look out the window at the sky to rest your eyes.",
    "💃 Put on your favorite track and just stretch/move around for 3 minutes.",
    "💧 Take 5 deep breaths and refill your water bottle.",
    "journal page: Write down three things you're grateful for right now."
]

# --- APP INTERFACE ---
st.title("🥀 romanticize the grind.")
st.caption("a minimalist stopwatch for deep, beautiful focus.")

# Initialize session state variables to track time across clicks
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "running" not in st.session_state:
    st.session_state.running = False
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0

# Sidebar configuration for custom settings
with st.sidebar:
    st.markdown("### ⏳ Interval Adjustments")
    quote_interval = st.number_input("Motivation Interval (Mins)", value=15, min_value=1)
    break_interval = st.number_input("Break Suggestion Interval (Mins)", value=20, min_value=1)
    st.markdown("---")
    st.markdown("*Tip: Shrink your browser window down to just show the timer text, and place it in the corner of your screen!*")

# Create simple control layout
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✨ Start / Resume"):
        if not st.session_state.running:
            st.session_state.start_time = time.time() - st.session_state.elapsed_time
            st.session_state.running = True

with col2:
    if st.button("⏳ Pause"):
        if st.session_state.running:
            st.session_state.elapsed_time = time.time() - st.session_state.start_time
            st.session_state.running = False

with col3:
    if st.button("🥀 Reset"):
        st.session_state.start_time = None
        st.session_state.running = False
        st.session_state.elapsed_time = 0
        st.rerun()

# --- THE LIVE TIMER LOOP ---
timer_display = st.empty()
quote_display = st.empty()
break_display = st.empty()

# Keep refreshing the page if the stopwatch is ticking
while st.session_state.running:
    # Calculate exactly how long it's been running
    current_elapsed = time.time() - st.session_state.start_time
    
    # Calculate minutes and seconds
    hours, remainder = divmod(int(current_elapsed), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Update the big beautiful aesthetic clock display
    timer_display.markdown(
        f"<h1 style='font-size: 65px; font-weight: 200; text-align: center; color: #DDA7A5;'>{hours:02d}:{minutes:02d}:{seconds:02d}</h1>", 
        unsafe_allow_html=True
    )
    
    # Check for the 15-Minute Motivation Trigger
    # Using dynamic calculation so it updates seamlessly when a new interval is reached
    current_total_minutes = int(current_elapsed // 60)
    
    if current_total_minutes > 0 and current_total_minutes % quote_interval == 0:
        # Pick a pseudo-random quote based on the current interval index so it doesn't flip every second
        quote_idx = (current_total_minutes // quote_interval) % len(MOTIVATIONAL_QUOTES)
        quote_display.markdown(
            f"<div class='quote-box'><b>Gentle Reminder:</b><br>{MOTIVATIONAL_QUOTES[quote_idx]}</div>", 
            unsafe_allow_html=True
        )
    else:
        quote_display.empty()
        
    # Check for the 20-Minute Break Suggestion Trigger
    if current_total_minutes > 0 and current_total_minutes % break_interval == 0:
        break_idx = (current_total_minutes // break_interval) % len(BREAK_ACTIVITIES)
        break_display.markdown(
            f"<div class='break-box'><b>☕ Lap Marker Reached:</b><br>{BREAK_ACTIVITIES[break_idx]}</div>", 
            unsafe_allow_html=True
        )
    else:
        break_display.empty()

    time.sleep(1)
    st.rerun()

# Static display if the timer is paused or has not started yet
if not st.session_state.running:
    hours, remainder = divmod(int(st.session_state.elapsed_time), 3600)
    minutes, seconds = divmod(remainder, 60)
    timer_display.markdown(
        f"<h1 style='font-size: 65px; font-weight: 200; text-align: center; color: #9A8194;'>{hours:02d}:{minutes:02d}:{seconds:02d}</h1>", 
        unsafe_allow_html=True
    )
