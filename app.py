import streamlit as st

from agents.planner import generate_plan
from agents.transport import suggest_transport
from agents.hotel import suggest_hotel
from agents.budget import breakdown_budget
from agents.personality_engine import apply_personality

from memory import update_memory

# ---------------- CONFIG ----------------
st.set_page_config(page_title="TRIPBUDDY ✈️", layout="wide")

# ---------------- SESSION ----------------
if "plans" not in st.session_state:
    st.session_state.plans = None

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #ff385c, #ff7a18);
    padding: 50px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}
.search-box {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
    margin-top: -30px;
}
.result-card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    line-height: 1.7;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>✈️ TRIPBUDDY</h1>
    <p>AI Travel Planner with Personality</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
st.markdown('<div class="search-box">', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    source = st.text_input("From", "Kolkata")

with c2:
    destination = st.text_input("To", "Goa")

with c3:
    days = st.number_input("Days", 1, 15, 3)

with c4:
    people = st.number_input("People", 1, 10, 2)

with c5:
    budget = st.number_input("Budget ₹", min_value=1000, value=10000)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SPLIT FUNCTION ----------------
def split_personalities(text):
    parts = {
        "chaotic": "",
        "planner": "",
        "local": ""
    }

    current = None

    for line in text.split("\n"):
        l = line.lower()

        if "chaotic" in l:
            current = "chaotic"
        elif "planner" in l:
            current = "planner"
        elif "local" in l:
            current = "local"
        elif current:
            parts[current] += line + "\n"

    return parts

# ---------------- MAIN ACTION ----------------
if st.button("🔍 Plan Trip", use_container_width=True):

    with st.spinner("Building your trip... ✨"):

        # 1️⃣ Agents
        plan = generate_plan(source, destination, days, people, budget)
        transport = suggest_transport(source, destination, budget)
        hotel = suggest_hotel(destination, budget)
        budget_plan = breakdown_budget(destination, days, people, budget)

        # 2️⃣ Combine
        combined = f"""
TRANSPORT:
{transport}

HOTEL:
{hotel}

BUDGET:
{budget_plan}

ITINERARY:
{plan}
"""

        # 3️⃣ Personality layer
        final_output = apply_personality(combined)

        # 4️⃣ Split
        plans = split_personalities(final_output)

        st.session_state.plans = plans

# ---------------- RESULTS ----------------
plans = st.session_state.plans

if plans:
    st.markdown("## 🎭 Choose Your Travel Style")

    tabs = st.tabs(["📊 Planner", "🤪 Chaotic", "😎 Local"])

    keys = ["planner", "chaotic", "local"]

    for i, tab in enumerate(tabs):
        with tab:
            content = plans.get(keys[i], "")

            st.markdown(f"""
            <div class="result-card">
            {content if content else "No plan generated"}
            </div>
            """, unsafe_allow_html=True)

# ---------------- MEMORY ----------------
st.markdown("---")

feedback = st.text_input("💬 Preferences (e.g. avoid clubs, prefer beaches)")

if st.button("Save Preference"):
    if feedback.strip():
        update_memory(feedback)
        st.success("Preference saved!")
    else:
        st.warning("Please enter something.")