
def bag_of_words(s, sw=[]):
    clean = s.lower()
    symbols = '!?()[]\',;.:\"-_'
    for symbol in symbols:
        clean = clean.replace(symbol, '')

    tokens = clean.split(' ')

    for stopword in sw:
        if stopword in tokens:
            tokens.remove(stopword)

    return tokens

if __name__ == '__main__':
    sentence = 'Ciao mi piace il gelato (al cioccolato)!'
    bow = bag_of_words(sentence, sw=['il', 'la', 'mi', 'al'])
    print(bow)