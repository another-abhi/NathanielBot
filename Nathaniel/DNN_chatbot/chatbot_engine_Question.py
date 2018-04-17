#--------------------------NATHANIEL ENGINE--------------------------------
import sys
sys.path.append('../')
import chatbot_config_Question as cfg
import pickle
# unpacking the training data
data = pickle.load( open( "../DNN_chatbot/training_data_question", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']
# unpacking the dataset
import json
with open("../DNN_chatbot/"+cfg.dataset) as json_data:
    intents = json.load(json_data)

import tensorflow as tf
import tflearn
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
#net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)
# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.load('../DNN_chatbot/Question_model.tflearn')

import nltk
#from nltk.stem.lancaster import LancasterStemmer
#stemmer = LancasterStemmer()
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
#converting input to numeric form
import numpy as np
import random

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each
# word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

#response generator
context={}
ERROR_THRESHOLD = cfg.error
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words, True)])[0]
    print (results)
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    print (results)
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    print(return_list)
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']
                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        s=(random.choice(i['responses']))
                        if (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                            context[userID] = ""
                        print (s)
                        return s
            results.pop(0)
    return "Sorry, I was unable to identify the class of that question"

while(1):
     #inp=raw_input("type your message here>>")
     inp=input("type your message here>>")
     print("type your message here>>",inp,"\n***********************************\nReply>>",response(inp,show_details=True))
     if inp=="stop":
         exit()