
# Dream11 Grand League Team Generator
import random
import pandas as pd

# Try importing Streamlit and micropip if required
try:
    import streamlit as st
except ModuleNotFoundError:
    print("[ERROR] Streamlit module not found. Please install it using 'pip install streamlit'.")
    exit()

st.set_page_config(page_title="Dream11 GL Team Generator", layout="centered")
st.title("🔥 Dream11 Grand League Team Generator")
st.markdown("Generate risky, winning combinations for today's match!")

# Define players by roles
batsmen = ["Paul Stirling", "Andy Balbirnie", "Harry Tector", "Brandon King", "Shai Hope"]
all_rounders = ["Roston Chase", "Curtis Campher", "Gareth Delany", "Andrew McBrine"]
bowlers = ["Alzarri Joseph", "Barry McCarthy", "Joshua Little", "Matthew Forde", "Craig Young"]
wicketkeepers = ["Lorcan Tucker"]

# Combine all players for fallback logic
players = batsmen + all_rounders + bowlers + wicketkeepers

# Captain & VC options
risky_captains = ["Roston Chase", "Matthew Forde", "Andrew McBrine", "Barry McCarthy"]
safe_captains = ["Shai Hope", "Paul Stirling"]

num_teams = st.slider("Select how many GL teams to generate:", 1, 20, 5)

# Role-based selection
st.markdown("### 🎯 Customize Your Team Composition")
num_batsmen = st.slider("Number of Batsmen", 1, 6, 3)
num_allrounders = st.slider("Number of All-rounders", 1, 4, 2)
num_bowlers = st.slider("Number of Bowlers", 1, 5, 4)
num_wicketkeepers = st.slider("Number of Wicketkeepers", 1, 2, 1)

role_total = num_batsmen + num_allrounders + num_bowlers + num_wicketkeepers

if role_total < 11:
    st.warning("⚠️ Total players selected per team must be at least 11. Please adjust the role sliders.")

elif st.button("Generate Teams"):
    all_teams = []

    for i in range(num_teams):
        try:
            team = random.sample(batsmen, num_batsmen) +                    random.sample(all_rounders, num_allrounders) +                    random.sample(bowlers, num_bowlers) +                    random.sample(wicketkeepers, num_wicketkeepers)

            if len(team) > 11:
                team = random.sample(team, 11)

        except ValueError:
            st.error("Not enough players in a role to generate team. Adjust sliders.")
            break

        captain = random.choice(risky_captains + safe_captains)
        vice_captain = random.choice([p for p in team if p != captain])

        all_teams.append({
            "Team No.": f"Team {i+1}",
            "Players": ", ".join(team),
            "Captain": captain,
            "Vice Captain": vice_captain
        })

    if all_teams:
        df = pd.DataFrame(all_teams)
        st.success("Here are your GL teams!")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Teams as CSV", data=csv, file_name="gl_teams.csv", mime="text/csv")

st.caption("Created by ChatGPT | Strategy: Use low-owned C/VC to beat the crowd!")
