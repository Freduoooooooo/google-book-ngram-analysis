import os
import io
from nltk import pos_tag
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

dir_path = os.path.split(os.path.realpath(__file__))[0]

def _wn_tag(tag):
	if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
		return 'n'
	elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
		return 'v'
	elif tag in ['RB', 'RBR', 'RBS']:
		return 'r'
	elif tag in ['JJ', 'JJR', 'JJS']:
		return 'a'
	return 'o'


def get_tag(word):
	word_tok = word_tokenize(word)
	tag = pos_tag(word_tok)

	tag_list = [_wn_tag(i[1]) for i in tag]
	
def preprocess(word):
	
	
	word_ = word.replace(' ', '_')
	file =word_ + '.txt'
	filename = os.path.join(dir_path, 'data', file)

	if not os.path.isfile(filename):
		print('file not found:', file)

	with io.open(filename, 'r') as file:
		file = file.readlines()

	file
	return file

if __name__ == "__main__":
	a = preprocess("artificial intelligence")
	print(a)