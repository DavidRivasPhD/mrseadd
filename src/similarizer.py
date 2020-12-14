
def similarizing(query, sentences, nlp):
    """
    Given a original_query and clean_sentences, the function scores the similarity between them
    """
    doc_query = nlp(query)
    similarity_scores = {}
    for i in range(0, len(sentences)):
        doc_sentence_i = nlp(sentences[i])
        similarity_i = doc_query.similarity(doc_sentence_i)
        similarity_scores[i] = similarity_i
    return similarity_scores
