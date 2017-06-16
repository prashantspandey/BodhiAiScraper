import nltk
from sklearn.neural_network import MLPClassifier
from nltk.stem import WordNetLemmatizer
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import pickle


def find_tags(article):
    tokenizer = RegexpTokenizer(r'\w+')
    # punctuation_list = [',','.','-',':',';']
    stop = set(list(stopwords.words('english')))
    text = tokenizer.tokenize(article)
    stop_list = []
    for i in text:
        if i.lower() not in stop:
            stop_list.append(i)
    tagged = nltk.pos_tag(stop_list)
    tagged = np.array(tagged)
    noun_list = []
    n = tagged[:, 1] == 'NNP'
    for k, i in enumerate(n):
        if i == True:
            noun_list.append(tagged[k, 0])

    c_list = Counter(noun_list)
    c_list = c_list.most_common(len(c_list))
    c_list = np.array(c_list)
    tags = c_list[:, 0]
    final_list = []
    for tag in tags:
        if len(tag) <= 2:
            pass
        else:
            final_list.append(tag)
    print(final_list)
    return final_list[:5]


def sample_to_features(li):
    stop_words = []
    with open('/home/prashant/Desktop/programming/projects/scrapewebsite/scrapewebsite/scrapersite/home/features3.pkl',
              'rb') as le:
        lexicon = pickle.load(le)
    lemmetizer = WordNetLemmatizer()
    reg1 = re.compile('\:', re.DOTALL)
    reg2 = re.compile('\,', re.DOTALL)
    reg3 = re.compile("\'", re.DOTALL)
    reg4 = re.compile('\[', re.DOTALL)
    reg5 = re.compile('\]', re.DOTALL)
    stop = set(list(stopwords.words('english')))

    first = li
    first = ''.join(first)

    second = [i for i in first.split()]
    second = str(second)

    second = reg1.sub(' ', second)
    second = reg2.sub(' ', second)
    second = reg3.sub(' ', second)
    second = reg4.sub(' ', second)
    second = reg5.sub(' ', second)

    second = ''.join(second)
    second = [i for i in second.split()]
    third = []
    for i in second:
        third.append(i.lower())

    for i in third:
        if i not in stop:
            stop_words.append(i)
    stop_words = [lemmetizer.lemmatize(i) for i in stop_words]
    fet = np.zeros(len(lexicon))
    for word in stop_words:
        if word in lexicon:
            index_value = lexicon.index(word)
            fet[index_value] += 1
    features = list(fet)
    print('Length of features: %s' % len(features))
    return features


def predict_category(features):
    with open(
            '/home/prashant/Desktop/programming/projects/scrapewebsite/scrapewebsite/scrapersite/home/SportsWorldIndiaMoviesScience-TechClassifier(neural_network).pkl',
            'rb') as cl:
        clf = pickle.load(cl)

        pred = clf.predict(features)
        print('Prediction: %s' % str(pred))
        return pred
