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
for word in count_words:
    print("{:<{}}: {}".format(word, length, count_words[word]))

