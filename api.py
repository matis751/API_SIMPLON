from flask import Blueprint
from flask import jsonify
from flask import Flask, render_template, request
import Abr, Class
from main import creat_tree
from flask import json


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def create_tree():

    url = request.json['url']
    word = request.json['word']

    tree = creat_tree(Class.Tree(), url)
    r = Abr.Iterative_tree_shearch(tree.root, hash(word))

    if r is not None:
        return jsonify({r.word_occurence[0] : r.word_occurence[1]})
    else:
        return(' not found')

