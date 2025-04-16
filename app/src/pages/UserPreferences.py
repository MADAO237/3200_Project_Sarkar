import streamlit as st

st.title("User Preferences")

# Filters
st.subheader("Filter Via")
filter_option = st.radio("Choose a filter", ("Location", "Pricing", "Delivery"))


# Recent filters with placeholder info
st.subheader("Recent filters")
filters = ["filter 1", "filter 2", "filter 3"]
for search in filters:
    col1, col2 = st.columns([3,1])
    col1.write(search)
    col2.button("Select", key=search)
    
    st.button("Save Filter as Preference?")