import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("d:/DBS-coding-camp/dashboard/all_data.csv")
data['datetime'] = pd.to_datetime(data['datetime'])

# Warna kategori kualitas udara
color_map = {
    "Good": "#00FF00",
    "Moderate": "#ADFF2F",
    "Unhealthy for Sensitive Groups": "#FFD700",
    "Unhealthy": "#FF8C00",
    "Very Unhealthy": "#FF4500",
    "Hazardous": "#8B0000"
}

# Urutan kategori kualitas udara
category_order = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]

# Sidebar Filters
st.sidebar.header('Filters')
st.title('Air Quality Dashboard')

# Select station
selected_stations = st.sidebar.multiselect('Select Stations', data['station'].unique(), default=[])

# Select date range
start_date = st.sidebar.date_input('Start Date', min(data['datetime']).date())
end_date = st.sidebar.date_input('End Date', max(data['datetime']).date())

# Apply filters only if selections are made
if selected_stations:
    filtered_data = data[(data['station'].isin(selected_stations)) & (data['datetime'].dt.date >= start_date) & (data['datetime'].dt.date <= end_date)]
    st.subheader(f"Hasil Analisis untuk {', '.join(selected_stations)} ({start_date} - {end_date})")

    # 1️⃣ Curah Hujan Per Waktu
    st.subheader("Curah Hujan Per Waktu")
    avg_rain = filtered_data['RAIN'].mean()
    avg_temp = filtered_data['TEMP'].mean()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Curah Hujan Rata-rata", value=f"{avg_rain:.2f} mm")
    with col2:
        st.metric(label="Suhu Rata-rata", value=f"{avg_temp:.2f} °C")

    fig_rain_time = px.line(filtered_data, x='datetime', y='RAIN', color='station', markers=True,
                            title='Curah Hujan dari Rentang Waktu yang Dipilih')
    st.plotly_chart(fig_rain_time)

    # 2️⃣ Kualitas Udara pada Rentang Waktu
    st.subheader("Kualitas Udara pada Rentang Waktu")
    category_counts = filtered_data['Category'].value_counts().reindex(category_order, fill_value=0).reset_index()
    category_counts.columns = ['Category', 'Count']
    fig_quality_time = px.pie(category_counts, values='Count', names='Category',
                              title='Distribusi Kualitas Udara dalam Rentang Waktu yang Dipilih',
                              color='Category', color_discrete_map=color_map)
    st.plotly_chart(fig_quality_time)

    # 3️⃣ Konsentrasi Polutan pada Rentang Waktu
    st.subheader("Konsentrasi Polutan pada Rentang Waktu")
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    pollutant_avg = filtered_data.groupby('station')[pollutants].mean().reset_index()
    fig_pollutants_time = px.bar(pollutant_avg.melt(id_vars=['station']), x='station', y='value', color='variable',
                                 title='Rata-rata Konsentrasi Polutan dalam Rentang Waktu yang Dipilih',
                                 barmode='group')
    st.plotly_chart(fig_pollutants_time)

else:

    # 1️⃣ Daerah dengan Curah Hujan Tertinggi
    st.subheader("Daerah dengan Curah Hujan Tertinggi")
    rainfall_stats = data.groupby('station')['RAIN'].max().reset_index()
    fig_rain = px.bar(rainfall_stats, x='station', y='RAIN', title='Curah Hujan Maksimum per Stasiun', color='RAIN')
    st.plotly_chart(fig_rain)

    # 2️⃣ Kualitas Udara Tiap Daerah
    st.subheader("Kualitas Udara Tiap Daerah")
    category_counts = data.groupby('station')['Category'].value_counts().unstack().fillna(0)
    category_counts = category_counts[category_order]  # Mengurutkan kategori
    fig_quality = px.bar(category_counts, x=category_counts.index, y=category_counts.columns,
                         title='Distribusi Kualitas Udara per Stasiun', barmode='stack',
                         color_discrete_map=color_map)
    st.plotly_chart(fig_quality)

    # 3️⃣ Konsentrasi Polutan Terbesar di Setiap Daerah
    st.subheader("Konsentrasi Polutan Terbesar per Stasiun")
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    pollutant_stats = data.groupby('station')[pollutants].max().reset_index()
    fig_pollutants = px.bar(pollutant_stats.melt(id_vars=['station']), x='station', y='value', color='variable',
                            title='Konsentrasi Polutan Terbesar per Stasiun', barmode='group')
    st.plotly_chart(fig_pollutants)
