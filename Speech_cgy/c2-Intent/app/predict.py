#!/usr/bin/env python
# coding: utf-8
import spacy

def predict(input_str):
    output_dir="/container/models"
    n_iter=15
    model=None
    nlp2 = spacy.load(output_dir)
    texts = [input_str]
    texts = [x.strip() for x in texts]
    docs = nlp2.pipe(texts)
    for doc in docs:
        #print(doc.text)
        for t in doc:
            if t.dep_=='ROOT':
                #print(t.text)
                return str(t.text)
        #print([(t.text, t.dep_, t.head.text) for t in doc if t.dep_ != "-"])
    #print(t.text)
    return "Undetected"



    # Expected output:
    # find a hotel with good wifi
    # [
    #   ('find', 'ROOT', 'find'),
    #   ('hotel', 'PLACE', 'find'),
    #   ('good', 'QUALITY', 'wifi'),
    #   ('wifi', 'ATTRIBUTE', 'hotel')
    # ]
    # find me the cheapest gym near work
    # [
    #   ('find', 'ROOT', 'find'),
    #   ('cheapest', 'QUALITY', 'gym'),
    #   ('gym', 'PLACE', 'find'),
    #   ('near', 'ATTRIBUTE', 'gym'),
    #   ('work', 'LOCATION', 'near')
    # ]
    # show me the best hotel in berlin
    # [
    #   ('show', 'ROOT', 'show'),
    #   ('best', 'QUALITY', 'hotel'),
    #   ('hotel', 'PLACE', 'show'),
    #   ('berlin', 'LOCATION', 'hotel')
    # ]