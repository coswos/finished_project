import pyttsx3

engine = pyttsx3.init()
voices = ["TTS_MS_EN-US_ZIRA_11.0", ]

def save_file(text):
    speach_text = f'./results/{text[0:7]}.mp3'
    engine.save_to_file(text, speach_text)
    engine.runAndWait()
    return speach_text
