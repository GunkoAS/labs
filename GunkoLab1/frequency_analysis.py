import frequency_analysis as fa

RU_FREQ_KEYS = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'


def create_frequency_dictionary(text):
	freq_dict = {}
	for letter in text:
		if not letter.isalpha():
			continue
		key = letter.lower()
		if key in freq_dict:
			freq_dict[key] += 1
		else:
			freq_dict[key] = 1
	return freq_dict


def sort_frequency_dictionary(freq_dict):
	return sorted(freq_dict, key=freq_dict.get, reverse=True)


def substitute_text_with_freq_dict(text, freq_dict):
	new_sentence = ""
	for letter in text:
		if not letter.isalpha():
			new_sentence += letter
		else:
			order = freq_dict.index(letter.lower())
			new_letter = RU_FREQ_KEYS[order]
			if letter.isupper():
				new_sentence += new_letter.upper()
			else:
				new_sentence += new_letter
	return new_sentence



encoded_file = open('stalker(coded).txt', 'r',encoding='utf8')
decoded_file = open('stalker(freq).txt', 'w',encoding='utf8')
text = encoded_file.read()
freq_dict = create_frequency_dictionary(text)
freq_dict = sort_frequency_dictionary(freq_dict)
decoded_file.write(substitute_text_with_freq_dict(text, freq_dict))
encoded_file.close()
decoded_file.close()



