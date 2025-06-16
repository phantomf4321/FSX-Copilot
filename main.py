import speech_recognition as sr
import pyautogui
import time
import os

def display_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("     ✈️  Voice-Controlled Flight Assistant (v1.0)     ")
    print("=" * 50)
    print("Available Voice Commands:")
    print("{:<30} {:<20}".format("Command", "Action"))
    print("-" * 50)
    print("{:<30} {:<20}".format("gears up / gears down", "Press 'G'"))
    print("{:<30} {:<20}".format("set flaps for takeoff", "Press 'F6' x3"))
    print("{:<30} {:<20}".format("flaps up", "Press 'F6'"))
    print("{:<30} {:<20}".format("flaps down", "Press 'F7'"))
    print("{:<30} {:<20}".format("flaps full", "Press 'F8'"))
    print("{:<30} {:<20}".format("lights", "Press 'L'"))
    print("{:<30} {:<20}".format("full stop", "Throttle + Brake"))
    print("=" * 50)
    print("Say a command after the prompt...\n")

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")

        if "gears up" in command or "gears down" in command or "gears" in command or "years" in command:
            print("Command recognized! Pressing 'G' key...")
            pyautogui.press('g')

        elif "set flaps for takeoff" in command:
            print("Command recognized! Pressing 'F6' key 3 times...")
            for _ in range(3):
                pyautogui.press('f6')
                time.sleep(0.1)

        elif "flaps up" in command:
            print("Command recognized! Pressing 'F6' key...")
            pyautogui.press('f6')

        elif "flaps down" in command:
            print("Command recognized! Pressing 'F7' key...")
            pyautogui.press('f7')

        elif "flaps full" in command:
            print("Command recognized! Pressing 'F8' key...")
            pyautogui.press('f8')

        elif "lights" in command:
            print("Command recognized! Pressing 'L' key...")
            pyautogui.press('l')

        elif "full stop" in command:
            print("Command recognized! Pressing throttle and brake keys...")
            pyautogui.press('f1')
            pyautogui.hotkey('ctrl', '.')

        else:
            print("Command not recognized in defined list.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def main():
    display_header()
    while True:
        listen_for_command()
        time.sleep(0.25)

if __name__ == "__main__":
    main()
