import streamlit as st
import pandas as pd
import time
import plotly.express as px


st.sidebar.title('PAD_10')
myPage = st.sidebar.selectbox('Wybierz zakladke:', ['Ankieta', 'Statystyki'])

if myPage == 'Ankieta':
    st.title('Ankieta')
    f_name = st.text_input('Imię: ')
    l_name = st.text_input('Nazwisko: ')

    if st.button('OK'):
        if f_name.isalpha() and l_name.isalpha():
            st.success('Wypelniono formularz!')
            with open('ankieta.csv', 'a') as file:
                file.write(','.join([f_name, l_name]))
                file.write('\n')
                file.close()
        else:
            st.error('Blad przy wprowadzaniu danych')

if myPage == 'Statystyki':
    st.title('Statystyki')

    info = st.file_uploader('Wczytaj dane', type=['csv'])

    if info is not None:
        with st.spinner('Loading...'):
            df = pd.read_csv(info, sep=',')
            time.sleep(2)
        st.dataframe(df)


        g_type = st.selectbox('Podaj typ wykresu', ('Barplot', 'Pieplot'))
        types = tuple(x for x in df.columns if df[x].dtype in ['str','object'])

        if g_type == 'Barplot':
            vb = st.selectbox('Wybierz zmienną',types)
            df_num = df[vb].value_counts().reset_index()
            barplot = px.bar(df_num, x = 'index', y = vb)
            st.plotly_chart(barplot)
        
        if(g_type) == 'Pieplot':
            vp = st.selectbox('Wybierz zmienną x', types)
            df_num = df[vp].value_counts().reset_index()
            pieplot = px.pie(df_num, values=vp, names=vp)
            st.plotly_chart(pieplot)