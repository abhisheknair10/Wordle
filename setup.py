from english_words import english_words_set

final = []

english_words_set = list(english_words_set)

for i in range(len(english_words_set)):
	if(len(english_words_set[i]) == 5):
		if(english_words_set[i][0].islower()):
			final.append(english_words_set[i]) 
print(final)
print(len(final))
