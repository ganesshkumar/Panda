import os, sys
from flask import Flask, render_template, url_for, request, jsonify

sys.path.append('libs')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("test.html", request=request)

@app.route('/search', methods=['POST', 'GET'])
def search():
    print 'searching'
    search_term = request.args.get('search', '', type=str)
    print search_term
    return jsonify(result=search_term)

if __name__ == '__main__':
    app.run()
