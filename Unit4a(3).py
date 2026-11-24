sentence = "apple mango apple orange mango apple"

words = sentence.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)