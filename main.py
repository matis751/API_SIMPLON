import sys
import ipdb

import Hash, Abr
import Class
import scrapper


def creat_tree(tree, url):
    word = scrapper.scrapper(url)
    num = len(word)
    i = 0
    while i < num: #creer un node pour chaque mot
        node = Class.Node()
        node.key = Hash.hash_str(word[i]) #assigne une valeur unique a chaque mots
        r = Abr.Tree_shearch(tree.root, node.key) #recherche dans l'arbre si la valeur existe deja
        if r == None: #si la valeur n'existe pas
            node.word_occurence[0] = word[i] #
            node.word_occurence[1] += 1 #
            Abr.Tree_insert(tree, node) #
        else:
            r.word_occurence[1] += 1
        i += 1

    return tree

if __name__ == '__main__':
    tree = Class.Tree()
    creat_tree(tree, sys.argv[1])


