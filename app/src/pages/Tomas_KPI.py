import streamlit
import pandas
import requests
import altair

streamlit.set_page_config(page_title = "Analysis Revenue KPI")

streamlit.title("Revenue Dashboard (KPI)")

response = requests.get("http://localhost:4000/logs")
if response.status_code == 200:
    data = response.json()
    data_frame = panda.DataFrame(data)

    # convert
    data_frame['total_revenue'] = data_frame['total_revenue'].astype(float)
    data_frame['date'] = panda.to_datetime(data_frame['date'])

    chart = altair.Chart(data_frame).mark_bar().encode(
        x = altair.X('date:T', title = 'Date'),
        y = altair.Y('total_revenue:Q', title = 'Total Revenue in USD'),

        tooltip=['date', 'total_revenue']
    ).properties(width = 1000, height = 500, title = 'Total Revenue per Day')

    streamlit.altair_chart(chart, use_container_width = True)
else:
    streamlit.error("Failed to fetch data from API.")