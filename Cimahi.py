import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':orange[STATISTIK] :blue[DAERAH] :green[KOTA CIMAHI]')

st.subheader('', divider='rainbow')

with st.expander('PENGANTAR'):
    st.success('Aplikasi ini berisi kumpulan Indikator Makro yang resmi dirilis oleh Badan Pusat Statistik, \
        ditambah data-data lain yang sumber resminya tercantum.')
    st.info('Aplikasi ini dibuat untuk memudahkan Para Pemangku Kepentingan dalam proses Perencanaan, Pelaksanaan, \
        Monitoring dan Evaluasi Pembangunan di Kota Cimahi.')
    st.warning('Silakan mengakses setiap indikator makro melalui menu di sebelah kiri.')

st.subheader('', divider='green')

kol1, kol2, kol3, kol4 = st.columns(4)
with kol1:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':green[Luas Wilayah (Km2)]')
            st.header(':green[42,43]')

with kol2:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':blue[Jumlah Kecamatan]')
            st.header(':blue[3]')

with kol3:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':orange[Jumlah Kelurahan]')
            st.header(':orange[15]')

with kol4:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':blue[Jumlah Desa]')
            st.header(':blue[0]')

            
with st.expander('Catatan'):
    st.caption('Berdasarkan Keputusan Menteri Dalam Negeri No. 050-145 Tahun 2022')

st.subheader('', divider='rainbow')
st.caption(':green[Statistik Daerah Kota Cimahi]')
st.caption(':green[Hak Cipta @ BPS Kota Cimahi]')