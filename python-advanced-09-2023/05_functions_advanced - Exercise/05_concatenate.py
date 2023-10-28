def concatenate(*args, **kwargs):
    sentence = ''
    for word in args:
        sentence += word
    for k, v in kwargs.items():
        if k in sentence:
            sentence = sentence.replace(k, v) # не се сетих как се замества нещо в стринг с replace
    return sentence