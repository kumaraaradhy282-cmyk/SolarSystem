import streamlit as st
import matplotlib.pyplot as plt
import math

st.set_page_config(
    page_title="Solar System Explorer",
    page_icon="🪐",
    layout="wide"
)

st.title("🪐 Solar System Explorer (Streamlit Free MVP)")
st.caption("Interactive • Educational • Single-file app")

# -----------------------------
# Planet data (semi-real + demo)
# -----------------------------
PLANETS = {
    "Mercury": {
        "size": 0.4,
        "distance": 1,
        "fact": "Smallest planet",
        "image": "https://solarsystem.nasa.gov/system/feature_items/images/18_mercury_new.png",
    },
    "Venus": {
        "size": 0.9,
        "distance": 2,
        "fact": "Hottest planet",
        "image": "https://solarsystem.nasa.gov/system/feature_items/images/27_venus_jg.png",
    },
    "Earth": {
        "size": 1.0,
        "distance": 3,
        "fact": "Our home planet",
        "image": "https://solarsystem.nasa.gov/system/feature_items/images/17_earth.png",
    },
    "Mars": {
        "size": 0.5,
        "distance": 4,
        "fact": "The red planet",
        "image": "https://solarsystem.nasa.gov/system/feature_items/images/19_mars.png",
    },
    "Jupiter": {
        "size": 2.5,
        "distance": 6,
        "fact": "Largest planet",
        "image": "https://solarsystem.nasa.gov/system/feature_items/images/16_jupiter_new.png",
    },
    "Saturn": {
        "size": 2.2,
        "distance": 8,
        "fact": "Famous rings",
        "image": "https://solarsystem.nasa.gov/system/feature_items/images/28_saturn.png",
    },
}

# -----------------------------
# Controls
# -----------------------------
planet_selected = st.selectbox("🖱️ Select a Planet", PLANETS.keys())
time_slider = st.slider("🕒 Timeline (orbit position)", 0, 360, 0)

# -----------------------------
# Draw solar system
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_facecolor("black")

# Sun
ax.scatter(0, 0, s=900, color="yellow")
ax.text(0, -1.2, "Sun", color="white", ha="center")

for name, p in PLANETS.items():
    angle = math.radians(time_slider + p["distance"] * 20)
    x = p["distance"] * math.cos(angle)
    y = p["distance"] * math.sin(angle)

    ax.scatter(x, y, s=p["size"] * 400, color="skyblue")
    ax.text(x, y - 0.7, name, color="white", ha="center", fontsize=8)

ax.set_xlim(-10, 10)
ax.set_ylim(-6, 6)
ax.axis("off")

st.pyplot(fig)

# -----------------------------
# Planet details
# -----------------------------
st.divider()
col1, col2 = st.columns([1, 2])

with col1:
    st.image(PLANETS[planet_selected]["image"], width=200)

with col2:
    st.subheader(f"🪐 {planet_selected}")
    st.write(f"**Distance from Sun:** {PLANETS[planet_selected]['distance']} AU")
    st.write(f"**Relative Size:** {PLANETS[planet_selected]['size']}")
    st.write(f"**Fun Fact:** {PLANETS[planet_selected]['fact']}")

# -----------------------------
# Comparison Mode
# -----------------------------
st.divider()
st.subheader("🔍 Compare Two Planets")

p1, p2 = st.multiselect(
    "Choose planets to compare",
    PLANETS.keys(),
    default=["Earth", "Mars"]
)

if len(p1) == 2:
    c1, c2 = st.columns(2)
    for col, planet in zip([c1, c2], p1):
        with col:
            st.image(PLANETS[planet]["image"], width=150)
            st.write(f"**{planet}**")
            st.write(f"Distance: {PLANETS[planet]['distance']} AU")
            st.write(f"Size: {PLANETS[planet]['size']}")
            st.write(f"Fact: {PLANETS[planet]['fact']}")

st.caption("Not to scale • Educational MVP • Streamlit Free compatible")
