import streamlit as st
import time

# --- STATE CONFIGURATION ---
if "start_time" not in st.session_state: st.session_state.start_time = None
if "running" not in st.session_state: st.session_state.running = False
if "elapsed_time" not in st.session_state: st.session_state.elapsed_time = 0
if "total_study_time" not in st.session_state: st.session_state.total_study_time = 0
if "break_mode" not in st.session_state: st.session_state.break_mode = False
if "break_end_time" not in st.session_state: st.session_state.break_end_time = None
if "current_target" not in st.session_state: st.session_state.current_target = ""

def format_time(seconds_count):
    hours, remainder = divmod(int(seconds_count), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Update text state immediately when the user changes it
def update_target():
    st.session_state.current_target = st.session_state.target_input_field

# Dynamic Tab Streaming Header
tab_title = "Study ritual"
if st.session_state.running:
    if st.session_state.break_mode and st.session_state.break_end_time:
        rem = max(0, int(st.session_state.break_end_time - time.time()))
        tab_title = f"({format_time(rem)}) Break Time"
    else:
        active_delta = (time.time() - st.session_state.start_time) if st.session_state.start_time else 0
        tab_title = f"({format_time(active_delta)}) Focus State"

st.set_page_config(page_title=tab_title, page_icon="🥀", layout="centered")

# --- CUSTOM PALETTE REGISTRY ---
THEMES = {
    "🌌 Periwinkle Dream": {
        "bg": "#A2A6F2", "card": "#7D82E6", "text": "#E8ECFA", "accent": "#F28627", "muted": "#B5B8F5"
    },
    "🎨 Fruit Punch Orchard": {
        "bg": "#C1809A", "card": "#DF0F57", "text": "#EABF28", "accent": "#EF8000", "muted": "#AACCCC"
    },
    "🌿 Botanical Solace": {"bg": "#043323", "card": "#105666", "text": "#F7F4D5", "accent": "#839050", "muted": "#039680"},
    "🏺 Gilded Bistre": {"bg": "#210100", "card": "#814436", "text": "#FECE79", "accent": "#E64341", "muted": "#8C0902"},
    "🔮 Cyber Orchid": {"bg": "#3D1472", "card": "#3333AF", "text": "#FA8EE4", "accent": "#9896FF", "muted": "#B744B5"},
    "🌊 Tropical Sea Foam": {"bg": "#076DDF", "card": "#19887F", "text": "#DAF6F6", "accent": "#92F1EC", "muted": "#35AEAC"},
    "🦩 Poolside Barbie": {"bg": "#227E9D", "card": "#51ACC5", "text": "#FDF9FA", "accent": "#FDA9CC", "muted": "#FD50A4"},
    "☀️ Sun-Drenched Apricot": {"bg": "#FA9058", "card": "#FECC64", "text": "#FFF6E8", "accent": "#FCEABC", "muted": "#B5D8FF"},
    "🍁 Autumnal Alchemy": {"bg": "#13260F", "card": "#344F30", "text": "#FDD973", "accent": "#F47230", "muted": "#9F350B"},
    "⛈️ Navagio Coastline": {"bg": "#3F9CB0", "card": "#58DEE1", "text": "#FFD6C7", "accent": "#EB8629", "muted": "#DC4A44"},
    "⚡ Neon Pulse": {"bg": "#231F20", "card": "#0AA9E0", "text": "#7BF004", "accent": "#FC05B8", "muted": "#FA6B05"},
    "🌸 Pastel Dreamcicle": {"bg": "#594EAD", "card": "#5A9AD6", "text": "#F99E85", "accent": "#F4607B", "muted": "#78C681"},
    "🪵 Desert Saddle": {"bg": "#957443", "card": "#1FB189", "text": "#CCCCAC", "accent": "#EC321F", "muted": "#E7ABC7"},
    "🍓 Azure Mist & Berry": {"bg": "#64A4ED", "card": "#A72536", "text": "#E5FAFF", "accent": "#FA4F8E", "muted": "#FFF2A3"},
    "🧥 White Silk & Navy": {"bg": "#26386A", "card": "#75B06F", "text": "#FAE251", "accent": "#FFFFFF", "muted": "#1F2B52"},
    "🌅 Denim Sunshine": {"bg": "#3F1E17", "card": "#2E4C6D", "text": "#FFD058", "accent": "#FE422C", "muted": "#FA9743"}
}

with st.sidebar:
    st.markdown("### 🎨 Space Design")
    selected_theme_name = st.selectbox("Active Aesthetic Environment", list(THEMES.keys()))
    st.markdown("---")
    st.markdown("### ⏳ Notification Delays")
    quote_interval = st.number_input("Motivation Quotes (Mins)", value=15, min_value=1)
    break_interval = st.number_input("Break Tasks (Mins)", value=20, min_value=1)

active_theme = THEMES[selected_theme_name]

# --- DESIGN INJECTIONS ---
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
    .main-title {{
        text-align: center;
        font-weight: 300;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
        color: {active_theme['text']};
    }}
    .sub-lyrics {{
        text-align: center;
        font-style: italic;
        font-weight: 600;
        color: {active_theme['accent']} !important;
        margin-bottom: 30px;
        font-size: 14px;
        letter-spacing: 0.5px;
    }}
    .timer-plate {{
        background-color: #0c0707e6 !important;
        border: 2px solid {active_theme['accent']};
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        box-shadow: 0px 20px 40px rgba(0,0,0,0.5);
        margin: 25px auto;
        max-width: 580px;
    }}
    .timer-text {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 78px !important;
        font-weight: bold !important;
        color: #FFFFFF !important;
        text-shadow: 0px 0px 15px {active_theme['accent']}cc;
        letter-spacing: 2px;
        margin: 0;
    }}
    .stButton>button {{
        background-color: {active_theme['card']} !important;
        color: {active_theme['text']} !important;
        border: 1px solid {active_theme['accent']}66 !important;
        border-radius: 24px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        font-size: 13px;
        letter-spacing: 0.5px;
        transition: all 0.2s ease;
        width: 100%;
    }}
    .stButton>button:hover {{
        background-color: {active_theme['accent']} !important;
        color: {active_theme['bg']} !important;
        border-color: {active_theme['accent']} !important;
        box-shadow: 0px 0px 12px {active_theme['accent']}88;
    }}
    .quote-box {{
        background-color: {active_theme['card']}bf;
        border-left: 4px solid {active_theme['accent']};
        padding: 18px;
        border-radius: 12px;
        margin: 25px auto;
        max-width: 580px;
        font-style: italic;
        color: {active_theme['text']};
    }}
    .break-box {{
        background-color: {active_theme['card']}bf;
        border: 1px dashed {active_theme['muted']};
        padding: 18px;
        border-radius: 12px;
        margin: 25px auto;
        max-width: 580px;
        color: {active_theme['text']};
    }}
    .metric-card {{
        background-color: {active_theme['card']}55;
        border: 1px solid {active_theme['accent']}22;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        margin: 0 auto 25px auto;
        max-width: 580px;
    }}
    .break-banner {{
        background-color: {active_theme['accent']};
        color: {active_theme['bg']};
        font-weight: bold;
        text-align: center;
        padding: 8px;
        border-radius: 6px;
        margin-bottom: 20px;
        letter-spacing: 1px;
        font-size: 12px;
    }}
    div[data-testid="stTextArea"] textarea {{
        background-color: #0c0707c2 !important;
        color: #FFFFFF !important;
        border: 1px solid {active_theme['accent']}66 !important;
        font-size: 15px !important;
    }}
    div[data-testid="stTextArea"] textarea:focus {{
        border-color: {active_theme['accent']} !important;
        box-shadow: 0 0 10px {active_theme['accent']}44 !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ENGINE DATA ARCHIVES ---
MOTIVATIONAL_QUOTES = [
    "“The most effective way to do it, is to do it.” — Amelia Earhart",
    "“I never dreamed about success. I worked for it.” — Estée Lauder",
    "“Define success on your own terms, achieve it by your own rules.” — Anne Sweeney",
    "“You can waste your lives drawing lines. Or you can live your life crossing them.” — Shonda Rhimes",
    "“Think like a queen. A queen is not afraid to fail.” — Oprah Winfrey",
    "“Done is better than perfect.” — Sheryl Sandberg",
    "“If they don't give you a seat at the table, bring a folding chair.” — Shirley Chisholm"
]

BREAK_ACTIVITIES = [
    "🧼 wash your face & refresh",
    "📂 Organize ONE tiny thing on your desk",
    "🎨 Doodle your thoughts on scrap paper",
    "✨ Work on making your study notes aesthetic",
    "🧊 get some ice water",
    "☕ Step away and fix yourself a warm cup of matcha or herbal tea."
]

# --- APP INTERFACE ---
st.markdown("<h1 class='main-title'>🥀 Study ritual.</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-lyrics'>I ain't never had a doubt inside me • And if I ever told you that I did, I'm fuckin' lyin'</p>", unsafe_allow_html=True)

active_run_delta = (time.time() - st.session_state.start_time) if (st.session_state.running and not st.session_state.break_mode) else 0
st.markdown(
    f"<div class='metric-card'><span style='color: {active_theme['accent']}; font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px;'>Cumulative Focus Block</span><br><b style='font-size: 24px; color: {active_theme['text']};'>{format_time(st.session_state.total_study_time + active_run_delta)}</b></div>",
    unsafe_allow_html=True
)

timer_display = st.empty()
quote_display = st.empty()
break_display = st.empty()

# --- EQUALIZED CONTROLS LAYOUT (4 Columns now without Lap) ---
ctrl_col1, ctrl_col2, ctrl_col3, ctrl_col4 = st.columns(4)

with ctrl_col1:
    if st.button("✨ Start"):
        if not st.session_state.running:
            st.session_state.break_mode = False
            st.session_state.start_time = time.time() - st.session_state.elapsed_time
            st.session_state.running = True
            st.rerun()

with ctrl_col2:
    if st.button("⏳ Pause"):
        if st.session_state.running and not st.session_state.break_mode:
            current_run_duration = time.time() - st.session_state.start_time
            st.session_state.total_study_time += (current_run_duration - st.session_state.elapsed_time)
            st.session_state.elapsed_time = current_run_duration
            st.session_state.running = False
            st.rerun()

with ctrl_col3:
    if st.button("☕ 5m Break"):
        st.session_state.running = True
        st.session_state.break_mode = True
        st.session_state.break_end_time = time.time() + 300
        st.rerun()

with ctrl_col4:
    if st.button("🥀 Reset"):
        st.session_state.start_time = None
        st.session_state.running = False
        st.session_state.elapsed_time = 0
        st.session_state.total_study_time = 0
        st.session_state.break_mode = False
        st.session_state.break_end_time = None
        st.rerun()

# --- INTENT BINDING WORKSPACE ---
st.markdown("<div style='max-width:580px; margin:25px auto 0 auto;'>", unsafe_allow_html=True)
st.text_area(
    label="🎯 Focus Target Objectives:", 
    value=st.session_state.current_target,
    placeholder="Type focus goal here and hit Ctrl+Enter to save...", 
    height=68, 
    label_visibility="collapsed",
    key="target_input_field",
    on_change=update_target
)
st.markdown("</div>", unsafe_allow_html=True)

# --- AUTOMATED LOOP CLOCK ---
if st.session_state.running:
    if st.session_state.break_mode:
        remaining_break = st.session_state.break_end_time - time.time()
        if remaining_break <= 0:
            st.session_state.running = False
            st.session_state.break_mode = False
            st.balloons()
            st.rerun()
        else:
            b_mins, b_secs = divmod(int(remaining_break), 60)
            timer_display.markdown(
                f"<div class='timer-plate'><div class='break-banner'>☕ BREAK CYCLE ACTIVE</div><p class='timer-text'>00:{b_mins:02d}:{b_secs:02d}</p></div>", 
                unsafe_allow_html=True
            )
    else:
        current_elapsed = time.time() - st.session_state.start_time
        timer_display.markdown(
            f"<div class='timer-plate'><p class='timer-text'>{format_time(current_elapsed)}</p></div>", 
            unsafe_allow_html=True
        )
        
        current_total_minutes = int(current_elapsed // 60)
        if current_total_minutes > 0 and current_total_minutes % quote_interval == 0:
            quote_idx = (current_total_minutes // quote_interval) % len(MOTIVATIONAL_QUOTES)
            quote_display.markdown(f"<div class='quote-box'><b>Empire Mindset:</b><br>{MOTIVATIONAL_QUOTES[quote_idx]}</div>", unsafe_allow_html=True)
        if current_total_minutes > 0 and current_total_minutes % break_interval == 0:
            break_idx = (current_total_minutes // break_interval) % len(BREAK_ACTIVITIES)
            break_display.markdown(f"<div class='break-box'><b>☕ Rest Strategy:</b><br>{BREAK_ACTIVITIES[break_idx]}</div>", unsafe_allow_html=True)

    time.sleep(1)
    st.rerun()

else:
    display_timestamp = format_time(st.session_state.elapsed_time)
    timer_display.markdown(
        f"<div class='timer-plate'><p class='timer-text' style='color: {active_theme['accent']} !important;'>{display_timestamp}</p></div>", 
        unsafe_allow_html=True
    )
