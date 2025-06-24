# FSX Co-Pilot: Voice Control Assistant for Flight Simulator X

## Overview  
FSX Co-Pilot is a voice command software designed to enhance the Microsoft Flight Simulator X (FSX) experience by allowing pilots to control key aircraft functions through natural speech commands. This Python-based application provides hands-free operation of critical flight systems, improving immersion and accessibility.

## Key Features

- **Voice-Activated Controls**: Uses speech recognition to interpret pilot commands  
- **Comprehensive Command Set**: Supports over 15 essential aircraft functions  
- **Logging System**: Maintains detailed records of all voice commands and system responses  
- **User-Friendly Interface**: Simple GUI with status display and log viewer  
- **Background Operation**: Runs alongside FSX without interfering with gameplay  

## Supported Commands

### Flight Controls:
- `Gears` / `Gear` - Lowers/raises landing gear (`G` key)  
- `Flaps up/down/full` - Adjusts flap positions (`F6-F8` keys)  
- `Set flaps for takeoff/landing` - Configures optimal flap settings  
- `Reverse` - Activates reverse thrust (`F2` key)  
- `Brake` / `Touch` - Controls wheel brakes (`.` and `/` keys)  

### Aircraft Systems:
- `Lights` - Toggles aircraft lighting (`L` key)  
- `Main door` / `Cargo door` - Operates doors (`Ctrl+E` combinations)  
- `Connect gate` - Requests gate connection (`Ctrl+J`)  

### Ground Operations:
- `Push back` - Initiates pushback procedure (`Shift+P`)  
- `Full stop` - Cuts throttle and applies full brakes (`F1` + `Ctrl+.`)  

## Technical Implementation

- Built with Python using `speech_recognition` and `pyautogui` libraries  
- Features a multi-threaded architecture for responsive operation  
- Includes a logging system with search and filtering capabilities  
- Optional background image for enhanced visual appeal  
- Lightweight design with minimal system impact  

## Benefits  

- ✈️ **Hands-Free Operation**: Keep hands on yoke/throttle while managing systems  
- 🎧 **Improved Realism**: More authentic cockpit experience with voice commands  
- ♿ **Accessibility**: Helps pilots with physical limitations  
- 📚 **Training Aid**: Useful for practicing proper phraseology and procedures  

> The FSX Co-Pilot bridges the gap between simulation and real-world aviation by bringing natural voice interaction to the virtual cockpit environment.