import streamlit as st
from weather_api import get_weather

def show_dashboard():
    st.title("🌤️ Weather Dashboard")

    city = st.text_input("Enter city name", "London")

    if st.button("Get Weather"):
        data = get_weather(city)
        if not data:
            st.error("City not found or API error.")
        else:
            st.success(f"Weather for {city}:")
            st.metric("Temperature (°C)", data["main"]["temp"])
            st.metric("Humidity (%)", data["main"]["humidity"])
            st.metric("Pressure (hPa)", data["main"]["pressure"])
            st.write("Description:", data["weather"][0]["description"].capitalize())
            st.write("Wind speed (m/s):", data["wind"]["speed"])