import os, sys, time, datetime
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
        test = panda.process(item)
        dates = []
        pos = []
        neg = []
        neu = []
        date_rating = item['date_rating']
        for key in sorted(date_rating.iterkeys()):
            dates.append(datetime.datetime.fromtimestamp(int(key)).strftime('%d-%m-%Y'))
            pos.append(date_rating[key]['positive'])
            neg.append(date_rating[key]['negative'])
            neu.append(date_rating[key]['neutral'])

        return jsonify(
            title=item['title'],
            amzn_senti=item['amzn_senti'],
            flip_senti=item['flip_senti'],
            amzn_rating=item['amzn_rating'],
            flip_rating=item['flip_rating'],
            twitter_senti=item['twitter_senti'],
            battery=item['feature_rating']['battery'],
            display=item['feature_rating']['display'],
            ram=item['feature_rating']['ram'],
            storage=item['feature_rating']['storage'],
            dates = dates,
            dates_pos = pos,
            dates_neg = neg,
            dates_neu = neu,
        )

