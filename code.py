import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="✨ Aesthetic Space", page_icon="🥀", layout="centered")

# --- THEME PALETTES DICTIONARY ---
THEMES = {
    "🥀 Persephone's Descent": {
        "bg": "#140B0B",       # A Garnet's Touch
        "card": "#471417",     # Miles Of Persephone
        "text": "#CD9454",     # Juno's Emblem
        "accent": "#A22737",   # Arresting Appeal
        "muted": "#660611"     # Passion Unraveled
    },
    "🌿 Botanical Solace": {
        "bg": "#043323",       # Dark green
        "card": "#105666",     # Midnight green
        "text": "#F7F4D5",     # Beige
        "accent": "#839050",   # Moss green
        "muted": "#039680"     # Rosy brown/teal accent
    },
    "🏺 Gilded Bistre": {
        "bg": "#210100",       # Bistre
        "card": "#814436",     # Indian Red
        "text": "#FECE79",     # Butter
        "accent": "#E64341",   # Goldfinch
        "muted": "#8C0902"     # Garnet
    },
    "🔮 Cyber Orchid": {
        "bg": "#3D1472",       # Persian Indigo
        "card": "#3333AF",     # Blue Depression
        "text": "#FA8EE4",     # Pink Wink
        "accent": "#9896FF",   # Gobalite
        "muted": "#B744B5"     # Purple Ink
    },
    "🌊 Tropical Sea Foam": {
        "bg": "#076DDF",       # Deep Sky
        "card": "#19887F",     # Palm Splash
        "text": "#DAF6F6",     # Sea Foam
        "accent": "#92F1EC",   # Crystal Clear
        "muted": "#35AEAC"     # Tropical Sea
    },
    "🦩 Poolside Barbie": {
        "bg": "#227E9D",       # Pool Bottom
        "card": "#51ACC5",     # Dragonity
        "text": "#FDF9FA",     # Abalone
        "accent": "#FDA9CC",   # Cotton Candy
        "muted": "#FD50A4"     # Barbie Pink
    },
    "☀️ Sun-Drenched Apricot": {
        "bg": "#FA9058",       # Sè Lời Orange
        "card": "#FECC64",     # Quing Yellow
        "text": "#FFF6E8",     # Apricot Ice
        "accent": "#FCEABC",   # Sun Drenched
        "muted": "#B5D8FF"     # Azure Sky
    },
    "🍁 Autumnal Alchemy": {
        "bg": "#13260F",       # Salamander
        "card": "#344F30",     # Palm Leaf
        "text": "#FDD973",     # Golden Coin
        "accent": "#F47230",   # Liselotte Syrup
        "muted": "#9F350B"     # Carmin
    }
}

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.markdown("### 🎨 Choose Your Vibe")
    selected_theme_name = st.selectbox("Current Theme", list(THEMES.keys()))
    
    st.markdown("---")
    st.markdown("### ⏳ Intervals")
    quote_interval = st.number_input("Motivation Interval (Mins)", value=15, min_value=1)
    break_interval = st.number_input("Break Suggestion Interval (Mins)", value=20, min_value=1)

active_theme = THEMES[selected_theme_name]

