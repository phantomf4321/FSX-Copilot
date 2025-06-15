import speech_recognition as sr
import pyautogui
import time
import keyboard
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

        if "gears up" in command or "gears" in command or "years" in command or "gears down" in command:
            print("Command recognized! Pressing 'G' key...")
            pyautogui.press('g')

        if "falps up" in command:
            print("Command recognized! Pressing 'f6' key...")
            pyautogui.press('f6')

        if "falps down" in command:
            print("Command recognized! Pressing 'f7' key...")
            pyautogui.press('f7')

        if "falps full" in command:
            print("Command recognized! Pressing 'f8' key...")
            pyautogui.press('f8')

        if "lights" in command:
            print("Command recognized! Pressing 'L' key...")
            pyautogui.press('l')

        if "full stop" in command:
            print("Command recognized! Pressing 'stop' key...")
            pyautogui.press('f1')
            pyautogui.press('ctrl+.')

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


def main():
    print("Voice Command App - Say 'Gears up' to press the G key")
    while True:
        listen_for_command()
        time.sleep(1)  # Small delay to prevent CPU overuse

if __name__ == "__main__":
    main()