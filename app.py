import flask
from flask import request, jsonify, abort
from flask_cors import CORS, cross_origin
import json


app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>librAIry BoW</h1>
<p>A prototype API for NLP tasks over BoWs.</p>'''

def get_tokens(bow):
    tokens = ""
    for token in bow.split(" "):
        word = token.split("=")[0]
        frequency_and_pos = token.split("=")[1]
        frequency = frequency_and_pos.split("#")[0]
        for i in range(frequency):
            tokens += word + " "
    return tokens
        
@app.route('/tokens', methods=['POST'])
def post_tokens():
    if not request.json or not 'text' in request.json:
        abort(400)
    json_request = request.json
    bow = json_request['text']
    result= {}
    result.setdefault('tokens',"")
    for token in bow.split(" "):
        word = token.split("=")[0]
        frequency_and_pos = token.split("=")[1]
        frequency = frequency_and_pos.split("#")[0]
        for i in range(frequency):
            result['tokens'] += word + " "
    print(result)
    return jsonify(result)

@app.route('/groups', methods=['POST'])
def post_groups():
    if not request.json or not 'text' in request.json:
        abort(400)
    content = request.json
    bow = content['text']
    result= {}
    result.setdefault('groups',[])
    for token in bow.split(" "):
        word = token.split("=")[0]
        frequency_and_pos = token.split("=")[1]
        frequency = frequency_and_pos.split("#")[0]
        pos = frequency_and_pos.split("#")[1]
        annotation = {'token':word, 'pos':pos, 'freq':frequency}
        result['groups'].append(annotation)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
