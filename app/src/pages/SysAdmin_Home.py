import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd

# this is also not connected to the actual databse due to errors, it does visually show how it would and should look however

st.set_page_config(layout='wide')

SideBarLinks()

st.title('User Management Dashboard')

# Initialize session state for users that don't exist
if 'users' not in st.session_state:
    # Sample initial data
    st.session_state.users = pd.DataFrame({
        'Name': ['Alice Smith', 'Bob Houston'],
        'Email': ['SmithA@email.com', 'HoustonB@email.com'],
        'Role': ['User', 'Admin']
    })

# Create a layout with two columns
col1, col2 = st.columns([3, 1])

with col2:
    # Search section
    with st.container(border=True):
        st.subheader('Search')
        search_name = st.text_input('Search by name')
        search_email = st.text_input('Search by e-mail')
        
        if st.button('Search', use_container_width=True):
            if search_name or search_email:
                filtered_users = st.session_state.users[
                    (st.session_state.users['Name'].str.contains(search_name, case=False) if search_name else True) &
                    (st.session_state.users['Email'].str.contains(search_email, case=False) if search_email else True)
                ]
                st.session_state.filtered = filtered_users
            else:
                st.session_state.filtered = st.session_state.users
    
    # Add New User section
    with st.container(border=True):
        st.subheader('Add New User')
        new_name = st.text_input('Enter name')
        new_email = st.text_input('Enter email')
        new_role = st.selectbox('Enter role', ['User', 'Admin', 'Viewer'])
        
        if st.button('Add User', type='primary', use_container_width=True):
            if new_name and new_email:
                new_user = pd.DataFrame({
                    'Name': [new_name],
                    'Email': [new_email],
                    'Role': [new_role]
                })
                st.session_state.users = pd.concat([st.session_state.users, new_user], ignore_index=True)
                st.success(f"User {new_name} added successfully!")
                # Reset input fields
                st.rerun()
            else:
                st.error("Name and Email are required fields.")

with col1:
    # Show users in a table
    st.subheader('Users')
    
    # Display filtered results if search was performed, otherwise show all users
    display_df = st.session_state.get('filtered', st.session_state.users)
    
    # Reset filtered view button
    if 'filtered' in st.session_state and st.button('Show All Users'):
        del st.session_state.filtered
        st.rerun()
    
    # Display the table with delete buttons
    for i, row in display_df.iterrows():
        cols = st.columns([3, 3, 1])
        with cols[0]:
            st.write(row['Name'])
        with cols[1]:
            st.write(row['Email'])
        with cols[2]:
            if st.button('DELETE', key=f"delete_{i}"):
                user_index = st.session_state.users[
                    (st.session_state.users['Name'] == row['Name']) & 
                    (st.session_state.users['Email'] == row['Email'])
                ].index
                st.session_state.users = st.session_state.users.drop(user_index).reset_index(drop=True)
                if 'filtered' in st.session_state:
                    del st.session_state.filtered
                st.success(f"User {row['Name']} deleted successfully!")
                st.rerun()
        st.divider()