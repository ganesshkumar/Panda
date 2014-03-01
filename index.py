import os, sys, time
from flask import Flask, render_template, url_for, request, jsonify

sys.path.append('libs')
from Panda import Panda
from MongoDBClient import MongoDBClient

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("test.html", request=request)

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_term = request.args.get('search', '', type=str)
    item = Panda.db_client.get(search_term)
    if item is None:
        return jsonify(result="ITEM_NOT_FOUND")
    else:
        panda = Panda()
        print search_term
        return jsonify(
            title=item['title'],
            amzn_senti=item['amzn_senti'],
            flip_senti=item['flip_senti'],
            amzn_rating=item['amzn_rating'],
            flip_rating=item['flip_rating'],
            twitter_senti=item['twitter_senti'],
        )

