"""
Main sequence to extract the clean_sentences of an original_text that are most similar to a clean_original_query
"""

# IMPORTS AND MODEL LOADING
from text_originater import text_originating
from sw_lister import sw_listing
from sw_adder import add_sw
from text_cleaner import text_cleaning
from independent_sentencer import independent_sentencing
from sentencer import sentencing
from similarizer import similarizing
from summarizer import summarizing
import spacy
import time
start = time.time()
nlp = spacy.load('enmd')
# nlp = spacy.load('enmd', disable=["tagger", "parser", "ner"])

# SIMPLE TESTING INPUTS (IT'S EITHER THIS INPUT SECTION OR THE NEXT ONE THAT NEEDS TO BE COMMENTED OUT)
original_query = 'diabetes symptoms'
original_text = 'Hello, fever! Here are two more mathematical expressions? This is a third violet bird. this is the last medicine?. Sugar; inflamation.'

# INPUTS
# query = "diabetes symptoms"
# search_results_text = text_originating(query)
# print('search_results_text =', search_results_text)
# original_query = query
# original_text = search_results_text

# CLEANING
clean_original_query = text_cleaning(original_query, nlp)
clean_original_text = text_cleaning(original_text, nlp)

# INTERMEDIATE PRINTING
print('original_query =', original_query)
print('original_text =', original_text)
print('clean_original_query =', clean_original_query)
print('clean_original_text =', clean_original_text)

# SENTENCES SIMILARITIES
original_sentences = independent_sentencing(original_text)
clean_sentences = sentencing(clean_original_text, nlp)

similarity_scores = similarizing(clean_original_query, clean_sentences, nlp)
n_summary_sentences = 3
summary = summarizing(original_sentences, similarity_scores, n_summary_sentences)

# INTERMEDIATE PRINTING
print('original_sentences =', original_sentences)
print('clean_sentences =', clean_sentences)
print('total_n_sentences =', len(clean_sentences))
# print('joining the original_sentences =', ' '.join(original_sentences))
# print('joining the clean_sentences =', ' '.join(clean_sentences))
print('similarity_scores =', similarity_scores)
print('')
print('number of sentences in the summary = ', n_summary_sentences)
print('summary =', summary)
print(" ")

# TOKENS AND VECTORS
sw_list = sw_listing(nlp)
# add_sw('lol')
print(sw_list)
end = time.time()
print('run time =', end - start, 'seconds')
