import subprocess
import time
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import threading

# def start():
def run_speech_recognition():
    subprocess.Popen(["python", "speechRecognition.py"], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, 
                     creationflags=subprocess.DETACHED_PROCESS)

# Function to Run Face Recognition in Background
def run_face_recognition():
    subprocess.Popen(["python", "noseLandmarkCursor.py"], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, 
                     creationflags=subprocess.DETACHED_PROCESS)

# Function to Start Both Features in Background
def start():
    threading.Thread(target=run_speech_recognition, daemon=True).start()
    threading.Thread(target=run_face_recognition, daemon=True).start()


if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("600x600")
    root.title("NaamaDhan - CodeRed")
    root.resizable(False, False)  # Prevent resizing for a cleaner UI

    # Load & Resize Background Image
    bg_image = Image.open("pixelcut-export.jpg")  # Ensure the image exists
    bg_image = bg_image.resize((600, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create Canvas (Allows Transparent Effect)
    canvas = tk.Canvas(root, width=600, height=600, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Set Background Image on Canvas
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)

    # Add Catchy & Attractive Text
    canvas.create_text(
        300, 100,  # X, Y Position (Centered)
        text="Gestures & Voice Control\n          Accessibility",  # Main Text
        font=("Helvetica", 30, "bold italic"),  # Bold & Italic for extra style
        fill="#fbf7d2",  # Golden Color for Attention
        activefill="#FF6347",  # Change color on hover (Tomato)
        tags="titl_text"
    )

    # Function for Hover Effect on Text (Change Text Color)
    def on_enter(e):
        canvas.itemconfig("title_text", fill="#FF6347")  # Change text color to Tomato when hovering

    def on_leave(e):
        canvas.itemconfig("title_text", fill="#fbf7d2")  # Restore color when not hovering

    # Bind Hover Effects to Title Text
    canvas.tag_bind("title_text", "<Enter>", on_enter)
    canvas.tag_bind("title_text", "<Leave>", on_leave)

    # Create "Transparent" Start Button (Canvas Text instead of Button)
    start_text = canvas.create_text(
        300, 450,  # X, Y Position (Centered)
        text="Start",
        font=("Arial", 24, "bold"),
        fill="white",  # Default text color
        activefill="#FF6347",  # Change color on hover
        tags="start_button"
    )

    # Function for Click Effect
    def on_click(e):
        start()  # Call the start function when text is clicked

    # Bind Click Event to "Button"
    canvas.tag_bind("start_button", "<Button-1>", on_click)
    canvas.tag_bind("start_button", "<Enter>", lambda e: canvas.itemconfig("start_button", fill="#FF6347"))
    canvas.tag_bind("start_button", "<Leave>", lambda e: canvas.itemconfig("start_button", fill="white"))

    # Run Application
    root.mainloop()