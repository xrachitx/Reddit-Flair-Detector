import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import svm
import joblib
import pickle

def multinomialNaiveBayes(X_train, X_test, y_train, y_test):
    nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])

    tempNB = nb.fit(X_train, y_train)
    yPred = nb.predict(X_test)
    return yPred

def logisticRegression(X_train, X_test, y_train, y_test):
    logreg = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', LogisticRegression(n_jobs=1, C=1e9)),
                   ])
    tempLR = logreg.fit(X_train, y_train)
    yPred = logreg.predict(X_test)
    return yPred

def randomForest(X_train, X_test, y_train, y_test):
    ranfor = Pipeline([('vect', CountVectorizer()),
                       ('tfidf', TfidfTransformer()),
                       ('clf', RandomForestClassifier(n_estimators = 1000, random_state = 42)),
                      ])
    tempRM = ranfor.fit(X_train, y_train)
    yPred = ranfor.predict(X_test)
    return yPred

def multiLayerPerceptron(X_train, X_test, y_train, y_test):
    mlp= Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      ('clf', MLPClassifier(hidden_layer_sizes=(30,30,30))),
                     ])
    tempMLP = mlp.fit(X_train, y_train)
    yPred = mlp.predict(X_test)
    return yPred

def mySVM(X_train, X_test, y_train, y_test):
    svmNew = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', svm.SVC(kernel='linear', C=1.0)),
                   ])
    SVM = svmNew.fit(X_train, y_train)
    yPred = svmNew.predict(X_test)
    return yPred

flairs =  ["Scheduled","Politics","Photography","Policy/Economy","AskIndia","Sports",
         "Non-Political","Science/Technology","Food","Business/Finance","Coronavirus"]
data = pd.read_csv('../data/cleansedData300.csv')
data["combined"] = data.title.astype("str")+" "+ data.comments.astype("str")
y = data.flair
X = data.combined
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.1,random_state = 5)

accNB = multinomialNaiveBayes(X_train, X_test, y_train, y_test)
print("Multi-Nomial Naive Bayes Accuracy: ",accuracy_score(accNB, y_test))
# print()
# print(classification_report(y_test, accNB,target_names=flairs))

accLR = logisticRegression(X_train, X_test, y_train, y_test)
print("Logistic Regression Accuracy: ",accuracy_score(accLR, y_test))
# print()
# print(classification_report(y_test, accLR,target_names=flairs))

accRF = randomForest(X_train, X_test, y_train, y_test)
print("Random Forest Accuracy: ",accuracy_score(accRF, y_test))
# print()
# print(classification_report(y_test, accRF,target_names=flairs))

accMLP = multiLayerPerceptron(X_train, X_test, y_train, y_test)
print("Multi Layer Perceptron Accuracy: ",accuracy_score(accMLP, y_test))
# print()
# print(classification_report(y_test, accMLP,target_names=flairs))


accSVM = mySVM(X_train, X_test, y_train, y_test)
print("SVM Accuracy: ",accuracy_score(accSVM, y_test))
# print()
# print(classification_report(y_test, accMLP,target_names=flairs))