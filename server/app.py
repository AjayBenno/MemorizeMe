#!/usr/bin/env python
from flask import Flask,render_template,request
from firebase import firebase
import random

firebase = firebase.FirebaseApplication('https://memorize-me-ab784.firebaseio.com/')
wordfile = open('words.txt')
words=[]
app = Flask(__name__)
def generateWords():
    for word in wordfile:
        words.append(word)
def getRandomWord():
    return random.choice(words)

    
def getResultfromFirebase(text):
    word = getRandomWord()


@app.route('/')
def hello_world():
    return render_template('index.html',name="a")

@app.route('/storeTextandGetName', methods=['POST'])
def test():
    text = request.form.get('textarea1','a')
    key = getResultfromFirebase(text)
    return text


if __name__ == '__main__':
    generateWords()
    app.run(debug=True)
