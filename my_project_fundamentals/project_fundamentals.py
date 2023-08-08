import stanza

stanza.download('bg')

nlp = stanza.Pipeline(lang='bg', processors='tokenize, pos, lemma, ner')

text = input('\nВъведете дума/изречение: ')
doc = nlp(text)

pos_mapping = {
    'ADJ': 'Прилагателно',
    'ADP': 'Предлог',
    'ADV': 'Наречие',
    'AUX': 'Помощен глагол',
    'CCONJ': 'Съюз',
    'DET': 'Определителен член',
    'INTJ': 'Междуметие',
    'NOUN': 'Съществително',
    'NUM': 'Числително',
    'PART': 'Частица',
    'PRON': 'Местоимение',
    'PROPN': 'Собствено име',
    'PUNCT': 'Пунктуация',
    'SCONJ': 'Съюз',
    'SYM': 'Символ',
    'VERB': 'Глагол',
    'X': 'Друго'
}


def translate_gender(gender):
    if gender == 'Masc':
        return 'м.р.'
    elif gender == 'Fem':
        return 'ж.р.'
    elif gender == 'Neut':
        return 'ср.р.'
    return '-'


def translate_number(number):
    if number == 'Sing':
        return 'ед.ч.'
    elif number == 'Plur':
        return 'мн.ч.'
    return ''


def translate_tense(verb_feats):
    tense = ''
    gender = ''
    number = ''
    for feat in verb_feats.split('|'):
        if feat.startswith('Tense'):
            tense = feat.split('=')[1]
        elif feat.startswith('Gender'):
            gender = feat.split('=')[1]
        elif feat.startswith('Number'):
            number = feat.split('=')[1]

    tense_str = ''
    if tense == 'Pres':
        tense_str = 'сег. време'
    elif tense == 'Past':
        tense_str = 'минало време'
    elif tense == 'Fut':
        tense_str = 'бъдеще време'

    return f"в {tense_str} ({translate_gender(gender)}, {translate_number(number)})"


def determine_person(verb_feats):
    person = ''
    for feat in verb_feats.split('|'):
        if feat.startswith('Person'):
            person = feat.split('=')[1]
    if person == '1':
        return 'първо лице'
    elif person == '2':
        return 'второ лице'
    elif person == '3':
        return 'трето лице'
    return ''


word_counter = 1

for sentence in doc.sentences:
    for word in sentence.words:
        # Проверка дали думата е позната в Stanza
        if word.lemma is None:
            print(f"{word_counter}. {word.text} - Непозната дума")
            word_counter += 1
            continue

        pos_tag = word.upos
        translated_pos = pos_mapping.get(pos_tag, pos_tag)

        if pos_tag in ['NOUN', 'ADJ']:
            features = word.feats.split('|')
            gender = ''
            number = ''
            for feature in features:
                if feature.startswith('Gender'):
                    gender = feature.split('=')[1]
                elif feature.startswith('Number'):
                    number = feature.split('=')[1]
            translated_pos += f" ({translate_gender(gender)}, {translate_number(number)})"

        elif pos_tag == 'VERB':
            translated_pos += f" {translate_tense(word.feats)} {determine_person(word.feats)}"

        print(f"{word_counter}. {word.text} ({word.lemma}) POS: {translated_pos}")
        word_counter += 1
