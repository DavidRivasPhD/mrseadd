
import spacy
nlp = spacy.load('enmd')
# nlp = spacy.load('enmd', disable=["tagger", "parser", "ner"])

def independent_sentencing(any_text):
    """
    Given any text, the function slices the text into its sentences with an independent nlp pipeline.
    """
    nlp.add_pipe(nlp.create_pipe('sentencizer'))
    doc = nlp(any_text)
    sentences = [sent.string.strip() for sent in doc.sents]
    return sentences
