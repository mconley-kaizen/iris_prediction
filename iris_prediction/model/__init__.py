from os import path
import pickle

MODEL_PATH = path.join(path.dirname(__file__), 'model.pkl')

persistent_model = pickle.load(open(MODEL_PATH, 'rb'))
