import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="", base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.write("## ChatBot de IA")

#Historico de mensagem
if not "message_list" in st.session_state:
    st.session_state["message_list"] = [] 

user_message = st.chat_input("Escreva sua mensagem aqui")

for menssagem in st.session_state["message_list"]:
    quem_enviou = menssagem["role"]
    texto_mensagem = menssagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)
    
if user_message:
    # pega a resposta do usuario
    st.chat_message("user").write(user_message) 
    message1 = {"role": "user", "content": user_message}
    st.session_state["message_list"].append(message1)

    # pega a resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages= st.session_state["message_list"],
        model="gemini-flash-lite-latest"
    ) 
    
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia) # envia a mensagem da IA no chat
    message2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["message_list"].append(message2)