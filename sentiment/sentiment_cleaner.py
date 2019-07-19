
def cleaner(t):
    symbols = '.:,;!?()[]\'#\"'
    for symbol in symbols:
        t = t.replace(symbol, '')

    t = t.replace('  ', ' ')

    print('cleaning', t)

    # return t.lower().split()
    return t.lower()