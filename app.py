import streamlit as st
from agents.crew import create_crew

st.set_page_config(page_title="TRIPBUDDY ✈️", layout="centered")

st.title("✈️ TRIPBUDDY")
st.subheader("Your AI Travel Planner (Offline)")

# Inputs
destination = st.text_input("📍 Destination", placeholder="e.g. Goa")
days = st.number_input("📅 Number of Days", min_value=1, max_value=30, value=3)
budget = st.text_input("💰 Budget", placeholder="e.g. 10000")

# Button
if st.button("🚀 Generate Trip Plan"):

    if not destination or not budget:
        st.warning("Please fill all fields")
    else:
        with st.spinner("Planning your trip... ✨"):

            crew = create_crew(destination, days, budget)
            result = crew.kickoff()

            result_text = str(result)

            st.success("Trip Plan Ready! 🎉")

            days = result_text.split("Day ")

            for day in days[1:]:
                day_title = day.split("\n")[0]
                content = "\n".join(day.split("\n")[1:])
                
                with st.expander(f"📅 Day {day_title}"):
                    st.markdown(content)

            # Optional sections
            if "Hotel" in result_text:
                st.markdown("## 🏨 Hotel Recommendation")
                st.write(result_text.split("Hotel")[1])

            if "Tips" in result_text:
                st.markdown("## 💡 Travel Tips")
                st.write(result_text.split("Tips")[1])