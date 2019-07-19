
import json

# with takes care of acquisition/release of resources
with open('stopwords-iso.json', 'rb') as f:
    sw = json.load(f)
print(sw)




