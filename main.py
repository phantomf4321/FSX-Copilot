import speech_recognition as sr
import pyautogui
import time
import tkinter as tk
from PIL import Image, ImageTk
import threading

def listen_loop():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with microphone as source:
            status_label.config(text="Ready for comand...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            status_label.config(text=f"Command: {command}")

            if "gears" in command or "years" in command:
                pyautogui.press('g')

            elif "flaps for takeoff" in command:
                for i in range(3):
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

            elif "push back" in command:
                pyautogui.hotkey('shift', 'p')

            elif "brake" in command:
                pyautogui.press('.')

            elif "touch" in command:
                pyautogui.press('/')

            else:
                status_label.config(text="Unknown command.")

        except sr.UnknownValueError:
            status_label.config(text="Could not understand.")
        except sr.RequestError as e:
            status_label.config(text=f"API error: {e}")

def start_listening_thread():
    thread = threading.Thread(target=listen_loop, daemon=True)
    thread.start()

# GUI Setupgl
app = tk.Tk()
app.title("FSX Co-Pilot")
app.geometry("800x500")
app.resizable(False, False)

# Background image
bg_image = Image.open("background.png")  # Use your cockpit image
bg_image = bg_image.resize((800, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

status_label = tk.Label(app, text="Initializing voice recognition...", font=("Arial", 14), bg="white")
status_label.pack(pady=20)

# Start listening right away
start_listening_thread()

app.mainloop()
