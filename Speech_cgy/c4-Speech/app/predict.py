import pyttsx3


def predict(input_str):
    c2_output, c3_output = str(input_str).split("|")
    engine = pyttsx3.init()
    engine.say(input_str)
    engine.runAndWait()
    return str("User is " + str(c2_output) + " about "+str(c3_output))


predict("I will speak this text")