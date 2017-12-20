from config import basedir
import os

MODELS_PATH = basedir + '/_models'

MODELS_PATH_DICT = {}

def register(name):
    path = MODELS_PATH + os.path.sep + name
    MODELS_PATH_DICT[name] = path

    if not os.path.exists(path):
        os.makedirs(path)

def get_model_path(name):
    return MODELS_PATH_DICT[name]