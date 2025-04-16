import streamlit as st

st.title("Select a Laundromat")

# Service Options
st.subheader("Select Option(s)")
services = st.multiselect("Choose services:", ["Washing + Drying", "Pressing", "Ironing"])

# Laundromat Info with placeholder labels/data
laundromats = {
    "Lawrence Laundry": ("2 hrs 30 mins", "$25.14 + $5.00 delivery"),
    "Wrinkle Relief": ("1 hr 15 mins", "$34.67 + $6.25 delivery"),
    "Suds and Duds": ("40 mins", "$29.99 + $10 delivery")
}

st.subheader("Laundromat Options")
for name, (time, price) in laundromats.items():
    col1, col2, col3 = st.columns(3)
    col1.write(f"**{name}**")
    col2.write(time)
    col3.write(price)
