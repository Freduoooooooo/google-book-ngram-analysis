import os
import gzip
import logging

def base_form(words):
	"""
	Get the base form of a list of words
	"""
	from nltk import pos_tag
	from nltk.stem.wordnet import WordNetLemmatizer

	def _wn_tag(tag):
		if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
			return 'n'
		elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
			return 'v'
		elif tag in ['RB', 'RBR', 'RBS']:
			return 'r'
		elif tag in ['JJ', 'JJR', 'JJS']:
			return 'a'
		return 'n'

	tags = pos_tag(words)
	base_form = []

	for tag in tags:
		wn_tag = _wn_tag(tag[1])
		base = WordNetLemmatizer().lemmatize(tag[0], wn_tag)
		base_form.append(base)

	return base_form


def read_data_file(data_file, output_file, topic):
	"""
	Get lines in data_file that contain the topic
	"""
	if not os.path.isfile(data_file):
		print('file not found:', data_file)
		return

	output = open(output_file, 'w+')
	topic = topic.lower().split()
	word_appears = False

	with gzip.open(data_file, 'r') as file:
		for idx, line in enumerate(file):
			line = str(line, 'utf-8').lower()

			if idx % 5000000 == 0:
				print('line:', idx, '\tcurrent word:', line[0:10])
			
			temp = True
			for word in topic:
				temp &= word in line
			if temp:
				word_appears = True
				output.write(line)

	if not word_appears:
		print(topic, 'not found in', data_file)

	output.close()


if __name__ == '__main__':
	output_file = 'output.txt'
	prefix2 = 'googlebooks-eng-all-2gram-20120701-'

	data = {
		'knowledge represent': prefix2+'kn.gz',
		'distribut system': prefix2+'di.gz',
		'internet protocol': prefix2+'in.gz',
		'information theory': prefix2+'in.gz',
		'amplitude modulat': prefix2+'am.gz',
		'quantum comput': prefix2+'qu.gz',
		'biochemic weapon': prefix2+'bi.gz',
		'nuclear fusion': prefix2+'nu.gz',
		'feminis campaign': prefix2+'fe.gz'
	}

	output = open(output_file, 'w')
	output.close()

	for topic, data_file in data.items():
		print('='*40)
		print('topic:', topic)
		read_data_file(data_file, output_file, topic)


	
