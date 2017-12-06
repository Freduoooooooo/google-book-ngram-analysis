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
		'amplitude modulat': prefix2+'am.gz',	# amplitude modulation
		'amber alert': prefix2+'am.gz',
		'baby boom': prefix2+'ba.gz',
		'barack obama': prefix2+'ba.gz',
		'biochemic weapon': prefix2+'bi.gz',	# biochemical weapon
		'bitcoin mining': prefix2+'bi.gz',
		'college educat': prefix2+'co.gz',		# college education
		'communis party': prefix2+'co.gz',		# communist party
		'data compression': prefix2+'da.gz',
		'data mining': prefix2+'da.gz',
		'data science': prefix2+'da.gz',
		'distribut system': prefix2+'di.gz',	# distributed system
		'electronic book': prefix2+'el.gz',
		'electronic music': prefix2+'el.gz',
		'feminis movement': prefix2+'fe.gz',	# feminist movement
		'heavy metal': prefix2+'he.gz',
		'hello world': prefix2+'he.gz',
		'hillary clinton': prefix2+'hi.gz',
		'information theory': prefix2+'in.gz',
		'integrat circuit': prefix2+'in.gz',	# integrated circuit
		'internet protocol': prefix2+'in.gz',
		'knowledge represent': prefix2+'kn.gz',	# knowledge representation
		'nuclear weapon': prefix2+'nu.gz',
		'quantum comput': prefix2+'qu.gz',		# quantum computing
		'question answer': prefix2+'qu.gz'	 	# question answering
	}

	output = open(output_file, 'w')
	output.close()

	for topic, data_file in data.items():
		print('='*40)
		print('topic:', topic)
		read_data_file(data_file, output_file, topic)


	
