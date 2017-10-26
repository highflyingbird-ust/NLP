Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import gnsim
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named gnsim
>>> import gensim
>>> model = gensim.models.KeyedVectors.load_word2vec_format('/home/sampath/Desktop/thesemicolon/word2vec.bin', binary=True,limit=100000)
>>> model.most_similar('boy')
[(u'girl', 0.8543272018432617), (u'teenager', 0.7606689929962158), (u'toddler', 0.7043969631195068), (u'teenage_girl', 0.6851483583450317), (u'man', 0.6824870109558105), (u'teen_ager', 0.6499968767166138), (u'son', 0.6337764263153076), (u'kid', 0.63228440284729), (u'youngster', 0.6183817386627197), (u'stepfather', 0.5989422798156738)]
>>> model.similarity('boy','man')
0.68248705829931611
>>> model.most_similar('data')
[(u'Data', 0.7262316346168518), (u'datasets', 0.603030264377594), (u'dataset', 0.5796631574630737), (u'databases', 0.5450120568275452), (u'statistics', 0.537885844707489), (u'information', 0.5368290543556213), (u'database', 0.5325667262077332), (u'Indicators', 0.46787744760513306), (u'analysis', 0.46195128560066223), (u'metrics', 0.455242395401001)]
>>> model.most_similar(negative('data'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'negative' is not defined
>>> model.most_similar(negative=('data'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'a' not in vocabulary"
>>> model.most_similar('hostel')
[(u'hostels', 0.8027491569519043), (u'Hostel', 0.6698718667030334), (u'dormitory', 0.5849594473838806), (u'accommodation', 0.5782935619354248), (u'dormitories', 0.5448293685913086), (u'canteen', 0.5311794281005859), (u'guesthouse', 0.5302660465240479), (u'lodgings', 0.5213447213172913), (u'railway_station', 0.5045744180679321), (u'premises', 0.5009268522262573)]
>>> model.most_similar(positive=['woman', 'king'], negative=['man'])
[(u'queen', 0.7118192911148071), (u'monarch', 0.6189674139022827), (u'princess', 0.5902431011199951), (u'crown_prince', 0.5499460697174072), (u'prince', 0.5377321243286133), (u'kings', 0.5236844420433044), (u'queens', 0.518113374710083), (u'sultan', 0.5098593235015869), (u'monarchy', 0.5087411999702454), (u'royal_palace', 0.5087165832519531)]
>>> model.most_similar(positive=['computer', 'science'])
[(u'computers', 0.6286005973815918), (u'mathematics', 0.5832267999649048), (u'biology', 0.5685796141624451), (u'Computer', 0.5564932823181152), (u'physics', 0.5369157791137695), (u'sciences', 0.5345146656036377), (u'robotics', 0.5173616409301758), (u'scientific', 0.513375997543335), (u'computing', 0.5084778070449829), (u'artificial_intelligence', 0.5067896842956543)]
>>> model.most_similar(positive=['tell', 'joke'])
[(u'know', 0.6594017148017883), (u'telling', 0.6423784494400024), (u'jokes', 0.6306398510932922), (u'laugh', 0.5976083874702454), (u'funny', 0.5902414321899414), (u'pretend', 0.5836428999900818), (u'joking', 0.5816095471382141), (u'kidding', 0.5680114030838013), (u'remember', 0.5564538836479187), (u'guess', 0.5555086731910706)]
>>> model.most_similar(positive=['machine', 'learning'])
[(u'machines', 0.5418595671653748), (u'learn', 0.47218501567840576), (u'computer', 0.4583987295627594), (u'simulator', 0.45783379673957825), (u'teaching', 0.456357479095459), (u'Learning', 0.44589924812316895), (u'mastering', 0.4417087137699127), (u'learner', 0.43878042697906494), (u'classroom', 0.4331943094730377), (u'classroom_instruction', 0.4319654107093811)]
>>> model.most_similar(positive=['soviet'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'soviet' not in vocabulary"
>>> model.most_similar(positive=['russia'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'russia' not in vocabulary"
>>> model.most_similar('russia')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'russia' not in vocabulary"
>>> model.most_similar('america')
[(u'american', 0.7169357538223267), (u'india', 0.6589398980140686), (u'obama', 0.6311533451080322), (u'thats', 0.6017112135887146), (u'indian', 0.5917373299598694), (u'.....', 0.578347384929657), (u'dont', 0.5698546171188354), (u'canada', 0.5664008855819702), (u'whats', 0.5597001910209656), (u'ppl', 0.5519510507583618)]
>>> model.most_similar('american')
[(u'america', 0.7169357538223267), (u'indian', 0.659941554069519), (u'thats', 0.5920654535293579), (u'dont', 0.5900669097900391), (u'india', 0.5897077322006226), (u'obama', 0.5797212719917297), (u'whats', 0.5609085559844971), (u'.....', 0.5561366677284241), (u'i_dont', 0.5474039316177368), (u'english', 0.5390437841415405)]
>>> model.most_similar('russia')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'russia' not in vocabulary"
>>> model.most_similar('india')
[(u'indian', 0.6967039704322815), (u'america', 0.6589398980140686), (u'canada', 0.6490967869758606), (u'uk', 0.6221641898155212), (u'american', 0.5897077322006226), (u'microsoft', 0.538908839225769), (u'buy_microsoft', 0.524248480796814), (u'viagra', 0.5152724981307983), (u'cialis', 0.5047127604484558), (u'India', 0.5045734643936157)]
>>> model.most_similar('kerala')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'kerala' not in vocabulary"
>>> model.most_similar('technology')
[(u'technologies', 0.8332264423370361), (u'innovations', 0.6230790615081787), (u'technological_innovations', 0.6102178692817688), (u'technological_advancement', 0.6036396622657776), (u'cutting_edge', 0.603604793548584), (u'technological_innovation', 0.6024578809738159), (u'technological_advancements', 0.5967106223106384), (u'innovation', 0.5921422243118286), (u'Technology', 0.5899151563644409), (u'advancements', 0.5859000086784363)]
>>> model.most_similar(positive=['woman', 'king'], negative=['man'])
[(u'queen', 0.7118192911148071), (u'monarch', 0.6189674139022827), (u'princess', 0.5902431011199951), (u'crown_prince', 0.5499460697174072), (u'prince', 0.5377321243286133), (u'kings', 0.5236844420433044), (u'queens', 0.518113374710083), (u'sultan', 0.5098593235015869), (u'monarchy', 0.5087411999702454), (u'royal_palace', 0.5087165832519531)]
>>> model.most_similar('blue')
[(u'red', 0.7225173711776733), (u'purple', 0.7134225368499756), (u'white', 0.6606028079986572), (u'maroon', 0.655741810798645), (u'colored', 0.6422423720359802), (u'orange', 0.642189085483551), (u'yellow', 0.6376121044158936), (u'teal', 0.6356960535049438), (u'pink', 0.6343377828598022), (u'pale_blue', 0.6308072209358215)]
>>> model.most_similar('james')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'james' not in vocabulary"
>>> model.most_similar('bond')
[(u'bonds', 0.7486938834190369), (u'bail', 0.5878828167915344), (u'surety_bond', 0.5336567163467407), (u'personal_recognizance', 0.4762340784072876), (u'Bail', 0.47461265325546265), (u'surety', 0.45017561316490173), (u'Bond', 0.44849133491516113), (u'own_recognizance', 0.4242705702781677), (u'Treasuries', 0.41651827096939087), (u'bonding', 0.4140605926513672)]
>>> model.most_similar('russia')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'russia' not in vocabulary"
>>> model.most_similar('china')
[(u'porcelain', 0.6392655372619629), (u'tableware', 0.5923404693603516), (u'glassware', 0.5766724348068237), (u'vases', 0.5563015937805176), (u'pottery', 0.5171363353729248), (u'ware', 0.49705737829208374), (u'vase', 0.4928912818431854), (u'cutlery', 0.49044227600097656), (u'linens', 0.48790350556373596), (u'Christmas_ornaments', 0.4808807969093323)]
>>> model.most_similar('india')
[(u'indian', 0.6967039704322815), (u'america', 0.6589398980140686), (u'canada', 0.6490967869758606), (u'uk', 0.6221641898155212), (u'american', 0.5897077322006226), (u'microsoft', 0.538908839225769), (u'buy_microsoft', 0.524248480796814), (u'viagra', 0.5152724981307983), (u'cialis', 0.5047127604484558), (u'India', 0.5045734643936157)]
>>> model.most_similar('microsoft')
[(u'buy_microsoft', 0.7902629375457764), (u'photoshop', 0.7404437065124512), (u'wo', 0.6462664604187012), (u'ca', 0.6310844421386719), (u'canada', 0.6283591985702515), (u'mac', 0.6273789405822754), (u'adobe', 0.6209553480148315), (u'ms', 0.6074421405792236), (u'linux', 0.5837568044662476), (u'uk', 0.5719637870788574)]
>>> model.similar('photoshop')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'KeyedVectors' object has no attribute 'similar'
>>> model.most_similar('photoshop')
[(u'microsoft', 0.7404437065124512), (u'buy_microsoft', 0.6846098899841309), (u'mac', 0.618245005607605), (u'ca', 0.6148430109024048), (u'wo', 0.6002457141876221), (u'adobe', 0.5933287143707275), (u'canada', 0.5911933183670044), (u'ms', 0.565524160861969), (u'uk', 0.5554846525192261), (u'linux', 0.5423921346664429)]
>>> model.most_similar('brad pitt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
KeyError: "word 'brad pitt' not in vocabulary"
>>> model.most_similar('ronaldo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 336, in most_similar
    mean.append(weight * self.word_vec(word, use_norm=True))
  File "/usr/local/lib/python2.7/dist-packages/gensim/models/keyedvectors.py", line 284, in word_vec
    raise KeyError("word '%s' not in vocabulary" % word)
