import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Spotify Artist Analysis", layout="wide")

# Title
st.title("🎵 Spotify Artist Data Visualization")

# Load dataset
df = pd.read_csv("Spotify_Mix.csv")

# Sidebar for artist selection
artists = df['artists'].unique()
selected_artist = st.sidebar.selectbox("Select an Artist:", artists)

# Filter data for selected artist
art = df[df['artists'] == selected_artist]

# Display selected artist name
st.subheader(f"Analysis for **{selected_artist}**")

# Create plots
fig, axes = plt.subplots(2, 2, figsize=(15, 8))

# Plot 1: Danceability
sb.barplot(ax=axes[0, 0], x='name', y='danceability', data=art, palette="viridis")
axes[0, 0].set_title('Danceability by Song')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Key
sb.barplot(ax=axes[0, 1], x='name', y='key', data=art, palette="coolwarm")
axes[0, 1].set_title('Key by Song')
axes[0, 1].tick_params(axis='x', rotation=45)

# Plot 3: Instrumentalness
sb.barplot(ax=axes[1, 0], x='name', y='instrumentalness', data=art, palette="mako")
axes[1, 0].set_title('Instrumentalness by Song')
axes[1, 0].tick_params(axis='x', rotation=45)

# Plot 4: Add one more parameter (or duplicate as before)
sb.barplot(ax=axes[1, 1], x='name', y='energy', data=art, palette="rocket")
axes[1, 1].set_title('Energy by Song')
axes[1, 1].tick_params(axis='x', rotation=45)

# Adjust layout and show in Streamlit
plt.tight_layout()
st.pyplot(fig)

# Optional: Show data table
with st.expander("View Data for Selected Artist"):
    st.dataframe(art)
