
import os

#root = os.getcwd()
#subfolder = 'movie-review'
#print( os.path.join(root, subfolder) )

all_txt = []
for root, dirs, files in os.walk('movie-review'):
    print('Listing folder', root)
    print('\tFound files', files)
    print('\tFound folders', dirs)
    print('===========')

    for f in files:
        if '.txt' in f:
            all_txt.append(f)

print(len(all_txt), all_txt)
