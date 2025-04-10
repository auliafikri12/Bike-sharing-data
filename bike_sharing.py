import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analisis data bike sharing")

st.caption("Analisis data bike sharing merupakan analisis data penjualan sepeda pada tahun 2011-2012. Data mentah dapat diperoleh dari file pada sidebar.")

tab_1 = "Penjelasan kasus"
tab_2 = "Analisis 1"
tab_3 = "Analisis 2"
tab_4 = "Analisis 3"
tab_5 = "Kesimpulan dan saran"

# Perbaikan di sini: Nama variabel konsisten dengan jumlah tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([tab_1, tab_2, tab_3, tab_4, tab_5])

day_df = pd.read_csv("https://raw.githubusercontent.com/auliafikri12/Bike-sharing-data/refs/heads/main/myfolder/day.csv")

# Ubah kolom dteday ke format datetime
day_df['dteday']= pd.to_datetime(day_df['dteday'])

#Definisi data penjualan rata-rata satu tahun pertama
First_year_data = day_df[day_df['dteday'] <= day_df['dteday'].min() + pd.DateOffset(years=1)]
First_year_data['month'] = First_year_data['dteday'].dt.month

monthlyfirst_avg_cnt = First_year_data.groupby('month')['cnt'].mean()

# Definisi data penjualan rata-rata satu tahun terakhir

last_year_data = day_df[day_df['dteday'] >= day_df['dteday'].max() - pd.DateOffset(years=1)]
last_year_data['month'] = last_year_data['dteday'].dt.month

monthly_avg_cnt = last_year_data.groupby('month')['cnt'].mean()

#Mencari faktor temperatur pada jumlah pelanggan
temp_cnt_df = First_year_data[['temp', 'cnt']]

temp_cnt_grouped = temp_cnt_df.groupby('temp')['cnt'].sum()

time_tempfirst_df = First_year_data[['dteday', 'temp']]

time_templast_df = last_year_data[['dteday', 'temp']]

time_humfirst_df = last_year_data[['dteday', 'hum']]

time_humlast_df = last_year_data[['dteday', 'hum']]

time_windspeedfirst_df = last_year_data[['dteday', 'windspeed']]

time_windspeedlast_df = last_year_data[['dteday', 'windspeed']]

avg_cnt_by_weather = First_year_data.groupby('weathersit')['cnt'].mean()

avg_cnt_by_weatherlast = last_year_data.groupby('weathersit')['cnt'].mean()

time_seasonfirst_df = First_year_data[['dteday', 'season']]

time_seasonlast_df = last_year_data[['dteday', 'season']]

avg_cnt_by_seasonfirst = First_year_data.groupby('season')['cnt'].mean()

avg_cnt_by_seasonlast= last_year_data.groupby('season')['cnt'].mean()

# Sidebar untuk download data
st.sidebar.header("Download data mentah")
st.sidebar.write("Download data yang diolah disini: ")
st.sidebar.download_button('Download CSV', day_df.to_csv(index=False), file_name='day.csv')





# Tab 1: Penjelasan Kasus
with tab1:
    st.title("Kasus bisnis Penjualan sepeda")
    st.caption("""
        Pada kasus ini, diberikan data penjualan sepeda di sebuah kota beserta beberapa kondisi di dalam kota 
        seperti cuaca, temperatur, dan lain-lain. Data-data ini dapat dianalisis dan digunakan untuk menjadi patokan 
        agar bisnis dapat dikembangkan dan keputusan bisnis dapat diperoleh dari data yang didapatkan dan diolah.
    """)
    st.caption("1. Bagaimana kondisi penjualan selama setahun terakhir?")
    st.caption("2. Kapan performa penjualan meningkat dan menurun?")
    st.caption("3. Faktor apa saja yang mempengaruhi performa dari penyewaan?")
    st.caption("Maka dari itu, kami mengolah data yang didapatkan untuk menganalisis ketiga pertanyaan tersebut dengan analisis dan visualisasi data.")
    
