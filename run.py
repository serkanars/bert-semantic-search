from flask import Flask, request
from flask_cors import CORS, cross_origin
from SemanticSearchBert import *

app = Flask(__name__)
file = open('./titles.txt')
sentences = file.readlines()

@app.route("/test/",methods=['GET', 'POST'])
def test_se():
    if request.method == 'POST':
        response = request.get_json()
        value = response['search']
        probably, sen = get_scores(value, sentences)
        #result = {"smilarity  sentences" : sen, "probably" : probably}


        return {"smilarity  sentences" : sen, "probably" : probably}

    
if __name__ == "__main__":
    app.run(debug=True, port = 5000)
 