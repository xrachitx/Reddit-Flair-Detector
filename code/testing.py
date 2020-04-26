import re
import lxml
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def decodeHTML(data):
    data = BeautifulSoup(data,"lxml").text
    return data
def normaliseTextToLower(data):
    return data.lower()
def tokenizeAndPunctuationRemoval(data):
    tokenizedList=[]
    for token in RegexpTokenizer('\w+').tokenize(data):
        tokenizedList.append(token)
    return tokenizedList
def removeNumbers(dataList):
    dataListRefined = []
    for token in dataList:
        if not (token.isnumeric()):
            dataListRefined.append(token)
    print("HELO")
    return dataListRefined
def removeStopWords(dataList):
    dataList = list(set(dataList))
    stopWords = set(stopwords.words("english"))
    nonStoppedWords = list(token for token in dataList if token not in stopWords)
    convertToText = " ".join(nonStoppedWords)
    return convertToText


text ='sample = """<h1>Title Goes Here</h1><b>Bolded Text</b><i>Italicized Text</i><img src="this should all be gone"/><a href="this will be gone, too">But this will still be here!</a>I run. He ran. She is running. Will they stop running?I talked. She was talking. They talked to them about running. Who ran to the talking runner?[Some text we don\'t want to keep is in here]¡Sebastián, Nicolás, Alejandro and Jéronimo are going to the store tomorrow morning!something... is! wrong() with.,; this :: sentence.I can\'t do this anymore. I didn\'t know them. Why couldn\'t you have dinner at the restaurant?My favorite movie franchises, in order: Indiana Jones; Marvel Cinematic Universe; Star Wars; Back to the Future; Harry Potter.Don\'t do it.... Just don\'t. Billy! I know what you\'re doing. This is a great little house you\'ve got here.[This is some other unwanted text]John: "Well, well, well."James: "There, there. There, there."&nbsp;&nbsp;There are a lot of reasons not to do this. There are 101 reasons not to do it. 1000000 reasons, actually.I have to go get 2 tutus from 2 different stores, too.22    45   1067   445{{Here is some stuff inside of double curly braces.}}{Here is more stuff in single curly braces.}[DELETE]</body></html>"""'

print(removeStopWords(removeNumbers(tokenizeAndPunctuationRemoval(normaliseTextToLower(decodeHTML(text))))))