# Tab 2: Analisis 1
with tab2:
    st.header("Bagaimana kondisi penjualan sepeda selama setahun terakhir?")
    st.caption("Analis melakukan perhitungan rata-rata penjualan setiap bulan.")
    Bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    plt.figure(figsize=(10, 6))
    plt.bar(Bulan, monthly_avg_cnt.values)
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
    plt.xticks(rotation=45)
    plt.title('Rata-rata Jumlah Penyewaan Sepeda Bulanan selama tahun 2012')
    plt.show()
    st.pyplot(plt)
    st.caption("""Berdasarkan data barchart yang menampilkan rata-rata jumlah pelanggan dari kolom 'cnt', pada satu tahun terakhir, diperoleh jumlah total pelanggan meningkat di bulan Januari-september dan mulai turun pada September-Desember.""")

# Tab 3: Analisis 2
with tab3:
    st.header("Kapan performa penjualan meningkat dan menurun?")
    
    #Menampilkan barchart rata-rata jumlah pelanggan setiap bulan pada tahun 2011
    Bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    plt.figure(figsize=(10, 6))
    plt.plot(Bulan, monthlyfirst_avg_cnt.values)
    plt.scatter(Bulan, monthlyfirst_avg_cnt.values)
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
    plt.xticks(rotation=45)
    plt.title('Rata-rata Jumlah Penyewaan Sepeda Bulanan selama tahun 2011')
    st.pyplot(plt)
    
    #Menampilkan barchart rata-rata jumlah pelanggan setiap bulan pada tahun 2012
    Bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    plt.figure(figsize=(10, 6))
    plt.plot(Bulan, monthly_avg_cnt.values)
    plt.scatter(Bulan, monthly_avg_cnt.values)
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
    plt.title('Rata-rata Jumlah Penyewaan Sepeda Bulanan selama tahun 2012')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    st.caption("""Kedua data diatas, pada tahun 2011 dan 2012 menunjukkan adanya tren kenaikan jumlah pelanggan pada bulan Januari-April dan penurunan jumlah pembeli dari "cnt". Hal ini bisa jadi dikarenakan ada faktor-faktor yang mempengaruhi kenaikan dan penurunan pembeli pada bulan-bulan tertentu.""")

