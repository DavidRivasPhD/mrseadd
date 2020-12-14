
def summarizing(sentences, similarity_scores, n_summary_sentences):
    """
    Given similarity scores of clean_sentences with original_query, the function extracts the clean_sentences with the top n scores as the summary.
    """
    sorted_sentences = {}
    j = -1
    orders = similarity_scores
    sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        j += 1
        sorted_sentences[j] = i[0]

    summary = ''
    for k in range(0, n_summary_sentences):
        summary = summary + '\n' + sentences[sorted_sentences.get(k)]

    return summary
