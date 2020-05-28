import speech_recognition as sr
from pocketsphinx import pocketsphinx, Jsgf, FsgModel
import os

from datetime import datetime

language_directory = "/container/models/wsj1"
config = pocketsphinx.Decoder.default_config()
config.set_string("-hmm", os.path.join(language_directory, "acoustic-model"))
config.set_string("-lm", os.path.join(language_directory, "language-model.lm.bin"))
config.set_string("-dict", os.path.join(language_directory, "pronounciation-dictionary.dict"))
config.set_string("-logfn", os.devnull)
config.set_int("-topn", 1)
config.set_int("-ds", 4)
config.set_int("-pl_window", 10)
config.set_int("-maxhmmpf", 1000)
config.set_int("-maxwpf", 5)
decoder = pocketsphinx.Decoder(config)




def predict(audio_file_index):
    t1 = datetime.utcnow()
    print("\n[INFO]\t", "[c1]\t", str(t1))

    audio_file_index = int(audio_file_index)
    audio_file_path = "/container/data/wav/" + str(audio_file_index) + " .wav"

    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_file_path)
    with audio_file as source:
        audio = recognizer.record(source)

    raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
    decoder.start_utt()  # begin utterance processing
    decoder.process_raw(raw_data, False, True)
    decoder.end_utt()  # stop utterance processing
    hypothesis = decoder.hyp()
    recognized_string = hypothesis.hypstr

    t2 = datetime.utcnow()
    print("[INFO]\t", "[c1]\t", str(t2))
    print("[INFO]\t", "[c1]\tTime elapsed: ", (t2-t1).total_seconds(), " seconds." )

    print(recognized_string)
        
    return recognized_string


if __name__ == "__main__":
    predict("53")
