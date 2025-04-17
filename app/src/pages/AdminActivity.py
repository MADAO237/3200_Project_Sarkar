import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta 

# There were issues connecting with the backend databases, so I ended up hardcoding sample data just to show what it should look like.

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Activity Overview 📈')

# Generate sample data for the charts and metrics
def generate_sample_data():
    # Generate dates for past week
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate user traffic data with some random variation
    base_traffic = 100
    traffic_data = [base_traffic + np.random.randint(-20, 100) for _ in range(len(dates))]
    
    # Create traffic dataframe
    traffic_df = pd.DataFrame({
        'Date': dates,
        'Users': traffic_data
    })
    
    # Format dates as day names (Mon, Tue, etc.)
    traffic_df['Day'] = traffic_df['Date'].dt.strftime('%a')
    
    return traffic_df

# Generate sample log entries
def generate_logs(count=10):
    log_types = [
        "New user added",
        "Long response time detected",
        "Database query timeout",
        "API request failed",
        "Authentication error",
        "User login successful",
        "File upload completed",
        "System backup completed",
        "Memory usage high",
        "CPU usage spike"
    ]
    
    logs = []
    now = datetime.now()
    
    for i in range(count):
        time_offset = timedelta(hours=-(i*2), minutes=-(i*17))
        log_time = now + time_offset
        log_entry = {
            'timestamp': log_time.strftime('%m/%d %H:%M'),
            'message': np.random.choice(log_types)
        }
        logs.append(log_entry)
    
    return logs

# Create layout
col1, col2 = st.columns([3, 2])

# Left column - System overview and charts
with col1:
    # System overview container
    with st.container(border=True):
        st.subheader('System Overview and Event Logs')
        
        # Generate traffic data
        traffic_data = generate_sample_data()
        
        # System metrics in 3 columns
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        
        with metrics_col1:
            st.metric("Active User Count", "500")
        
        with metrics_col2:
            st.metric("Response Time", "10 ms")
        
        with metrics_col3:
            st.metric("Uptime", "90%")
        
        # User traffic chart
        st.subheader('User Traffic Over Time')
        chart_data = pd.DataFrame({
            'index': traffic_data['Day'],
            'Users': traffic_data['Users']
        }).set_index('index')
        
        st.line_chart(chart_data)

# Right column - Event logs and actions
with col2:
    # Event log container
    with st.container(border=True):
        st.subheader('Event Log')
        
        logs = generate_logs(5)
        
        for log in logs:
            st.text(f"[{log['timestamp']}] {log['message']}")
    
    # Action button for messaging
    st.button('Send Message to New Users', type='primary', use_container_width=True)
    
    # Additional sample system health indicators
    with st.expander("System Health Details"):
        st.write("CPU Usage: 35%")
        st.write("Memory Usage: 2.1 GB / 8 GB")
        st.write("Disk Space: 120 GB available")
        st.write("Last Backup: Today at 03:00 AM")
        st.progress(35, "CPU Load")
        st.progress(65, "Memory Usage")