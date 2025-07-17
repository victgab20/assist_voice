import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import torch

print(torch.cuda.is_available())

device = "cuda" if torch.cuda.is_available() else "cpu"

def gravar_audio(duracao=5, fs=16000, nome_arquivo='audio.wav'):
    print("Gravando...")
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(nome_arquivo, fs, audio)
    return nome_arquivo

def transcrever_audio(caminho='audio.wav'):
    print("Transcrevendo áudio...")
    modelo = whisper.load_model("base", device=device)
    print("Modelo carregado:", modelo.is_multilingual)
    resultado = modelo.transcribe(caminho,language="pt")
    print("Transcrição concluída.")
    return resultado["text"]
