import os
import nltk 
from rake_nltk import Rake 
r= Rake()
x=raw_input('Enter text: ');
# x='The little red dog, barked at the cat. The cat was flying';
r.extract_keywords_from_text(x)
k = r.get_ranked_phrases()
key = ','.join(k)
print 'Rake output: '+key
tokens = nltk.word_tokenize(x)
pos = nltk.pos_tag(tokens)
# print pos
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(pos)
print result
# result.draw()