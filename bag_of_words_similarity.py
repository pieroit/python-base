import json
from bag_of_words import bag_of_words

def similarity(s1, s2, sw=[]):
    bow1 = bag_of_words(s1, sw=stopwords)
    bow2 = bag_of_words(s2, sw=stopwords)

    bow1 = set(bow1)
    bow2 = set(bow2)

    bow_intersection = bow1.intersection(bow2)
    bow_union = bow1.union(bow2)
    simil = len(bow_intersection) / len(bow_union)
    return simil

if __name__ == '__main__':
    sentence1 = 'I like the python language'
    sentence2 = 'A python bit me'

    with open('stopwords-all.json', 'rb') as f:
        stopwords = json.load(f)
        stopwords = stopwords['en']

    #stopwords = ['i', 'me', 'a', 'the']
    sim = similarity(sentence1, sentence2, sw=stopwords)
    print(sim)



