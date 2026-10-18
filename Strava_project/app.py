import json
from pathlib import Path
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Strava Run Dashboard", layout="wide", page_icon="🏃")
st.title("Micka's Strava Dashboard")

file_path = Path(__file__).parent / "myactivities.json"
with open(file_path, "r", encoding="utf-8") as f:
    activities = json.load(f)

for activity in activities:
    if "Run" in activity["type"]:
        # Pace berechnen
        total_seconds = 1000 / activity['average_speed']
        pace_minutes = int(total_seconds // 60)
        pace_seconds = int(total_seconds % 60)

        # Strava-Datumsstring einlesen und umwandeln
        raw_date = activity['start_date']
        dt = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y um %H:%M Uhr")

        # Bewegungszeit in Stunden, Minuten und Sekunden aufteilen
        moving_seconds = activity['moving_time']
        hours = int(moving_seconds // 3600)
        minutes = int((moving_seconds % 3600) // 60)
        seconds = int(moving_seconds % 60)

        with st.container(border=True):
            col_title, col_date = st.columns([3, 2])
            with col_title:
                st.subheader(f"🏃 {activity['name']}")
            with col_date:
                st.caption(f"📅 {formatted_date}")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(label="Distance (km)", value=f"{activity['distance'] / 1000:.2f}")

            with col2:
                if hours > 0:
                    st.metric(label="Moving Time", value=f"{hours}:{minutes:02d}:{seconds:02d}")
                else:
                    st.metric(label="Moving Time", value=f"{minutes}:{seconds:02d}")

            with col3:
                st.metric(label="Average Pace (min/km)", value=f"{pace_minutes}:{pace_seconds:02d}")

            with col4:
                hr = activity.get('average_heartrate')
                hr_value = f"{hr:.0f} bpm" if hr else "–"
                st.metric(label="Puls (Ø)", value=hr_value)
