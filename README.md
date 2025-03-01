# HackIndia-Spark-1-2025-CodeRed
This project empowers individuals with physical disabilities by enabling hands-free computer access through voice commands and facial gestures. It allows users to control the cursor, click, scroll, and type without needing a keyboard or mouse, promoting independence and digital accessibility.

# Gesture & Voice Control Accessibility

## Overview
This project enables hands-free computer interaction using face-tracking and voice commands. It integrates:
- **Face Tracking (noseLandmarkCursor.py)**: Controls the mouse cursor using nose movement.
- **Speech Recognition (speechRecorgnition_updated.py)**: Executes voice commands for cursor clicks, scrolling, typing, and application control.
- **GUI Interface (main.py)**: A simple Tkinter-based UI to launch both features.

## Features
- Move the cursor using facial landmarks
- Perform left/right clicks, scrolling, and window control via voice
- Voice-based Gemini AI activation for search queries
- Supports Tamil & English voice recognition

## Installation
### Prerequisites:
Ensure you have the following installed:
- Python 3.x
- Required libraries:
download command: pip install opencv-python dlib pyautogui speechrecognition pyttsx3 googletrans google-generativeai

 Download `shape_predictor_68_face_landmarks.dat` from [dlib models](data/shape_predictor_68_face_landmarks.dat) and place it in the project directory.

## Usage
1. Run `main.py` to start the GUI.
2. Click "Start" to launch speech and face tracking features.
3. Control the cursor with head movements.
4. Use voice commands to interact with the system.

## Voice Commands
- `"left click"`, `"right click"`, `"scroll up"`, `"scroll down"`
- `"activate gemini"`, `"deactivate gemini"` (AI assistant)
- `"exit"`, `"close tab"`, `"enter"`
- `"move left/right/up/down"`
- `"type <text>"`

## Notes
- Ensure the webcam is functional for face tracking.
- Background noise can affect speech recognition accuracy.

## Contributors
- SP.Sethumathavan
- T.K.Siva Subanesh
- Rajavarshan.R.R
- K.Tamil Selvan

# User Log - Gesture & Voice Control Accessibility (NaamaDhan - CodeRed)

## **Session Start**
1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Run the following command to start the application:
  4. The GUI window will appear with the **"Start"** button.
  5. Click **"Start"** to enable voice and face tracking.
  
  ---
  
  ## **Using Face Tracking (Cursor Control)**
  - Ensure your webcam is enabled.
  - Move your **nose** to control the cursor position.
  - The system detects eye landmarks to track movement.
  
  ---
  
  ## **Using Voice Commands**
  - Speak clearly into the microphone.
  - Supported voice commands:
  
  **Mouse Control**
  - `"left click"` → Left mouse click
  - `"right click"` → Right mouse click
  - `"scroll up"` → Scroll up
  - `"scroll down"` → Scroll down
  - `"double click"` → Double click
  
  **Keyboard Control**
  - `"enter"` → Presses Enter key
  - `"space"` → Presses Spacebar
  - `"exit"` → Closes the active window
  - `"close tab"` → Closes the current tab
  - `"type <your text>"` → Types the specified text
  
  **Window Management**
  - `"move left"` → Moves active window left
  - `"move right"` → Moves active window right
  - `"move up"` → Moves active window up
  - `"move down"` → Moves active window down
  
  **AI Assistant (Gemini)**
  - `"activate gemini"` → Activates AI assistant
  - `"deactivate gemini"` → Deactivates AI assistant
  - Ask any question after activation, e.g., `"What is AI?"`
  
  **Language Switching**
  - `"ஆங்கிலம்"` → Switches to Tamil recognition
  - `"tamil"` → Switches back to English recognition
  
  ---
  
  ## **Stopping the Application**
  - To stop only the **AI assistant**, say:  
  `"deactivate gemini"`
  - To exit voice control, say:  
  `"stop"`
  - To exit the entire application, close the GUI window or press **`Esc`** in the face-tracking window.
  
  ---
  
  ## **Troubleshooting**
  - If the webcam is not detected, restart the application.
  - If voice commands do not work:
  - Ensure the microphone is working.
  - Reduce background noise.
  - Speak clearly and loudly.
  - If face tracking is not responsive:
  - Adjust your lighting conditions.
  - Ensure your face is visible in the webcam.
  
  ---
  
  ## **Session End**
  1. Close the application manually.
  2. Ensure no background processes are running.
  3. Restart the application if needed.
  
  **Enjoy hands-free control!**
