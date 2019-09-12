words = input("Please enter a sentence: ")
sentence = words.split()
sentence.sort()

length = max((len(word) for word in sentence))
count_words = {}
for word in sentence:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

word_key = list(count_words.keys())
word_key.sort()
max_word_length = max((len(word)) for word in sentence)

for word in count_words:
    print("{:<{}}: {}".format(word, max_word_length, count_words[word]))

