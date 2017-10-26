import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/home/sampath/Desktop/stanford/'
os.environ['STANFORD_MODELS'] = '/home/sampath/Desktop/stanford/'

parser = stanford.StanfordParser(model_path="/home/sampath/Desktop/stanford/models/lexparser/englishPCFG.ser.gz")
dep_parser = stanford.StanfordDependencyParser(model_path="/home/sampath/Desktop/stanford/models/lexparser/englishPCFG.ser.gz")

x = raw_input('Enter text to be parsed: ');

dep =  list(parser.raw_parse(x))
# print dep[0]
print [parse.tree() for parse in dep_parser.raw_parse(x)]