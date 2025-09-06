import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import datetime

st.set_page_config(page_title="LumiAll Dashboard", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://lumialldash.blob.core.windows.net/lumiall-data/icons/logo_lumiAll.png", width=180)
    st.title("Menu")
    nome = st.selectbox("Selecione o colaborador:", ["João Silva", "Maria Oliveira", "Carlos Souza"])
    periodo = st.date_input(
    "Selecione o intervalo:",
    [datetime.date.today() - datetime.timedelta(days=7), datetime.date.today()]
)

with st.container():

    st.title(f"Dashboard de Desempenho - Colaboradorª {nome}")

col1, col2, col3, col4 = st.columns(4, border=True)
col5, col6 = st.columns([1, 1], border=True)
col7, col8 = st.columns([2, 1], border=True)

with col1:
    st.metric("Tarefas Concluídas", "15", "+10%")

with col2:
    st.metric("Média Tempo", "3h", "-5%")

with col3:
    st.metric("Projetos Ativos", "5", "+1")

with col4:
    st.metric("Reuniões", "3", "+3%")

with col5:
    st.subheader("Desempenho ao Longo do Tempo")
    dates = pd.date_range(start=periodo[0], periods=30)
    performance = np.random.randint(1, 8, size=30)
    df_time = pd.DataFrame({"Data": dates, "Desempenho": performance})
    fig_time = px.line(df_time, x="Data", y="Desempenho", title="Desempenho Diário")
    st.plotly_chart(fig_time, use_container_width=True)

with col6:
    st.subheader("Engajamento Semanal")

    semanas = [1, 2, 3, 4]
    dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]

    data = np.random.randint(0, 10, size=(len(semanas), len(dias)))
    df = pd.DataFrame(data, index=semanas, columns=dias)
    df = df.reset_index().melt(id_vars="index")
    df.columns = ["Semana", "Dia", "Engajamento"]

    fig = px.imshow(
        data,
        labels=dict(x="Dia", y="Semana", color="Engajamento"),
        x=dias,
        y=[f"Semana {s}" for s in semanas],
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col7:
    subcol1, subcol2 = st.columns([1, 5])

    with subcol1:
        st.image("https://lumialldash.blob.core.windows.net/lumiall-data/icons/heart.png", width=25)
    
    with subcol2:
        st.subheader("Bem-estar")
    ssubcol1, ssubcol2 = st.columns(2)

    with ssubcol1:
        
        st.metric("Nível de Estresse", "Baixo")

    with ssubcol2:
        st.metric("Feedback do colaborador", "😄 😄 🙁 😄")

with col8:
    subcol3, subcol4 = st.columns([1, 5])
    with subcol3:
        st.image("https://lumialldash.blob.core.windows.net/lumiall-data/icons/autism_mind.png", width=25)
    with subcol4:
        st.subheader("Insights Rápidos")
        st.write("O colaborador manteve consistêcia nas ultimas 4 semanas.")
    
