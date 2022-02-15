import sys
import ipdb

sys.path.insert(0, 'abr')
import Hash, Abr
sys.path.insert(0, 'Class')
import Class
import scrapper


def creat_tree(tree):
    words = scrapper.scrapper(input())
    num = len(words)
    i = 0
    while i < num:
        node = Class.Node()
        node.key = Hash.hash_str(words[i])
        r = Abr.Tree_shearch(tree.root, node.key)
        if r == None:
            node.word_occurence[0] = words[i]
            node.word_occurence[1] += 1
            Abr.Tree_insert(tree, node)
        else:
            r.word_occurence[1] += 1
        i += 1

    Abr.Tree_walk(tree.root)

if __name__ == '__main__':
    tree = Class.Tree()
    creat_tree(tree)


