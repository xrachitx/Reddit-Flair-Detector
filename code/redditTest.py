import praw
from pymongo import MongoClient
import pickle
import re
import lxml
import nltk
import pandas as pd
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import redditTest
reddit=praw.Reddit(client_id='Qq1MxtQ9YVNXgA',client_secret='hg00d83IEYWEAAT0RdFzm50zm5E', user_agent='testing',  username='mic_testing123',password='Cookies')

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
    # print("HELO")
    return dataListRefined

def removeStopWords(dataList):
    dataList = list(set(dataList))
    stopWords = set(stopwords.words("english"))
    nonStoppedWords = list(token for token in dataList if token not in stopWords)
    convertToText = " ".join(nonStoppedWords)
    return convertToText

def cleanData(data):
    return (removeStopWords(removeNumbers(tokenizeAndPunctuationRemoval(normaliseTextToLower(decodeHTML(data))))))
