import speech_recognition as sr
import webbrowser
import pyautogui

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def run(self):
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
            
            try:
                recognized_text = self.recognizer.recognize_google(audio, language='ka-GE')
                print("Recognized command: ", recognized_text)
                self.process_command(recognized_text)
                
                if recognized_text.lower() == "ნახვამდის":
                    break

            except sr.UnknownValueError:
                print("Sorry, I could not understand your command.")
            except sr.RequestError as e:
                print("Could not request results from the ASR service:", str(e))

    def process_command(self, command):
        if "გახსენი" in command:
            if "youtube" in command:
                self.open_website("https://www.youtube.com")
            elif "argusi" in command:
                self.open_website("https://argus.iliauni.edu.ge/ka")
            elif "ფეისბუქი" in command or "facebook" in command:
                self.open_website("https://www.facebook.com/")
        elif "რა არის" in command:
            search_query = "+".join(command.split(" ")[2:])
            self.search_google(search_query)
        elif "ხმოვანი მართვა" in command:
            self.voice_control_mouse()

    def open_website(self, link):
        webbrowser.open(link)

    def search_google(self, query):
        link = "https://www.google.com/search?q=" + query
        webbrowser.open(link)

    def voice_control_mouse(self):
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            try:
                recognized_text = self.recognizer.recognize_google(audio, language='ka-GE')
                print("Recognized command:", recognized_text)
                if recognized_text.lower() == "stop" or recognized_text.lower() == "სტოპ":
                    break
                self.move_mouse(recognized_text)

            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service:", str(e))

    def move_mouse(self, command):
        arr_com = command.split(" ")
        try:
            if "მარჯვნივ" in command:
                current_x, current_y = pyautogui.position()
                current_x += int(arr_com[1])
                pyautogui.moveTo(current_x, current_y, duration=1)
            elif "მარცხნივ" in command:
                current_x, current_y = pyautogui.position()
                current_x -= int(arr_com[1])
                pyautogui.moveTo(current_x, current_y, duration=1)
            elif "ზემოთ" in command:
                current_x, current_y = pyautogui.position()
                current_y -= int(arr_com[1])
                pyautogui.moveTo(current_x, current_y, duration=1)
            elif "ქვემოთ" in command:
                current_x, current_y = pyautogui.position()
                current_y += int(arr_com[1])
                pyautogui.moveTo(current_x, current_y, duration=1)
            elif "გახსენი" in command:
                pyautogui.click()
        except ValueError:
            pass

assistant = VoiceAssistant()
assistant.run()
