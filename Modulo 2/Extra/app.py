import streamlit as st

st.title('Vendinha do Tuê')
st.subheader('Venha fazer parte da Vendinha')
st.sidebar.image('logo.png')

nome = st.text_input('Digite o nome do seu funcionario')
idade = st.text_input('Digite a idade do seu funconario')
email = st.text_input('Digite o email do seu funcionario')
salario = st.text_input('Digite o salario do seu funcionario')
cargos = st.text_input('Digite o cargo do seu funcionario')

if st.button('Cadastrar'):
    st.warning(f'O funcionario {nome} foi conratado')
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')