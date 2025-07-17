import pyttsx3

def falar_texto(texto: str):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


