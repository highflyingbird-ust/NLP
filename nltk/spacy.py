import spacy
from nltk import Tree

en_nlp = spacy.load('en')

doc = en_nlp("The quick brown fox jumps over the lazy dog.")

def tok_format(tok):
    return "_".join([tok.orth_, tok.tag_])


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(tok_format(node), [to_nltk_tree(child) for child in node.children])
    else:
        return tok_format(node)