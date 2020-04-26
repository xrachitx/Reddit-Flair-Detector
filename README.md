# Reddit-Flair-Detector
A web app which detects the flair of a reddit r/india post.

## Local Deployment
1. Clone the git repository.
2. Create a virtual environment (inside the cloned folder):
```bash
virtualenv -p /usr/bin/python3 virtualenvironment/
```
3. Activate virtual environment:
```bash
source virtualenvironment/bin/activate
```
4. Install dependencies in requirements.txt:
```bash
pip3 install -r requirements.txt
```
5. Start the application:
```bash
python3 app.py
```
6. Go to your local host server mentioned in the terminal and use the flair detector!

## Tasks

### 1. Extracting Data
Data was extracted using code/extractData.ipynb jupyter notebook. PRAW API was used to extract data and MongoDB was used to store the extracted data. 11 flairs were taken which were: Scheduled, Politics, Photography, Policy/Economy, AskIndia, Sports, Non-Political, Science/Technology, Food, Business/Finance, Coronavirus.At first I extracted 100 posts per flair and 10 comments per post. But after that to increase the accuracy of my machine learning model I extracted 250 posts per flair and 30 posts per flair. Increasing the number of posts and comments gave a bump to the accuracy of my model by almost 5%!

### 2. Exploratory Data Analysis
Data was explored using code/dataVisualisation.ipynb and code/dataVisualisationCleaned.ipynb. In the code/dataVisualisation.ipynb jupyter notebook I explored the top 10 most common words for each flair and it became very evident that the data contains a lot of stopwords which needed removal. Therefore I cleaned the data, by removing any html syntax, normalising by lowering text, removing punctuation, removing numbers and finally removing stop words, before doing any further analysis of the text data.
Thus in the code/dataVisualisationCleaned.ipynb I performed name-entity analysis and explored the top 10 words for each flair for cleaned data. The combination of the 2 gave excellent complimentary results! For example: named entity analysis for scheduled showed that Time is the most common entity being talked about in a scheduled post which was complemented by the fact that words like daily, night etc were some of the most used words in a scheduled post. Also Political posts in r/India showed that the most common words used were "Modi" and "India" which was again complemented by the name-entity analysis which showed that GPE (countries, cities, etc) and Persons were the most common entity.

### 3. Training and Testing Models 
5 different algorithms namely: Multinomial Naive Bayes, Logistic Regression, Random Forest, Multilayer Perceptron and SVM were used. The given machine learning algorithms were tested on many different combinations of data but Title+URL+Comments+Authors+CommentAuthors gave the best accuracy of **66.66% with Multinomial Naive Bayes**. The other different combinations are mentioned below:
#### Title+URL+Comments+Authors+CommentAuthors
**Algorithm** | **Accuracy**
------------ | -------------
Multinomial Naive Bayes | **66.66**
Logistic Regression | 63.67
Random Forest | 56.55
Multilayer Perceptron | 52.05
SVM | 63.67

#### Some other Combinations with their best accuracy
Combination | Algorithm | Accuracy
------------ | -------------|----------
Title+Body|Multinomial Naive Bayes|60.67
Title+Comments|Multinomial Naive Bayes|60.67
Title+Comments+Body|Multinomial Naive Bayes|60.06
Title+Comments+Body+URL|Multinomial Naive Bayes and SVM|61.04
Title+Comments+Body+URL+Author |Logistic Regression|62.54

### 4. Web App
Web App created using Flask+HTML+CSS with /automated_testing route used for automated post requests.

### 5. Heroku App
Heroku App Deployed on: https://redditflairdetect-14.herokuapp.com/

## File Structure
```bash
├── app.py
├── code
│   ├── cleanText.ipynb
│   ├── dataVisualisationCleaned.ipynb
│   ├── dataVisualisation.ipynb
│   ├── extractData.ipynb
│   ├── machineLearning.ipynb
│   ├── __pycache__
│   │   └── redditTest.cpython-36.pyc
│   ├── redditTest.py
│   └── testing.py
├── data
│   ├── cleansedData300.csv
│   ├── cleansedData.csv
│   └── finalModel.sav
├── LICENSE
├── nltk.txt
├── Procfile
├── README.md
├── requirements.txt
├── static
│   └── assets
│       ├── fonts
│       │   ├── Montserrat-BlackItalic.ttf
│       │   ├── Montserrat-Black.ttf
│       │   ├── Montserrat-BoldItalic.ttf
│       │   ├── Montserrat-Bold.ttf
│       │   ├── Montserrat-ExtraBoldItalic.ttf
│       │   ├── Montserrat-ExtraBold.ttf
│       │   ├── Montserrat-ExtraLightItalic.ttf
│       │   ├── Montserrat-ExtraLight.ttf
│       │   ├── Montserrat-Italic.ttf
│       │   ├── Montserrat-LightItalic.ttf
│       │   ├── Montserrat-Light.ttf
│       │   ├── Montserrat-MediumItalic.ttf
│       │   ├── Montserrat-Medium.ttf
│       │   ├── Montserrat-Regular.ttf
│       │   ├── Montserrat-SemiBoldItalic.ttf
│       │   ├── Montserrat-SemiBold.ttf
│       │   ├── Montserrat-ThinItalic.ttf
│       │   └── Montserrat-Thin.ttf
│       └── images
│           └── cool-background.png
└── templates
    └── index.html

8 directories, 37 files

```

## Resources

1. https://towardsdatascience.com/exploratory-data-analysis-for-natural-language-processing-ff0046ab3571
2. https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15
3. https://programminghistorian.org/en/lessons/sentiment-analysis
4. https://praw.readthedocs.io/en/latest/
5. https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
6. https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908
7. https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
8. https://medium.com/greyatom/an-introduction-to-bag-of-words-in-nlp-ac967d43b428
9. https://spacy.io/api/annotation
