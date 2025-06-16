import speech_recognition as sr
import pyautogui
import time
import tkinter as tk
from PIL import Image, ImageTk
import threading

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        status_label.config(text="Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        status_label.config(text=f"Recognized: {command}")

        if "gears" in command or "years" in command:
            pyautogui.press('g')

        elif "set flaps for takeoff" in command:
            for _ in range(3):
                pyautogui.press('f6')
                time.sleep(0.1)

        elif "flaps up" in command:
            pyautogui.press('f6')

        elif "flaps down" in command:
            pyautogui.press('f7')

        elif "flaps full" in command:
            pyautogui.press('f8')

        elif "lights" in command:
            pyautogui.press('l')

        elif "full stop" in command:
            pyautogui.press('f1')
            pyautogui.hotkey('ctrl', '.')

    except sr.UnknownValueError:
        status_label.config(text="Could not understand audio.")
    except sr.RequestError as e:
        status_label.config(text=f"API error: {e}")

def start_listening():
    threading.Thread(target=listen_for_command).start()

# GUI Setup
app = tk.Tk()
app.title("FSX Co-Pilot")
app.geometry("800x500")

# Background image
bg_image = Image.open("background.jpg")  # Use your generated cockpit image
bg_image = bg_image.resize((800, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

status_label = tk.Label(app, text="Press Start and Speak", font=("Arial", 14), bg="white")
status_label.pack(pady=20)

start_button = tk.Button(app, text="Start Listening", command=start_listening, font=("Arial", 12), bg="lightblue")
start_button.pack()

app.mainloop()
