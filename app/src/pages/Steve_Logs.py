import streamlit
import pandas
import requests

streamlit.set_page_config(page_title = "Admin - Logs Viewer")

streamlit.title("System Logs")

response = requests.get("http://localhost:4000/logs")
if response.status_code == 200:
    data = response.json()
    data_frame = pandas.DataFrame(data)
    streamlit.dataframe(data_frame)
else:
    streamlit.error("Failed to fetch logs from the server.")