with tab4:
    st.header("Kapan performa penjualan meningkat dan menurun?")
    #Data Scatter plot vs Jumlah Pelanggan/Pembeli
    plt.figure(figsize=(10, 6))
    plt.scatter(temp_cnt_grouped.index, temp_cnt_grouped.values)
    plt.xlabel('Temperatur')
    plt.ylabel('Jumlah Pembeli')
    plt.title('Temperatur vs Jumlah Pelanggan')
    st.pyplot(plt)
    
    
    
    # Data Temperatur pada tahun 2011 timeseries
    plt.figure(figsize=(10, 6))
    plt.scatter(time_tempfirst_df['dteday'], time_tempfirst_df['temp'])
    plt.xlabel('Waktu')
    plt.ylabel('Temperatur')
    plt.title('Data Temperatur pada tahun 2011')
    st.pyplot(plt)
    
    #Data Temperatur pada tahun 2012
    plt.figure(figsize=(10, 6))
    plt.scatter(time_templast_df['dteday'], time_templast_df['temp'])
    plt.xlabel('Waktu')
    plt.ylabel('Temperatur')
    plt.title('Data Temperatur pada tahun 2012')
    st.pyplot(plt)
    
    
    #Data kelembapan pada tahun 2011
    plt.figure(figsize=(10, 6))
    plt.scatter(time_humfirst_df['dteday'], time_humfirst_df['hum'])
    plt.xlabel('Waktu')
    plt.ylabel('kelembapan')
    plt.title('Data kelembapan pada tahun 2011')
    st.pyplot(plt)
    
    #Data kelembapan pada tahun 2012
    plt.figure(figsize=(10, 6))
    plt.scatter(time_humlast_df['dteday'], time_humlast_df['hum'])
    plt.xlabel('Waktu')
    plt.ylabel('kelembapan')
    plt.title('Data kelembapan pada tahun 2012')
    st.pyplot(plt)
    #Data kecepatan udara pada tahun 2011
    plt.figure(figsize=(10, 6))
    plt.scatter(time_windspeedfirst_df['dteday'], time_windspeedfirst_df['windspeed'])
    plt.xlabel('Waktu')
    plt.ylabel('kecepatan udara')
    plt.title('Data kecepatan udara pada tahun 2011')
    st.pyplot(plt)
    #Data kecepatan udara pada tahun 2012
    plt.figure(figsize=(10, 6))
    plt.scatter(time_windspeedlast_df['dteday'], time_windspeedlast_df['windspeed'])
    plt.xlabel('Waktu')
    plt.ylabel('kecepatan udara')
    plt.title('Data kecepatan udara pada tahun 2012')
    st.pyplot(plt)
    #Jumlah pembeli di setiap cuaca 2011
    Cuaca = ['Cerah','berawan','hujan dan salju']
    plt.figure(figsize=(10, 6))
    plt.bar(Cuaca, avg_cnt_by_weather.values)
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah pembeli')
    plt.title('Jumlah pembeli di setiap cuaca 2011')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    #Jumlah pembeli di setiap cuaca 2012
    Cuaca =['Cerah','berawan','hujan dan salju']
    plt.figure(figsize=(10, 6))
    plt.bar(Cuaca, avg_cnt_by_weatherlast.values)
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah pembeli')
    plt.title('Jumlah pembeli di setiap cuaca 2012')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    #Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Musim pada tahun 2011
    Musim = ['semi', 'panas', 'gugur', 'dingin']
    plt.figure(figsize=(10, 6))
    plt.bar(Musim, avg_cnt_by_seasonfirst.values)
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Penyewaan')
    plt.title('Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Musim pada tahun 2011')
    st.pyplot(plt)
    #Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Musim pada tahun 2012
    Musim = ['semi', 'panas', 'gugur', 'dingin']
    plt.figure(figsize=(10, 6))
    plt.bar(Musim, avg_cnt_by_seasonlast.values)
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Penyewaan')
    plt.title('Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Musim pada tahun 2012')
    st.pyplot(plt)

    st.caption("""Berdasarkan data yang disajikan, kenaikan jumlah pada saat temperatur naik. Temperatur ini naik dengan puncak pada saat bulan juli di tahun 2011 dan 2012.
Selain itu musim gugur juga berpengaruh terhadap jumlah pembeli. Berdasarkan data yang disajikan, musim gugur terjadi pada bulan juli. Hal ini sesuai dengan data sebelumnya yang menunjukkan bahwa bulan juli merupakan puncak jumlah pelanggan.
Variabel lain seperti kecepatan udara dan kelembapan tidak berpengaruh terhadap jumlah pelanggan. Hal ini ditunjukkan dengan nilai variabel yang bergerak acak terhadap waktu.""")

    
    
with tab5:
    st.header("Kesimpulan")
    st.caption("Terdapat  tiga poin kesimpulan yang dapat diambil dari data ini.")
    st.caption("1. Selama setahun terakhir, berdasarkan data barchart yang menampilkan rata-rata jumlah pelanggan dari kolom 'cnt', pada satu tahun terakhir, diperoleh jumlah total pelanggan meningkat di bulan Januari-september dan mulai turun pada September-Desember.")
    st.caption("2. Berdasarkan analisis visualisasi data pada pertanyaan dua, Data Cenderung naik dari setiap Januari-Juli dan cenderung turun September-Desember.")
    st.caption("3. Faktor-faktor yang mempengaruhi penjualan sepeda adalah temperatur. Semakin besar nilai temperatur, semakin banyak pula peminat orang-orang untuk bersepeda sehingga penjualan meningkat. Temperatur hangat ini puncaknya terjadi pada bulan Juli yang sesuai dengan data yang ada. Pada bulan ini pula terjadi musim gugur yang merupakan puncak jumlah pelanggan ada.")
    st.header("Saran")
    st.caption("Perusahaan bisa memberikan diskon terhadap pembelian sepeda pada musim semi untuk meningkatkan penjualan. Hal ini karena tidak mungkin orang-orang untuk bersepeda pada musim dingin yang merupakan jumlah pelanggan terendah. Hal ini karena pada saat itu orang-orang cenderung menghindari aktivitas outdoor.")


