import streamlit as st
from modules.whisper_stt import gravar_audio, transcrever_audio
from modules.llama_interface import chamar_llama
from modules.tts import falar_texto

st.title("🦙 Assistente de Voz com LLaMA 3.1")

if st.button("🎤 Gravar e Perguntar"):
    caminho = gravar_audio()
    texto_usuario = transcrever_audio(caminho)
    st.write("Você disse:", texto_usuario)

    resposta = chamar_llama(texto_usuario)
    st.write("🤖 Resposta:", resposta)

    falar_texto(resposta)
