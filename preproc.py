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

	return tag_list

def preprocess(word):
	# get the tag
	tag_list = get_tag(word)

	word_ = word.replace(' ', '_')
	file =word_ + '.txt'
	filename = os.path.join(dir_path, 'data', file)

	if not os.path.isfile(filename):
		print('file not found:', file)

	with io.open(filename, 'r') as file:
		text = file.readlines()

	word_list = []
	for i in text:
		new_line = i.replace('\n', '').split()
		word_list.append(new_line)
	
	word_list_new = [[word, tag_list, i[-3], i[-2], i[-1]] for i in word_list]
	return word_list_new

if __name__ == "__main__":
	# get the word list
	with io.open('wordlist.txt', 'r') as file:
		wordlist = file.readlines()

	wordlist = [i.replace('\n', '') for i in wordlist]

	final_list = []
	for name in wordlist:
		final_list += preprocess(name)
	
	output = open('output.txt', 'w+')
	for i in final_list:
		output.write(str(i))

	output.close()