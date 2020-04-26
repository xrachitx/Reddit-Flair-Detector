from flask import Flask, redirect, url_for, request,flash,render_template
import praw
import pickle
import re
import lxml
import nltk
import pandas as pd
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import json

reddit=praw.Reddit(client_id='',client_secret='', user_agent='',  username='',password='')

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

def predict(post):
    title= str(post.title)
    url = str(post.url)
    author=str(post.author)
    cnt = 0
    post.comments.replace_more(limit=0)
    comments = ""
    authors = ""
    for j in post.comments:
        if (cnt>30):
            break
        comments += str(j.body) + " "
        authors += str(j.author) + " "
        cnt+=1
    comments = comments[:-1]
    authors = authors[:-1]
    finalData = title + " " +comments
    finalData = cleanData(finalData)
    post = {"data":finalData,"url":url,"author":author,"authors":authors}
    finalData = pd.DataFrame([post])
    finalData["final"] = finalData.data.astype("str")+" "+ finalData.url.astype("str")+" "+ finalData.author.astype("str")+" "+finalData.authors.astype("str")
    loaded_model=pickle.load(open("data/finalModel.sav",'rb'))
    predicted_flair=loaded_model.predict(finalData["final"])    
    return predicted_flair

app = Flask(__name__)
app.secret_key = "hello"
@app.route("/",methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        userLink=request.form["nm"]
        splitLink = userLink.split("/")
        try:
            post=reddit.submission(url=userLink)
            if splitLink[4] != "india":
                flash("Please post only r/india reddit urls")
                return render_template('index.html')
        except praw.exceptions.ClientException:
            flash("Please post a valid URL")
            return render_template('index.html')
        predicted_flair=predict(post)
        print(str(predicted_flair))
        flash("Flair Detected: " +str(predicted_flair)[2:-2])
        return render_template('index.html')
    flash("Flair Detected:")
    return render_template('index.html')

@app.route("/automated_testing",methods = ['POST'])
def testing():
    if request.method == "POST":
        fileGiven= request.files["upload_file"]
        urls = fileGiven.read().decode("utf-8").split("\n")
        ans = {}
        for userLink in urls:
            post=reddit.submission(url=userLink)
            predicted_flair=str(predict(post))
            print(predicted_flair[2:-2])
            ans[userLink] = predicted_flair[2:-2]
        return json.dumps(ans)
        

    # pass

if __name__ == '__main__':
   app.run(debug=True)
