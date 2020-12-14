

from spacy.lang.en.stop_words import STOP_WORDS


def add_sw(new_sw):
    STOP_WORDS.add(new_sw)
    return
