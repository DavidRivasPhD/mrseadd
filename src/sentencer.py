
def sentencing(any_text, nlp):
    """
    Given any text, the function slices the text into its sentences.
    """
    nlp.add_pipe(nlp.create_pipe('sentencizer'))
    doc = nlp(any_text)
    sentences = [sent.string.strip() for sent in doc.sents]
    return sentences
