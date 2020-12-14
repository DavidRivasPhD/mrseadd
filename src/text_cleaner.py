
def text_cleaning(any_text, nlp):
    """
    The function filters out stop words from any text and returns tokenized and lemmatized words
    """
    doc = nlp(any_text.lower())
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        # if token.is_punct:
        #     continue
        result.append(token.lemma_)
    clean_text = " ".join(result)
    return clean_text
