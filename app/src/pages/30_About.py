import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About Suds N' Duds ")

st.markdown (
    """
    Suds N' Duds is a smart, data-driven laundry delivery service—like UberEats, but for your laundry. Our easy-to-use app connects customers with local drivers who take care of the entire process. From picking up your laundry at your doorstep to getting it cleaned at a trusted local laundromat and delivering it back fresh and folded, Suds N' Duds handles the dirty work so you don’t have to. 

    Stay tuned for more information and features to come!
    """
        )
