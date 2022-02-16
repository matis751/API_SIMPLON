from flask import Blueprint
from flask import jsonify
from flask import Flask
from flask import request
import Abr, Class
from main import creat_tree




app = Flask(__name__)
@app.route('/text', methods=['POST', 'GET'])
def create_tree():
    request.data = 'https://en.wikipedia.org/wiki/Tokyo'
    tree = creat_tree(Class.Tree(), request.data)
    r = Abr.Iterative_tree_shearch(tree.root, hash('and'))
    if r is not None:
        return ({r.word_occurence[0] : r.word_occurence[1]})
    else:
        return('Rien trouver')

