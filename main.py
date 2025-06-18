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
            status_label.config(text="Ready for command...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            status_label.config(text=f"Command: {command}")

            if "gears" in command or "gear" in command:
                print("G")

            elif "contact" in command:
                pyautogui.press('~')

            elif "flaps take" in command:
                for i in range(3):
                    pyautogui.press('f6')
                    time.sleep(0.1)

            elif "flaps up" in command or "flap up" in command:
                pyautogui.press('f6')

            elif "flaps down" in command or "flap down" in command:
                pyautogui.press('f7')

            elif "flaps full" in command or "flap full" in command:
                pyautogui.press('f8')

            elif "lights" in command or "light" in command:
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
                print(command)

        except sr.UnknownValueError:
            status_label.config(text="Could not understand.")
        except sr.RequestError as e:
            status_label.config(text=f"API error: {e}")


def start_listening_thread():
    thread = threading.Thread(target=listen_loop, daemon=True)
    thread.start()

app = tk.Tk()
app.title("FSX Co-Pilot")
app.geometry("800x500")
app.resizable(False, False)

bg_image = Image.open("background.png")
bg_image = bg_image.resize((800, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

status_label = tk.Label(app, text="Initializing voice recognition...", font=("Arial", 14), bg="white")
status_label.pack(pady=20)

start_listening_thread()

app.mainloop()
