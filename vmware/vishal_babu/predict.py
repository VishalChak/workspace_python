import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lr_clf_path = "lr_clf.sav"
cv_path = "cv.sav"

lemmatizer = WordNetLemmatizer()

def preprocessing(txt):
    '''
    this fucnction is for preprocessing.
    It take raw text and return clean text
    '''
    txt = re.sub('[^a-zA-Z]', ' ', txt)
    txt = txt.lower()
    txt = txt.split()
    txt = [word for word in txt if word not in stopwords.words('english')]
    txt = [lemmatizer.lemmatize(word) for word in txt]
    txt = ' '.join(txt)
    return txt


def prediction(txt):
    '''
    this function for get prediction
    It load model, load vectorizer call text preprocessing then return results.
    '''
    clf = pickle.load(open(lr_clf_path, 'rb'))
    cv = pickle.load(open(cv_path, 'rb'))
    txt = preprocessing(txt)
    x_text_cv = cv.transform([txt])
    y_pred = clf.predict(x_text_cv)
    return y_pred[0]

if __name__ == "__main__":
    txt = 'Adversaries may modify code signing policies to enable execution of unsigned or self-signed code. Code signing provides a level of authenticity on a program from a developer and a guarantee that the program has not been tampered with. Security controls can include enforcement mechanisms to ensure that only valid, signed code can be run on an operating system.'
    print(prediction(txt))