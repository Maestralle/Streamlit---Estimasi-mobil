import pickle 
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))
st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('input Tahun mobil')
mileage = st.number_input('Input Jarak Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('input Konsumsi BBM mobil')
engineSize = st.number_input('Input Ukuran Mesin Mobil')

prediction = ''

if st.button('Estimasi Harga') : 
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('estimasi Harga Mobil Bekas dalam Pounds :', predict)
    st.write('estimasi Harga Mobil Bekas dalam Rupiah (Juta) :', predict*20164)