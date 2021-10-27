from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


model = SentenceTransformer('all-mpnet-base-v2')

def QueryEmbed(input):
    """
    It encodes the inputs using the encode structure of the specified model.
    -------------

    Parameter: Search query.

    Return: Returns the given sentence as an encoded array of the length of the specified pattern.
    
    """
    
    return model.encode(input)

def get_scores(input_query, input_corpus, count=15):
    """
    Searching by similarity returns the similarity between the text
    and the document to be searched using cosine similarity.
    --------------

    Parameters: Search query, document and how many sentences are desired as output.

    Return: Similarity probability and sentences of the determined number of sentences 
    close to the entered sentence according to cosine similarity.
    
    """

    embedding_corpus = np.array(QueryEmbed(input_corpus))
    embedding_query = np.array(QueryEmbed([input_query]))
    results = cosine_similarity(embedding_query, embedding_corpus)[0]
    count = results.argsort()[-count:][::-1]
    scores = results[count]
    sentences = [input_corpus[idx] for idx in count]
    return [str(s) for s in scores], sentences


## Example
"""data = pd.read_excel(your_data)

SearchQuery = 'kredi kartını nasıl alabilirim'

probably, sen = get_scores(SearchQuery, data)

print(probably, sen)"""