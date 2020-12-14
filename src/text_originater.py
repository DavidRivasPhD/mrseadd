
from Bio import Entrez
from Bio import Medline

def text_originating(query):
    """
    Given a query, the function returns the text of the top 10 PubMed search results
    """
    Entrez.email = "davidrivas@blockchainguru.ca"
    handle = Entrez.esearch(db="pubmed", retmax=10, term=query, usehistory='y', sort='relevance')
    record = Entrez.read(handle)
    query_key = record["QueryKey"]
    webenv = record["WebEnv"]
    handle = Entrez.efetch(db="pubmed", webenv=webenv, query_key=query_key, retmax=10, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    search_results_text = " "
    for record in records:
        deltatext = record.get("TI", "?") + record.get("AB", "?")
        search_results_text = search_results_text + deltatext + "\n"
    handle.close()
    return search_results_text
