Подробнее читать здесь: 
    https://habr.com/ru/articles/585034/


Кластеризация — разбиение множества объектов на подмножества, называемые кластерами. 
Кластеризация, будучи математическим алгоритм имеет широкое применение во многих сферах: 
 начиная с таких естественно научных областей как биология и физиология, 
 и заканчивая маркетингом в социальных сетях и поисковой оптимизацией.
    
Приступим к реализации алгоритма:

Исходные данные алгоритма:
n — количество строк;

k — количество кластеров;
dim — размерность точек (пространства).

Выходные данные алгоритма:
    
cluster — двумерный массив размерностью dim * k, содержащий k точек — центры кластеров;

cluster_content — массив, содержащий в себе k массивов — массивов точек принадлежащих соответствующему кластеру.
1

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
2


pip install pymorphy2
3

from tqdm import tqdm
import pymorphy2
import re
tqdm.pandas()


morph = pymorphy2.MorphAnalyzer()


Переменные заданы. Первичные центры кластеров созданы с помощью библиотеки random max_claster_value — 
константа задающая примерные границы исходного множества;
При помощи функции data_ditribution() произведено первичное распределения точек по кластерам. Рассмотрим эту функцию подробнее:

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

Слово good – это лемма для слова better. Стеммер не увидит эту связь, так как здесь нужно сверяться со словарем.
Слово play – это базовая форма слова playing. Тут справятся и стемминг, и лемматизация.
Слово meeting может быть как нормальной формой существительного, так и формой глагола to meet, в зависимости от контекста. 
В отличие от стемминга, лемматизация попробует выбрать правильную лемму, опираясь на контекст.


df['clear_text'] = df['lemmatize_tokens'].progress_apply(lambda x: " ".join(x))
df


2. Токенизация по словам

Токенизация (иногда – сегментация) по словам – это процесс разделения предложений на слова-компоненты. 
В английском и многих других языках, использующих ту или иную версию латинского алфавита, пробел – это неплохой разделитель слов.

Тем не менее, могут возникнуть проблемы, если мы будем использовать только пробел – 
в английском составные существительные пишутся по-разному и иногда через пробел. И тут вновь нам помогают библиотеки.



from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")
my_words = ['Василий', 'Геннадий', 'Виталий']
l=[stemmer.stem(p) for word in df['clear_text'] for p in word.split()]
l


df['stem'] = df['clear_text'].progress_apply(lambda x: " ".join(list(map( lambda y: stemmer.stem(y), x.split()))))
