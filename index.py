import os, sys
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
        res = panda.process(item)
<<<<<<< HEAD
        return jsonify(result='res')
=======
        return jsonify(result=res)
>>>>>>> 0e04daf8cb1773cab90d484d61be2f081600259c

if __name__ == '__main__':
    app.run()
