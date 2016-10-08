import speech_recognition

recognizer = speech_recognition.Recognizer()


class user_commands:
    def __init__(self):
        pass

    @staticmethod
    def open_browser(browserCommand):
        print browserCommand


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)

    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recognition Error; {0}".format(e))

    return ""


def command(user_phrase):
    uc = user_commands()
    if user_phrase == 'hello':
        user_commands.open_browser(user_phrase)
    return user_phrase


def main():
    phrase = listen()
    print phrase
    print command(phrase)


if __name__ == '__main__':
    main()