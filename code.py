import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="✨ I gon make it out", page_icon="🥀", layout="centered")

# --- THEME PALETTES DICTIONARY ---
THEMES = {
    "🥀 Persephone's Descent": {
        "bg": "#140B0B", "card": "#471417", "text": "#CD9454", "accent": "#A22737", "muted": "#660611"
    },
    "🌿 Botanical Solace": {
        "bg": "#043323", "card": "#105666", "text": "#F7F4D5", "accent": "#839050", "muted": "#039680"
    },
    "🏺 Gilded Bistre": {
        "bg": "#210100", "card": "#814436", "text": "#FECE79", "accent": "#E64341", "muted": "#8C0902"
    },
    "🔮 Cyber Orchid": {
        "bg": "#3D1472", "card": "#3333AF", "text": "#FA8EE4", "accent": "#9896FF", "muted": "#B744B5"
    },
    "🌊 Tropical Sea Foam": {
        "bg": "#076DDF", "card": "#19887F", "text": "#DAF6F6", "accent": "#92F1EC", "muted": "#35AEAC"
    },
    "🦩 Poolside Barbie": {
        "bg": "#227E9D", "card": "#51ACC5", "text": "#FDF9FA", "accent": "#FDA9CC", "muted": "#FD50A4"
    },
    "☀️ Sun-Drenched Apricot": {
        "bg": "#FA9058", "card": "#FECC64", "text": "#FFF6E8", "accent": "#FCEABC", "muted": "#B5D8FF"
    },
    "🍁 Autumnal Alchemy": {
        "bg": "#13260F", "card": "#344F30", "text": "#FDD973", "accent": "#F47230", "muted": "#9F350B"
    },
    "🌊 Navagio Coastline": {
        "bg": "#3F9CB0", "card": "#58DEE1", "text": "#FFD6C7", "accent": "#EB8629", "muted": "#DC4A44"
    },
    "⚡ Neon Pulse": {
        "bg": "#231F20", "card": "#0AA9E0", "text": "#7BF004", "accent": "#FC05B8", "muted": "#FA6B05"
    },
    "🌸 Pastel Dreamcicle": {
        "bg": "#594EAD", "card": "#5A9AD6", "text": "#F99E85", "accent": "#F4607B", "muted": "#78C681"
    },
    "🪵 Desert Saddle": {
        "bg": "#957443", "card": "#1FB189", "text": "#CCCCAC", "accent": "#EC321F", "muted": "#E7ABC7"
    },
    "🍓 Azure Mist & Berry": {
        "bg": "#64A4ED", "card": "#A72536", "text": "#E5FAFF", "accent": "#FA4F8E", "muted": "#FFF2A3"
    },
    "🧥 White Silk & Navy": {
        "bg": "#26386A", "card": "#75B06F", "text": "#FAE251", "accent": "#FFFFFF", "muted": "#1F2B52"
    },
    "🌅 Denim Sunshine": {
        "bg": "#3F1E17", "card": "#2E4C6D", "text": "#FFD058", "accent": "#FE422C", "muted": "#FA9743"
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
        width: 100%;
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
    .metric-card {{
        background-color: {active_theme['card']}66;
        border: 1px solid {active_theme['accent']}22;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }}
    .lap-row {{
        background-color: {active_theme['card']}40;
        border-bottom: 1px solid {active_theme['accent']}11;
        padding: 8px 16px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: {active_theme['text']};
    }}
    .break-banner {{
        background-color: {active_theme['accent']};
        color: {active_theme['bg']};
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- DATA POOLS ---
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

BREAK_ACTIVITIES = [
    "🧼 wash your face & refresh",
    "📂 Organize ONE tiny thing on your desk",
    "🎨 Doodle your thoughts on scrap paper",
    "✨ Work on making your study notes aesthetic",
    "📝 write 3 things ur thankful for in journal",
    "🧊 get some ice water",
    "🧘‍♀️ Lie on the floor and stare at the ceiling",
    "☕ Step away and fix yourself a warm cup of matcha or herbal tea.",
    "🌱 Water a plant or look out the window at the sky to completely rest your eyes.",
    "💃 Put on your current favorite track and just move around freely for 3 minutes."
]

def format_time(seconds_count):
    hours, remainder = divmod(int(seconds_count), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# --- STATE MANAGEMENT ---
if "start_time" not in st.session_state: st.session_state.start_time = None
if "running" not in st.session_state: st.session_state.running = False
if "elapsed_time" not in st.session_state: st.session_state.elapsed_time = 0
if "total_study_time" not in st.session_state: st.session_state.total_study_time = 0
if "laps" not in st.session_state: st.session_state.laps = []
if "last_lap_elapsed" not in st.session_state: st.session_state.last_lap_elapsed = 0
# Break Engine State Properties
if "break_mode" not in st.session_state: st.session_state.break_mode = False
if "break_end_time" not in st.session_state: st.session_state.break_end_time = None

# --- APP INTERFACE ---
st.title("🥀 Study ritual.")
st.caption("I ain't never had a doubt inside me\nAnd if I ever told you that I did, I'm fuckin' lyin'")

# Session Total Accumulator Card
active_run_delta = (time.time() - st.session_state.start_time) if (st.session_state.running and not st.session_state.break_mode) else 0
st.markdown(
    f"<div class='metric-card'><span style='color: {active_theme['accent']}; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;'>Total Focused Time This Session</span><br><b style='font-size: 22px; color: {active_theme['text']};'>{format_time(st.session_state.total_study_time + active_run_delta)}</b></div>",
    unsafe_allow_html=True
)

# Responsive Controls Layout (5 equal columns)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("✨ Start"):
        if not st.session_state.running:
            st.session_state.break_mode = False
            st.session_state.start_time = time.time() - st.session_state.elapsed_time
            st.session_state.running = True

with col2:
    if st.button("⏳ Pause"):
        if st.session_state.running and not st.session_state.break_mode:
            current_run_duration = time.time() - st.session_state.start_time
            st.session_state.total_study_time += (current_run_duration - st.session_state.elapsed_time)
            st.session_state.elapsed_time = current_run_duration
            st.session_state.running = False
            st.rerun()

with col3:
    if st.button("☕ 5m Break"):
        st.session_state.running = True
        st.session_state.break_mode = True
        st.session_state.break_end_time = time.time() + 300 # 5 minutes countdown anchor
        st.rerun()

with col4:
    if st.button("🥀 Reset"):
        st.session_state.start_time = None
        st.session_state.running = False
        st.session_state.elapsed_time = 0
        st.session_state.total_study_time = 0
        st.session_state.laps = []
        st.session_state.last_lap_elapsed = 0
        st.session_state.break_mode = False
        st.session_state.break_end_time = None
        st.rerun()

# Dynamic Placeholders
timer_display = st.empty()
quote_display = st.empty()
break_display = st.empty()

# --- LIVE RUNNING EXECUTION LOOP (Handles both Focus Mode & Break Mode) ---
while st.session_state.running:
    if st.session_state.break_mode:
        # --- BREAK OVERVIEW TRACKING LOOP ---
        remaining_break = st.session_state.break_end_time - time.time()
        
        if remaining_break <= 0:
            st.session_state.running = False
            st.session_state.break_mode = False
            timer_display.markdown(
                f"<div class='break-banner'> BREAK OVER! TIME TO LOCK BACK IN.</div><h1 style='font-size: 70px; font-weight: 200; text-align: center; color: {active_theme['accent']};'>00:00:00</h1>", 
                unsafe_allow_html=True
            )
            st.balloons()
            break
        else:
            b_mins, b_secs = divmod(int(remaining_break), 60)
            timer_display.markdown(
                f"<div class='break-banner' style='background-color: {active_theme['card']}; color: {active_theme['text']};'>☕ Rest Mode Ticking...</div><h1 style='font-size: 70px; font-weight: 200; text-align: center; color: {active_theme['text']};'>{0:02d}:{b_mins:02d}:{b_secs:02d}</h1>", 
                unsafe_allow_html=True
            )
    else:
        # --- REGULAR STUDY SYSTEM RUN ---
        current_elapsed = time.time() - st.session_state.start_time
        hours, remainder = divmod(int(current_elapsed), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        timer_display.markdown(
            f"<h1 style='font-size: 70px; font-weight: 200; text-align: center; color: {active_theme['text']};'>{hours:02d}:{minutes:02d}:{seconds:02d}</h1>", 
            unsafe_allow_html=True
        )
        
        current_total_minutes = int(current_elapsed // 60)
        
        if current_total_minutes > 0 and current_total_minutes % quote_interval == 0:
            quote_idx = (current_total_minutes // quote_interval) % len(MOTIVATIONAL_QUOTES)
            quote_display.markdown(
                f"<div class='quote-box'><b>From a woman who built her empire:</b><br>{MOTIVATIONAL_QUOTES[quote_idx]}</div>", 
                unsafe_allow_html=True
            )
        else:
            quote_display.empty()
            
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

# Static Display fallback state container
if not st.session_state.running and not st.session_state.break_mode:
    hours, remainder = divmod(int(st.session_state.elapsed_time), 3600)
    minutes, seconds = divmod(remainder, 60)
    timer_display.markdown(
        f"<h1 style='font-size: 70px; font-weight: 200; text-align: center; color: {active_theme['accent']};'>{hours:02d}:{minutes:02d}:{seconds:02d}</h1>", 
        unsafe_allow_html=True
    )

# --- LAP DISPLAY BOARD AREA ---
if st.session_state.laps:
    st.markdown(f"<h3 style='font-size: 16px; font-weight: 400; color: {active_theme['text']}; letter-spacing: 1px; margin-top: 30px;'>📜 Focus Milestones (Laps)</h3>", unsafe_allow_html=True)
    for lap in st.session_state.laps:
        st.markdown(
            f"<div class='lap-row'><span>✨ Chapter/Subject Marker <b>#{lap['num']}</b></span><span>⏱️ Duration: <b>{lap['duration']}</b> <span style='color:{active_theme['accent']}aa; font-size:11px; margin-left:8px;'>(Timeline: {lap['total']})</span></span></div>",
            unsafe_allow_html=True
        )
