words = str(input("Gimme string"))
word = words.split()
count = 0
dictionary = {}
for word_check in word:
    y = str(word.count(word_check))
    x = str(word[count])
    count = count + 1
    dictionary.update({x: y})
print(dictionary)
    
    