# --- INJECT CUSTOM CSS ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {active_theme['bg']} !important;
        color: {active_theme['text']} !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        transition: all 0.5s ease;
    }}
    [data-testid="stSidebar"] {{
        background-color: {active_theme['card']} !important;
        border-right: 1px solid {active_theme['accent']}33;
    }}
    [data-testid="stSidebar"] * {{
        color: {active_theme['text']} !important;
    }}
    .stButton>button {{
        background-color: {active_theme['card']} !important;
        color: {active_theme['accent']} !important;
        border: 1px solid {active_theme['accent']}66 !important;
        border-radius: 24px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 300 !important;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {active_theme['accent']} !important;
        color: {active_theme['bg']} !important;
        border-color: {active_theme['accent']} !important;
        box-shadow: 0px 0px 15px {active_theme['accent']}66;
    }}
    .quote-box {{
        background-color: {active_theme['card']}bf;
        border-left: 3px solid {active_theme['accent']};
        padding: 18px;
        border-radius: 12px;
        margin: 22px 0;
        font-style: italic;
        color: {active_theme['text']};
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        line-height: 1.5;
    }}
    .break-box {{
        background-color: {active_theme['card']}bf;
        border: 1px dashed {active_theme['muted']};
        padding: 18px;
        border-radius: 12px;
        margin: 22px 0;
        color: {active_theme['text']};
        line-height: 1.5;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 30 QUOTES BY SUCCESSFUL WOMEN ---
MOTIVATIONAL_QUOTES = [
    "“The most effective way to do it, is to do it.” — Amelia Earhart",
    "“I never dreamed about success. I worked for it.” — Estée Lauder",
    "“Define success on your own terms, achieve it by your own rules, and build a life you’re proud to live.” — Anne Sweeney",
    "“I'm not intimidating, you're intimidated. There's a difference.” — Issa Rae",
    "“You can waste your lives drawing lines. Or you can live your life crossing them.” — Shonda Rhimes",
    "“Think like a queen. A queen is not afraid to fail. Failure is another steppingstone to greatness.” — Oprah Winfrey",
    "“The power you have is to be the best version of yourself you can be, so you can create a better world.” — Ashley Graham",
    "“If you don't risk anything, you risk even more.” — Erica Jong",
    "“Nothing is impossible, the word itself says 'I'm possible!'” — Audrey Hepburn",
    "“If you’re clear on what you believe, you have a great foundation to step out into the world.” — Sanna Marin",
    "“We do not need magic to change the world, we carry all the power we need inside ourselves already.” — J.K. Rowling",
    "“Passion is energy. Feel the power that comes from focusing on what excites you.” — Oprah Winfrey",
    "“Don't watch the clock; do what it does. Keep going.” — Sam Levenson",
    "“I am not free while any woman is unfree, even when her shackles are very different from my own.” — Audre Lorde",
    "“You may encounter many defeats, but you must not be defeated.” — Maya Angelou",
    "“Done is better than perfect.” — Sheryl Sandberg",
    "“The most common way people give up their power is by thinking they don't have any.” — Alice Walker",
    "“If they don't give you a seat at the table, bring a folding chair.” — Shirley Chisholm",
    "“Success isn't about how much money you make, it's about the difference you make in people's lives.” — Michelle Obama",
    "“Never limit yourself because of others’ limited imagination; never limit others because of your own limited imagination.” — Dr. Mae Jemison",
    "“You cannot leave footprints in the sands of time if you are sitting on your butt. And who wants to leave buttprints?” — Bobbie Thomas",
    "“It is within everyone's power to rewrite their story.” — Mindy Kaling",
    "“I naturally look at the world as something that needs to be explored, not feared.” — Sophia Amoruso",
    "“I’ve learned that making a 'living' is not the same thing as making a 'life.'” — Maya Angelou",
    "“Do one thing every day that scares you.” — Eleanor Roosevelt",
    "“The desire to reach for the stars is ambitious. The desire to reach hearts is wise.” — Maya Angelou",
    "“Turn your wounds into wisdom.” — Oprah Winfrey",
    "“Hard work keeps the wrinkles out of the mind and spirit.” — Helena Rubinstein",
    "“You have to look at your career and your life as a collection of horizons.” — Indra Nooyi",
    "“Be messy and complicated and afraid and show up anyway.” — Glennon Doyle"
]

# --- REFRESHED BREAK OPTIONS WITH YOUR REQS ---
BREAK_ACTIVITIES = [
    "📝 write 3 things ur thankful for in journal",
    "🧊 get some ice water",
    "🧘‍♀️ Lie on the floor and stare at the ceiling",
    "☕ Step away and fix yourself a warm cup of matcha or herbal tea.",
    "🌱 Water a plant or look out the window at the sky to completely rest your eyes.",
    "💃 Put on your current favorite track and just move around freely for 3 minutes."
]

# --- APP INTERFACE ---
st.title("🥀 Study Ritual.")
st.caption(f"currently vibrating in: {selected_theme_name.lower()}")

# State Management for Stopwatch
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "running" not in st.session_state:
    st.session_state.running = False
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0

# Controls Layout
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✨ Start"):
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

# Dynamic Placeholders
timer_display = st.empty()
quote_display = st.empty()
break_display = st.empty()

# --- STOPWATCH LIVE EXECUTION LOOP ---
while st.session_state.running:
    current_elapsed = time.time() - st.session_state.start_time
    
    hours, remainder = divmod(int(current_elapsed), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Large Elegant Display
    timer_display.markdown(
        f"<h1 style='font-size: 70px; font-weight: 200; text-align: center; color: {active_theme['text']};'>{hours:02d}:{minutes:02d}:{seconds:02d}</h1>", 
        unsafe_allow_html=True
    )
    
    current_total_minutes = int(current_elapsed // 60)
    
    # Quote trigger loop logic
    if current_total_minutes > 0 and current_total_minutes % quote_interval == 0:
        quote_idx = (current_total_minutes // quote_interval) % len(MOTIVATIONAL_QUOTES)
        quote_display.markdown(
            f"<div class='quote-box'><b>From a woman who built her empire:</b><br>{MOTIVATIONAL_QUOTES[quote_idx]}</div>", 
            unsafe_allow_html=True
        )
    else:
        quote_display.empty()
        
    # Break idea trigger loop logic
    if current_total_minutes > 0 and current_total_minutes % break_interval == 0:
        break_idx = (current_total_minutes // break_interval) % len(BREAK_ACTIVITIES)
        break_display.markdown(
            f"<div class='break-box'><b>☕ Time to reset:</b><br>{BREAK_ACTIVITIES[break_idx]}</div>", 
            unsafe_allow_html=True
        )
    else:
        break_display.empty()

    time.sleep(1)
    st.rerun()

# Static Display
if not st.session_state.running:
    hours, remainder = divmod(int(st.session_state.elapsed_time), 3600)
    minutes, seconds = divmod(remainder, 60)
    timer_display.markdown(
        f"<h1 style='font-size: 70px; font-weight: 200; text-align: center; color: {active_theme['accent']};'>{hours:02d}:{minutes:02d}:{seconds:02d}</h1>", 
        unsafe_allow_html=True
    )
