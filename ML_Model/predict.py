# Importing libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import pickle


def prediction(key_word):
    # load Ml model
    kmeans = pickle.load(open("ML_model/models/model.h5", "rb"))

    transformer = TfidfTransformer()
    # load tfidf model
    loaded_vec = CountVectorizer(
        decode_error="replace", vocabulary=pickle.load(open("ML_model/models/vocabulary.h5", "rb")))

    input_word = transformer.fit_transform(
        loaded_vec.fit_transform(np.array([key_word])))
    prediction = kmeans.predict(input_word)
    return prediction
