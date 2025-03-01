import speech_recognition as sr
import pyautogui
import pygetwindow as gw
import pyttsx3
import google.generativeai as genai
from googletrans import Translator
from IPython.display import clear_output, display, Markdown
import asyncio
import sys
from langdetect import detect

sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "AIzaSyDTrzcaUzOX5XQvpf6JGByPNOzXtsEj3dg"
recognizer = sr.Recognizer()
genai.configure(api_key=API_KEY)
    
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def search_gemini(txt,lang):
    translator = Translator()
    API_KEY = "AIzaSyDTrzcaUzOX5XQvpf6JGByPNOzXtsEj3dg"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    prompt = txt
    response = model.generate_content(prompt)
    if lang == "ஆங்கிலம்":
        translated = asyncio.run(translator.translate(response.text, src="en", dest="ta"))    
        print(translated.text)
    print(response.text)
# search_gemini("what are you ")

def get_active_window():
    window = gw.getActiveWindow()
    return window if window else None

# Move the active window
def move_window(direction, step=100):
    window = get_active_window()
    if window:
        x, y = window.left, window.top
        if direction == "right":
            window.moveTo(x + step, y)
        elif direction == "left":
            window.moveTo(x - step, y)
        elif direction == "up":
            window.moveTo(x, y - step)
        elif direction == "down":
            window.moveTo(x,y+step)

    
def activate_gemini():
    lang = "tamil"
    text_to_speech("gemini activated")
    while True:
            with sr.Microphone() as source:
                print("Listening...")
                try:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                    print("Recognizing...")
                    # text = recognizer.recognize_google(audio)+"give in short"
                    if lang == "tamil":
                        try:
    # Try recognizing in Tamil
                            text = recognizer.recognize_google(audio, language="ta-IN")
                        except sr.UnknownValueError:
                            pass
                    else:
                        try:
                            # If Tamil fails, try English
                            text = recognizer.recognize_google(audio, language="en")
                        except sr.UnknownValueError:
                            print("Could not understand audio")
                            exit()
                    if text == "ஆங்கிலம்":
                        lang = "ஆங்கிலம்"
                        continue
                    elif text == "tamil":
                        lang = "tamil"
                        continue
                    # Detect language dynamically
                    detected_lang = detect(text)

                    if detected_lang == "ta":
                        print("Tamil:", text)
                    else:
                        print("English:", text)
                    if(text in ("deactivate gemini","deactivate","deactivate gemini","stop gemini","de-activate gemini","de activate gemini")):
                        text_to_speech("gemini deactivated")
                        break
                    search_gemini(text,lang)
                    
                except sr.UnknownValueError:
                    print("Sorry, could not understand the audio.")
                except sr.RequestError as e:
                    print(f"API Error: {e}")
                
def voiceRecorgnise():
    # Initialize recognizer
    

    text="start"
    
    
    while(text != "stop"):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                
                print(f"Recognized Text: {text}")
                if(text == "left click"):
                    pyautogui.leftClick()
                    text_to_speech("left clicked")
                elif(text == "right click"):
                    pyautogui.rightClick()
                    text_to_speech("right clicked")
                elif(text == "scroll down"):
                    pyautogui.press('pagedown')
                    text_to_speech("scrolled down")
                elif(text == "scroll up"):
                    pyautogui.press('pageup')
                    text_to_speech("scrolled up")
                elif(text == "space" or text == "pause"):
                    pyautogui.press('space')
                    if(text=="space"):
                        text_to_speech("spaced")
                    else:
                        text_to_speech("paused")
                elif(text == "zooom in"):
                    pyautogui.hotkey("ctrl","shift","+")
                    text_to_speech("zoomed in")
                elif(text == "zoom out"):
                    pyautogui.hotkey("ctrl","-")
                    text_to_speech("zoomed out")
                elif(text == "exit"):                                                         
                    pyautogui.hotkey("alt","f4")
                    text_to_speech("exited")
                elif(text == "close tab"):                                                   
                    pyautogui.hotkey("ctrl","w")
                    text_to_speech("tab closed")
                elif text[0:4] == "move":
                    move_window(text[5:])  # Move window to the right
                elif(text == "enter"): 
                    pyautogui.press('enter')
                    text_to_speech("entered")
                elif(text[0:4] == "type"):
                    pyautogui.typewrite(text[5:])
                    text_to_speech("text has been typewrited")
                elif(text=="double click"):
                    pyautogui.doubleClick()
                    text_to_speech("double clicked")
                elif(text.lower().strip() in ("activate gemini","activate gem")):
                    activate_gemini()
            except sr.UnknownValueError:
                print("Sorry, could not understand the audio.")
            except sr.RequestError as e:
                print(f"API Error: {e}")
voiceRecorgnise()