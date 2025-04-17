import streamlit as st
import requests

st.title("Select a Laundromat")

# 🧺 Service Options (at the top)
st.subheader("Select Option(s)")
services = st.multiselect(
    "Choose services:",
    ["Washing + Drying", "Pressing", "Ironing"]
)

# 📡 Fetch laundromats from backend
try:
    response = requests.get("http://localhost:4000/l/laundromat?...")
    laundromats = response.json()
except Exception as e:
    st.error(f"Could not connect to backend. {e}")
    laundromats = []

# ✅ Show laundromats if fetched
if laundromats:
    st.subheader("Laundromat Options")
    for laundromat in laundromats:
        name = laundromat["location"]
        time = laundromat.get("time_process", "N/A")
        price = f"${laundromat['pricing']} + ${laundromat['delivery_fee']} delivery"

        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            st.write(f"**{name}**")
        with col2:
            st.write(time)
        with col3:
            st.write(price)

        st.button(f"Select {name}", key=f"select_{laundromat['laundromat_id']}")
else:
    st.info("No laundromats found.")
