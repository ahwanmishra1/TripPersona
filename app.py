import streamlit as st
from agents.crew import create_crew
from agents.personality_engine import generate_personalities
from memory import update_memory

st.set_page_config(page_title="TRIPBUDDY ✈️", layout="wide")

# ---------------- SESSION ----------------
if "plans" not in st.session_state:
    st.session_state.plans = None

# ---------------- CSS ----------------
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
    line-height: 1.6;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>✈️ TRIPBUDDY</h1>
    <p>Plan smarter trips with AI personalities</p>
</div>
""", unsafe_allow_html=True)

# # ---------------- INPUT ----------------
# st.markdown('<div class="search-box">', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    source = st.text_input("From", "Bhubaneswar")

with c2:
    destination = st.text_input("To", "Goa")

with c3:
    days = st.number_input("Days", 1, 10, 3)

with c4:
    people = st.number_input("People", 1, 10, 2)

with c5:
    budget = st.number_input("Budget ₹", min_value=1000, value=10000)

if st.button("🔍 Plan Trip", use_container_width=True):

    with st.spinner("Planning your trip... ✨"):
        crew = create_crew(source, destination, days, budget, people)
        base_plan = crew.kickoff()

        plans = generate_personalities(
            base_plan, source, destination, people, budget
        )

        st.session_state.plans = plans

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RESULTS ----------------
plans = st.session_state.plans

if plans:

    st.markdown("## 🎭 Choose Your Style")

    tabs = st.tabs(["📊 Planner", "🤪 Chaotic", "😎 Local"])
    mapping = ["planner", "chaotic", "local"]

    for i, tab in enumerate(tabs):
        with tab:

            result_text = plans.get(mapping[i], "")

            if not result_text.strip():
                st.warning("⚠️ Empty plan. Try regenerating.")
            else:
                st.markdown(f"""
                <div class="result-card">
                    {result_text}
                </div>
                """, unsafe_allow_html=True)

# ---------------- FEEDBACK ----------------
st.markdown("---")

feedback = st.text_input("💬 Preferences (e.g. avoid clubs, prefer chill vibe)")

if st.button("Save Preference"):
    update_memory(feedback)
    st.success("Saved!")