import speech_recognition as sr
import pyautogui
import time
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import threading
import os
from datetime import datetime

# Constants
LOG_FILE = "voice_commands.log"
MAX_LOG_ENTRIES = 2500


class CommandLogger:
    def __init__(self, log_file=LOG_FILE, max_entries=MAX_LOG_ENTRIES):
        self.log_file = log_file
        self.max_entries = max_entries
        self.initialize_log_file()

    def initialize_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("Voice Command Log - Created on {}\n\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def log_command(self, command, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {command} - {status}\n"

        # Read existing logs
        with open(self.log_file, 'r') as f:
            lines = f.readlines()

        # Keep header if exists
        header = []
        if lines and "Voice Command Log" in lines[0]:
            header = lines[:2]
            lines = lines[2:]

        # Add new entry and enforce max size
        lines.append(log_entry)
        if len(lines) > self.max_entries:
            lines = lines[-self.max_entries:]

        # Write back to file
        with open(self.log_file, 'w') as f:
            f.writelines(header + lines)

    def get_logs(self):
        try:
            with open(self.log_file, 'r') as f:
                return f.read()
        except:
            return "No logs available"


class LogViewer(tk.Toplevel):
    def __init__(self, parent, logger):
        super().__init__(parent)
        self.title("Command Log Viewer")
        self.geometry("800x600")
        self.logger = logger

        self.create_widgets()
        self.load_logs()

    def create_widgets(self):
        # Toolbar
        toolbar = ttk.Frame(self)
        toolbar.pack(fill=tk.X, padx=5, pady=5)

        refresh_btn = ttk.Button(toolbar, text="Refresh", command=self.load_logs)
        refresh_btn.pack(side=tk.LEFT, padx=2)

        clear_btn = ttk.Button(toolbar, text="Clear Logs", command=self.clear_logs)
        clear_btn.pack(side=tk.LEFT, padx=2)

        # Search frame
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        search_entry.bind("<KeyRelease>", self.on_search)

        # Log display
        self.log_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Consolas', 10))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def load_logs(self):
        logs = self.logger.get_logs()
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, logs)
        self.log_text.config(state=tk.DISABLED)
        self.log_text.yview(tk.END)

    def clear_logs(self):
        with open(self.logger.log_file, 'w') as f:
            f.write("Voice Command Log - Created on {}\n\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.load_logs()

    def on_search(self, event=None):
        search_term = self.search_var.get().lower()
        self.log_text.tag_remove('highlight', 1.0, tk.END)

        if search_term:
            start_pos = "1.0"
            while True:
                start_pos = self.log_text.search(search_term, start_pos, stopindex=tk.END, nocase=True)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_term)}c"
                self.log_text.tag_add('highlight', start_pos, end_pos)
                start_pos = end_pos

            self.log_text.tag_config('highlight', background='yellow')


def listen_loop(logger):
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
                logger.log_command(command, "Executed: G key pressed")
                print("G")

            elif "contact" in command:
                logger.log_command(command, "Executed: ~ key pressed")
                pyautogui.press('~')

            elif "flaps take" in command:
                logger.log_command(command, "Executed: F6 pressed 3 times")
                for i in range(3):
                    pyautogui.press('f6')
                    time.sleep(0.1)

            elif "flaps up" in command or "flap up" in command:
                logger.log_command(command, "Executed: F6 pressed")
                pyautogui.press('f6')

            elif "flaps down" in command or "flap down" in command:
                logger.log_command(command, "Executed: F7 pressed")
                pyautogui.press('f7')

            elif "flaps full" in command or "flap full" in command:
                logger.log_command(command, "Executed: F8 pressed")
                pyautogui.press('f8')

            elif "lights" in command or "light" in command:
                logger.log_command(command, "Executed: L key pressed")
                pyautogui.press('l')

            elif "full stop" in command:
                logger.log_command(command, "Executed: F1 pressed + Ctrl+.")
                pyautogui.press('f1')
                pyautogui.hotkey('ctrl', '.')

            elif "push back" in command:
                logger.log_command(command, "Executed: Shift+P pressed")
                pyautogui.hotkey('shift', 'p')

            elif "brake" in command:
                logger.log_command(command, "Executed: . key pressed")
                pyautogui.press('.')

            elif "touch" in command:
                logger.log_command(command, "Executed: / key pressed")
                pyautogui.press('/')

            else:
                status = "Unknown command"
                status_label.config(text=status)
                logger.log_command(command, status)
                print(command)

        except sr.UnknownValueError:
            status = "Could not understand audio"
            status_label.config(text=status)
        except sr.RequestError as e:
            status = f"API error: {e}"
            status_label.config(text=status)
            logger.log_command("API Request", status)


def start_listening_thread(logger):
    thread = threading.Thread(target=listen_loop, args=(logger,), daemon=True)
    thread.start()


def show_log_viewer():
    LogViewer(app, logger)


# Initialize the logger
logger = CommandLogger()

# Create main application window
app = tk.Tk()
app.title("FSX Co-Pilot")
app.geometry("400x300")
app.resizable(False, False)

# Try to load background image
try:
    bg_image = Image.open("assets/background.png")
    bg_image = bg_image.resize((400, 300))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(app, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except:
    # Fallback if image not available
    bg_label = tk.Label(app, bg='lightgray')
    bg_label.place(relwidth=1, relheight=1)

# Main UI elements
status_label = tk.Label(app, text="Initializing voice recognition...",
                        font=("Arial", 14), bg="white")
status_label.pack(pady=20)

# Add view logs button
view_logs_btn = ttk.Button(app, text="View Command Logs", command=show_log_viewer)
view_logs_btn.pack(pady=10)

# Start the listening thread
start_listening_thread(logger)

app.mainloop()