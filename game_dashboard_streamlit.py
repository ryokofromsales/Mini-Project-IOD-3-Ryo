import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv(r'C:\Users\ryoko\OneDrive\Documents\Data Sciecne Course Files\Module 9\Module 9 Answers\game_dashboard_data.csv')

st.title("Gaming Cross-Platform Dashboard")

st.markdown(
    """
    This dashboard combines live player counts (Steam), Twitch stream activity, and Reddit community buzz for trending games.
    """
)

# Sidebar for filtering
game_list = df["Game"].sort_values().tolist()
selected_games = st.sidebar.multiselect("Select games to view:", game_list, default=game_list)

filtered_df = df[df["Game"].isin(selected_games)]

st.subheader("Main Metrics Table")
st.dataframe(
    filtered_df[
        [
            "Game",
            "Steam Players",
            "Twitch Streams",
            "Reddit Mentions",
            "Reddit Comment Score",
        ]
    ].sort_values("Steam Players", ascending=False),
    use_container_width=True,
)

st.subheader("Steam Players vs. Twitch Streams")
st.bar_chart(filtered_df.set_index('Game')[["Steam Players", "Twitch Streams"]])

st.subheader("Reddit Mentions and Top Comment Score")
st.bar_chart(filtered_df.set_index('Game')[["Reddit Mentions", "Reddit Comment Score"]])

st.subheader("Top Reddit Comments")
for _, row in filtered_df.iterrows():
    st.markdown(f"**{row['Game']}**")
    st.info(f"_{row['Top Reddit Comment']}_\n\n*Score: {row['Reddit Comment Score']}*")
    st.caption(f"Submission: {row['In Submission']}")

st.markdown("---")
st.markdown("Built with Streamlit. Data: Steam, Twitch, Reddit.")