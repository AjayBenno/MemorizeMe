#!/usr/bin/env python
from flask import Flask,render_template,request
from firebase import firebase
import random,json

firebase = firebase.FirebaseApplication('https://memorize-me-ab784.firebaseio.com/',)
wordfile = open('words.txt')
words=[]
app = Flask(__name__)
def generateWords():
    for word in wordfile:
        words.append(word)
def getRandomWord():
    return random.choice(words)

    
def getResultfromFirebase(text):
    currentUsedWords = firebase.get('/text',None)
    if(currentUsedWords != None and len(currentUsedWords) ==850):
        firebase.delete('/text')
    word = getRandomWord()
    while(currentUsedWords != None and word in currentUsedWords):
        word = getRandomWord()
    data = {word:text}
    sent = json.dumps(data)
    firebase.post('/text',sent)
    return word



@app.route('/')
def hello_world():
    return render_template('index.html',name="a")

@app.route('/storeTextandGetName', methods=['POST'])
def test():
    text = request.form.get('textarea1','a')
    key = getResultfromFirebase(text)
    return key


if __name__ == '__main__':
    generateWords()
    app.run(debug=True)
