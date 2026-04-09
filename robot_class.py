class Robot:
	def __init__(self):
		self.__known_words = set()
		self._responses = ["I do not understand the input", "I already know the word ", "Thank you for teaching me "]
		for string in self._responses:
			arr = string.split(' ')
			for word in arr:
				self.learn_word(word)

	def learn_word(self, word):
		word_cpy = word.lower()
		if word.isalpha() == False:
			return self._responses[0]
		elif word_cpy in self.__known_words:
			return self._responses[1] + word
		else:
			self.__known_words.add(word_cpy)
			return self._responses[2] + word 