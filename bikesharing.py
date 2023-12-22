# Proyek Analisis Data: [Bike Sharing]
# - **Nama:** Sayed Muzammil
# - **Email:** smuzammil87@gmail.com
# - **ID Dicoding:** sayed_muzammil_tkog

## Menentukan Pertanyaan Bisnis

# - Pertanyaan 1 : Tahun mana yang paling banyak rental?
# - Pertanyaan 2 : Pada season apa orang banyak melakukan rental? 

## Import Semua Packages/Library yang Digunakan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

## Data Wrangling

### Gathering Data

day_df = pd.read_csv("day.csv")
day_df.head()


### Assessing Data

# **Menilai** data **day_df**

day_df.info()


print("Jumlah duplikasi: ", day_df.duplicated().sum())


day_df.describe()


day_df.nunique()


### Cleaning Data

# **Memperbaiki** tipe data **dteday**

datetime_columns = ["dteday"]

for column in datetime_columns:
  day_df[column] = pd.to_datetime(day_df[column])

day_df.info()


day_df.head()



## Exploratory Data Analysis (EDA)

### Explore day_df

day_df.describe(include="all")


# Mempersiapkan data per tahun

day_df.groupby(by="dteday").agg({
    "registered": ["max", "min", "mean", "std"]
})

# Mempersiapkan data per Season

day_df.groupby(by="season").agg({
    "registered": ["max", "min", "mean", "std"]
})

## Visualization & Explanatory Analysis

### Pertanyaan 1: Tahun mana yang paling banyak rental?

yearly_rental_df = day_df.resample(rule='Y', on='dteday').agg({
    "registered": "sum"
})

yearly_rental_df.index = yearly_rental_df.index.strftime('%Y') #mengubah format order date menjadi Tahun-Bulan
yearly_rental_df = yearly_rental_df.reset_index()
yearly_rental_df.rename(columns={
    "dteday": "Tahun",
    "registered": "Total_peserta"
}, inplace=True)
yearly_rental_df.head()

plt.figure(figsize=(10, 5))
colors = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]


sns.barplot(
    y="Total_peserta", 
    x="Tahun",
    data=yearly_rental_df.sort_values(by="Tahun", ascending=True),
    palette=colors
)
plt.title("Jumlah customer per Tahun", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

### Pertanyaan 2: Pada season apa orang banyak melakukan rental? 

season_rental_df = day_df.groupby("season").registered.sum().sort_values(ascending=False).reset_index()

season_rental_df.rename(columns={
    "registered": "Total_peserta"
}, inplace=True)
season_rental_df.head()


plt.figure(figsize=(10, 5))


sns.barplot(
    y="Total_peserta", 
    x="season",
    data=season_rental_df.sort_values(by="season", ascending=True),
)
plt.title("Jumlah customer per Tahun", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

## Conclusion

# - Conclution pertanyaan 1 : Lebih banyak jumlah rental di tahun 2012

# - Conclution pertanyaan 2 : Lebih banyak jumlah rental di season 3 (fall)
