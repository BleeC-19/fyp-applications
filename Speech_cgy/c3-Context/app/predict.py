import cytoolz
import numpy
#from train import SentimentAnalyser
from keras.models import Sequential, model_from_json
from keras.layers import LSTM, Dense, Embedding, Bidirectional
from keras.layers import TimeDistributed
from keras.optimizers import Adam
import spacy
from sentimentanalyzer.sentimentanalyzer import Sentiment




def predict(input_str):
    #model_dir = pathlib.Path("/container/Model")
    #nlp = spacy.load("en_vectors_web_lg")
    #nlp.add_pipe(nlp.create_pipe("sentencizer"))
    max_length=100
    #nlp.add_pipe(SentimentAnalyser.load(model_dir, nlp, max_length=max_length))
    obj = Sentiment(text=input_str)
    data = obj.get
    texts = [input_str]
    correct = 0
    i = 0
    if data['Positive']>data['Negative']:
        return ("User is happy")
    return "User is Unhappy"


predict("I am happy")