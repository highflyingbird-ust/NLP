import gensim
x=int(input('Enter vocab size: '));
model = gensim.models.KeyedVectors.load_word2vec_format('/home/sampath/Desktop/thesemicolon/word2vec.bin',binary=True,limit=x)
def wordVec(word):
    print model.most_similar(word)
    
