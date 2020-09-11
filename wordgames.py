word = input("enter a word")

def anagram(word):
    valid_words = []#same length
    new_list = []#sorted a-z, equal length
    final_list = [] #sorted a-z, equal length, same letters
    with open("words.txt", "r") as f:
        for line in f:
            if len(line.strip()) == len(word):  
                valid_words.append(line.strip())
    for i in valid_words:
        new_list.append(sorted(i))
    for i in new_list:
        if i == sorted(word):
            final_list.append(i)
    for i in final_list:
        print(i)
anagram(word)
        