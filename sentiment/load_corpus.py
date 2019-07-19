
import os
import glob
import pandas as pd

def get_document_from_file(file_path_url_yeah):

    # estrai il nome della cartella che contiene il file
    separator = os.sep
    category = file_path_url_yeah.split(separator)
    category = category[-2]

    # estrai testo dal file
    with open(file_path_url_yeah, 'r') as f:
        text = f.read()

    # restituisci dizionario
    return {
        'text': text,
        'category': category
    }


parent_folder = 'movie-review\\movie_reviews'
corpus = []

for root, dirs, files in os.walk(parent_folder):
    expression = os.path.join(root, '*.txt')
    txt_files = glob.glob(expression)

    for txt_file in txt_files:
        document = get_document_from_file(txt_file)
        corpus.append(document)

corpus = pd.DataFrame(corpus)
corpus.to_csv('sentiment.csv', sep=';', index=False)

