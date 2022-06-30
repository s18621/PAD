import streamlit as st
import pandas as pd
import time
import plotly.express as px
import streamlit.components.v1 as components
from pivottablejs import pivot_ui


st.sidebar.title('PAD Project')
myPage = st.sidebar.selectbox('Choose a Tab:', ['Statistics'])

if myPage == 'Statistics':
    st.title('Stats')
    info = 'data.csv'
    teams = 'teams.csv'

    if info is not None:
        with st.spinner('Loading...'):
            df = pd.read_csv(info, sep=',')
            dfT = pd.read_csv(teams, sep=',')
            time.sleep(2)
        st.dataframe(df)

        g_type = st.selectbox('Choose chart type', ('Pivot', 'Pie', 'Histogram'))

        if(g_type) == 'Pie':
            fig3 = px.pie(df, values='Gamelength', names='Side',title="Victories by Side and Time", color='Side', width=500)
            st.plotly_chart(fig3)
            st.markdown('Procentowa wygrana obu stron na postawie czasu gry \n Widać wyraźnie, że czas ma wpływ na wygrywanie gier przez konkretną stronę')


        if(g_type) == 'Histogram':
            fig = px.histogram(dfT, "Tag", "Wins" ,title="Victories by Team")
            st.plotly_chart(fig)
            st.markdown('Wykres dotyczący ilości wygranych danej drużyny we wszsytkich mistrzostwach \n Z danych historycznych, drużyny które częściej zwyciężały stawały się bardziej popularne wsród widowni na arenie międzynarodowej')

            figOne = px.histogram(df, "Year", color="Type")
            figOne.update_yaxes(matches=None, showticklabels=True)
            st.plotly_chart(figOne)   
            st.markdown('Wykres pokazujący liczbę gier danego typu na przestrzeni lat \n Widać tendencję, że z każdym rokiem coraz więcej mistrzostw było organizowane')

            fig2 = px.histogram(df, 'Side',title="Victories by Side", color='Side', width=500)
            st.plotly_chart(fig2)
            st.markdown('Zwycięstwa na podstawie strony wygranej drużyny \n Widać tendencję, że niebieska strona znacznie częściej wygrywa')
        
        if(g_type) == 'Pivot':
            league_df = df.pivot_table('Result', 'League', 'Year')
            st.dataframe(league_df)
            st.markdown('Wykres pokazujący liczbę zwycięstw na podstawie strony na wszystkich mistrzostwach w kolejnych latach \n jako 1 oznaczone są drużyny niebieskie, a jako 0, drużyny czerwone \n Widać również, że w niekótrych latach nie odbyły się dane mistrzostwa')

            length_df = df.pivot_table('Result', 'Gamelength', 'League')
            st.dataframe(length_df)
            st.markdown('Wykres pokazujący wygraną stronę na podstawie czasu gry')

            Blue_df = df.pivot_table('Result', 'Year', 'BlueTeamTag')
            st.dataframe(Blue_df)
            st.markdown('Wykres pokazujący wygrane drużyn po stronie niebieskich w latach')

            Red_df = df.pivot_table('Result', 'Year', 'RedTeamTag')
            st.dataframe(Red_df)
            st.markdown('Wykres pokazujący wygrane drużyn po stronie czerwonych w latach')