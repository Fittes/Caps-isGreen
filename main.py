import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords



pip install pymorphy2


from tqdm import tqdm
import pymorphy2
import re
tqdm.pandas()


morph = pymorphy2.MorphAnalyzer()


def lemmatize(words:list):
    text = []
    for word in words:
        morph_word = morph.parse(word)[0]
        if morph_word.tag.POS in ['NOUN', 'ADJF'] and morph_word[2] not in stopwords.words('russian'):
            text.append(morph_word[2])
    return text


def clear_text(text):
    clear_text = re.sub(r'[^А-Яа-я ]', '', str(text))
    tokens = clear_text.split()
    tokens = list(filter(lambda x: len(x) > 3, tokens))
    lemmatize_tokens = lemmatize(tokens)
    return lemmatize_tokens


def post_words_count(text):
    return len(text)

df['lemmatize_tokens'] = df['Тема'].progress_apply(lambda x: clear_text(x))

df['word_count'] = df['lemmatize_tokens'].progress_apply(lambda x: post_words_count(x))


df['clear_text'] = df['lemmatize_tokens'].progress_apply(lambda x: " ".join(x))
df



from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")
my_words = ['Василий', 'Геннадий', 'Виталий']
l=[stemmer.stem(p) for word in df['clear_text'] for p in word.split()]
l


df['stem'] = df['clear_text'].progress_apply(lambda x: " ".join(list(map( lambda y: stemmer.stem(y), x.split()))))