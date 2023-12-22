import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_yearly_rental_df(df):
    yearly_rental_df = day_df.resample(rule='Y', on='dteday').agg({
    "registered": "sum"
    })
    yearly_rental_df.index = yearly_rental_df.index.strftime('%Y') #mengubah format order date menjadi Tahun-Bulan
    yearly_rental_df = yearly_rental_df.reset_index()
    yearly_rental_df.rename(columns={
        "dteday": "Tahun",
        "registered": "Total_peserta"
    }, inplace=True)
    
    return yearly_rental_df


def create_season_rental_df(df):
    season_rental_df = day_df.groupby("season").registered.sum().sort_values(ascending=False).reset_index()
    season_rental_df.rename(columns={
        "registered": "Total_peserta"
    }, inplace=True)
  
    return season_rental_df


def create_hour_rental_df(df):
    hour_rental_df = hour_df.groupby("hr").registered.sum().sort_values(ascending=False).reset_index()
    hour_rental_df.rename(columns={
        "registered": "Total_peserta",
        "hr" : "Jam"
    }, inplace=True)
  
    return hour_rental_df



# Load cleaned data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")


datetime_columns = ["dteday"]

for column in datetime_columns:
  day_df[column] = pd.to_datetime(day_df[column])

for column in datetime_columns:
  day_df[column] = pd.to_datetime(hour_df[column])


# # Menyiapkan berbagai dataframe
yearly_rental_df = create_yearly_rental_df(day_df)
season_rental_df = create_season_rental_df(day_df)
hour_rental_df = create_hour_rental_df(hour_df)


# Dashboard
st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader("Bike Sharing")

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

col1, col2 = st.columns(2)

with col1:
    # Yearly rental
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
      y="Total_peserta", 
      x="Tahun",
      data=yearly_rental_df.sort_values(by="Tahun", ascending=True),
      palette=colors,
      ax=ax
      )
  
    ax.set_title("Jumlah customer per Tahun", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)


with col2:
    # Season rental
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
      y="Total_peserta", 
      x="season",
      data=season_rental_df.sort_values(by="season", ascending=True),
      palette=colors,
      ax=ax
      )
  
    ax.set_title("Jumlah customer per Season", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Hour rental
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="Total_peserta", 
    x="Jam",
    data=hour_rental_df.sort_values(by="Jam", ascending=True),
    palette=colors,
    ax=ax
)
ax.set_title("Jumlah customer per Hour", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


st.caption('Copyright © Dicoding 2023')
