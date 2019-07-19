import glob
import os
import pandas as pd

#for root, files, dirs in os.walk('movie-review'):
#    print('Searching folder', root)
#    print('founf files', files)
#    print('found dirs', dirs)
#    print('\n')

parent_folder = 'movie-review/movie_reviews'
folder_names = ['pos', 'neg']
regex = '*.txt'

corpus = []
for folder in folder_names:
    path = os.path.join(parent_folder, folder, regex)
    files = glob.glob(path)
    print('Folder', path)
    print(files)
    for file in files:
        with open(file, 'r') as f:
            document = {
                'text': f.read(),
                'sentiment': folder
            }
        corpus.append(document)

df = pd.DataFrame(corpus)
df.to_csv('_tmp.csv')
