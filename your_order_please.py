def order(sentence):
	sentence = str(sentence)
	arr = sentence.split(' ')
	ret = ""
	i = 0
	m = len(arr)
	while i < m:
		i += 1
		for word in arr:
			char = str(i)
			if word.find(char) == -1:
				continue
			else:
				ret += word
		if i < m:
			ret += ' '
	return ret