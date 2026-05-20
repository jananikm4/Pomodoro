import streamlit as st
import time

st.title("⏱️ Minimalist Focus Timer")

# 1. User inputs for time
focus_time = st.slider("Set Focus Time (Minutes)", 1, 60, 25)

# 2. Start Button
if st.button("Start Focusing 🚀"):
    # Convert minutes to total seconds
    total_seconds = focus_time * 60
    
    # Create an empty placeholder to update the countdown text dynamically
    timer_placeholder = st.empty()
    progress_bar = st.progress(0)
    
    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        # Format as MM:SS
        timer_placeholder.header(f"⏳ Time Remaining: {mins:02d}:{secs:02d}")
        
        # Update progress bar
        fraction_done = 1.0 - (remaining / total_seconds)
        progress_bar.progress(fraction_done)
        
        time.sleep(1) # Wait 1 second
        
    st.success("🎉 Time's up! Take a well-deserved break.")
    st.balloons()
