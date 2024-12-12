# Voice Assistant Using Python

This project is a versatile **Voice Assistant** built with Python, capable of handling multiple tasks like opening applications, searching the web, automating typing, and more. It is designed for ease of use, modularity, and extensibility, making it a great tool for personal productivity or an educational project.

---

## Features

- **Application Control:**
  - Open and close installed applications by name using advanced search methods (directories, environment variables, start menu, and Windows registry).
  
- **Web Integration:**
  - Open websites and search queries on Google and YouTube.
  - Play videos directly on YouTube using voice commands.

- **Wikipedia Integration:**
  - Retrieve concise summaries of topics or people from Wikipedia.

- **Text Automation:**
  - Automate typing tasks by dictating text.

- **Dynamic Greeting:**
  - Greets users based on the time of day with a customizable message.

- **Conversational Interaction:**
  - Uses **speech recognition** for user commands and provides **text-to-speech** responses.

---

## Technologies Used

- **Python Libraries:**
  - `pyttsx3` for text-to-speech conversion.
  - `speech_recognition` for recognizing voice commands.
  - `wikipedia` for fetching summaries from Wikipedia.
  - `webbrowser` and `pywhatkit` for web-based tasks.
  - `pyautogui` for automating typing tasks.
  - `subprocess` and `os` for application management.
  - `winreg` for searching installed applications in the Windows registry.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant-python.git
   cd voice-assistant-python
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python voice_assistant.py
   ```

---

## Usage

1. Launch the voice assistant.
2. Use voice commands for various actions, such as:
   - **"Open Google"**: Opens Google.com in the default browser.
   - **"Search for Tesla on Wikipedia"**: Retrieves a summary about Tesla.
   - **"Play Despacito on YouTube"**: Plays the specified video on YouTube.
   - **"Open Telegram"**: Opens the Telegram application if installed.
   - **"Close Telegram"**: Closes the Telegram application if running.

---

## Example Commands

- **"What is Python?"**: Searches for Python on Wikipedia.
- **"Open Notepad"**: Opens the Notepad application.
- **"Close Notepad"**: Closes Notepad.
- **"Type Hello, World!"**: Automatically types "Hello, World!" into the current window.
