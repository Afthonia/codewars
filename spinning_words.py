def spin_words(sentence):
	if sentence.count(" ") > 0:
		words = sentence.split(" ")
		for word in words:
			if len(word) >= 5:
				changed_word = list(word)
				changed_word.reverse()
				changed_word = "".join(changed_word)
				words.insert(words.index(word), changed_word)
				words.remove(word)

		changed_words = " ".join(words)
		return changed_words
			
	else:
		if len(sentence) >= 5:
			words = list(sentence)
			words.reverse()
			words = "".join(words)
            
	return words
