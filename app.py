import streamlit as st

st.set_page_config(
    page_title="Solar System MVP",
    page_icon="🪐",
    layout="centered"
)

st.title("🪐 Solar System Explorer (MVP)")
st.caption("Streamlit Free • No external libraries")

# -----------------------------
# Planet data (static / demo)
# -----------------------------
PLANETS = {
    "Mercury": {
        "distance": "57.9 million km",
        "size": "Smallest planet",
        "fact": "Closest planet to the Sun",
        "emoji": "☿️",
    },
    "Venus": {
        "distance": "108.2 million km",
        "size": "Similar to Earth",
        "fact": "Hottest planet",
        "emoji": "♀️",
    },
    "Earth": {
        "distance": "149.6 million km",
        "size": "Medium",
        "fact": "Only known planet with life",
        "emoji": "🌍",
    },
    "Mars": {
        "distance": "227.9 million km",
        "size": "Smaller than Earth",
        "fact": "Known as the Red Planet",
        "emoji": "♂️",
    },
    "Jupiter": {
        "distance": "778.5 million km",
        "size": "Largest planet",
        "fact": "Has a giant red storm",
        "emoji": "🟠",
    },
    "Saturn": {
        "distance": "1.43 billion km",
        "size": "Very large",
        "fact": "Famous for its rings",
        "emoji": "🪐",
    },
    "Uranus": {
        "distance": "2.87 billion km",
        "size": "Ice giant",
        "fact": "Rotates on its side",
        "emoji": "🔵",
    },
    "Neptune": {
        "distance": "4.50 billion km",
        "size": "Ice giant",
        "fact": "Strongest winds",
        "emoji": "🔷",
    },
}

# -----------------------------
# Planet selector (acts like click)
# -----------------------------
planet = st.selectbox("🖱️ Select a Planet", PLANETS.keys())

# -----------------------------
# Simple solar system view (text-based)
# -----------------------------
st.divider()
st.subheader("☀️ Solar System")

solar_line = "☀️  "
for p in PLANETS:
    solar_line += PLANETS[p]["emoji"] + "  "

st.write(solar_line)

# -----------------------------
# Planet details
# -----------------------------
st.divider()
details = PLANETS[planet]

st.subheader(f"🪐 {planet}")
st.write(f"**Distance from Sun:** {details['distance']}")
st.write(f"**Size:** {details['size']}")
st.write(f"**Fun Fact:** {details['fact']}")

st.caption("Educational MVP • No graphics libraries • Streamlit Free compatible")
