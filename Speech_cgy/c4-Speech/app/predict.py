import pyttsx3


def predict(input_str):
    #c1_output, c2_output = str(input_str).split("|")
    engine = pyttsx3.init()
    engine.say(input_str)
    #engine.runAndWait()
    return str("Read Finished")


predict("I will speak this text")