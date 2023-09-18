import pyttsx3

def robo_speaker():
    engine = pyttsx3.init()

    # List of pre-defined responses
    responses = "I am your speaker, I will help you converse"

    print(f"Robo Speaker: {responses}")
    engine.say(responses)
    engine.runAndWait()
    while True:
        user_input = input("You: ")

        if user_input == 'q':
            print("Robo Speaker: Goodbye!")
            break

        # Speak the user's input
        engine.say(f" {user_input}")
        engine.runAndWait()

if __name__ == '__main__':
    robo_speaker()
