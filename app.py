import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Başlık
st.title("Hava Kirliliği Tahminleme Uygulaması")

# Modeli ve Scaler'ı yükle
model = joblib.load("eniyi.joblib")      # Eğitilmiş model

# Kullanıcı girdisi için giriş alanları
st.header("Giriş Değerlerini Girin:")
pm25 = st.number_input("PM 2.5 (µg/m3):", min_value=0.0, format="%.2f")
so2 = st.number_input("SO2 (µg/m3):", min_value=0.0, format="%.2f")
co = st.number_input("CO (µg/m3):", min_value=0.0, format="%.2f")
no2 = st.number_input("NO2 (µg/m3):", min_value=0.0, format="%.2f")
nox = st.number_input("NOX (µg/m3):", min_value=0.0, format="%.2f")
no = st.number_input("NO (µg/m3):", min_value=0.0, format="%.2f")

# Tahminleme butonu
if st.button("Tahminle"):
    # Girdi verilerini DataFrame formatında birleştir
    input_data = pd.DataFrame([[pm25, so2, co, no2, nox, no]],
                              columns=['PM 2.5 ( µg/m3 )', 'SO2 ( µg/m3 )', 'CO ( µg/m3 )', 
                                       'NO2 ( µg/m3 )', 'NOX ( µg/m3 )', 'NO ( µg/m3 )'])

    prediction = model.predict(input_data)
    prediction_value = float(prediction[0])

    # Sonucu ekrana yazdır
    st.success(f"Tahmin Edilen PM10 Değeri: {prediction_value:.2f} µg/m3")
