import streamlit as st
from agents.crew import create_crew
from agents.personality_engine import generate_personalities
from memory import update_memory

st.set_page_config(page_title="TRIPBUDDY ✈️", layout="centered")

st.title("✈️ TRIPBUDDY")
st.subheader("AI Travel Planner with Personalities")

source = st.text_input("🛫 Source", placeholder="e.g. Kolkata")
destination = st.text_input("📍 Destination", placeholder="e.g. Goa")

days = st.number_input("📅 Days", 1, 30, 3)
people = st.number_input("👨‍👩‍👧‍👦 People", 1, 10, 2)
budget = st.number_input("💰 Budget (INR ₹)", min_value=1000, value=10000)

if st.button("🚀 Generate Trip Plan"):

    if not source or not destination:
        st.warning("Fill all fields")
    else:
        with st.spinner("Planning your trip... ✨"):

            crew = create_crew(source, destination, days, budget, people)
            base_plan = crew.kickoff()

            personality_plans = generate_personalities(
                base_plan, source, destination, people, budget
            )

        st.success("Trip Plans Ready! 🎉")

        for key, value in personality_plans.items():
            with st.expander(f"{key.upper()} VERSION"):
                st.markdown(value)

        # choice = st.radio("Choose your plan", ["chaotic", "planner", "local"])

        # if st.button("✅ Confirm Plan"):
        #     st.markdown("## 🎉 Final Itinerary")
        #     st.markdown(personality_plans[choice])

# Feedback
st.markdown("---")
feedback = st.text_input("💬 Feedback (e.g., skip clubs, prefer beaches)")

if st.button("Submit Feedback"):
    update_memory(feedback)
    st.success("Memory updated 🧠")