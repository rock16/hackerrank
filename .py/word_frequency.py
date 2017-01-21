import string
table = string.maketrans(string.punctuation+string.lowercase,
                         " "*len(string.punctuation)+string.lowercase)
def count_word_frequency(word_list):
    H_ash = {}
    total_words = 0
    for word in word_list:
        if word in H_ash:
            H_ash[word] += 1
        else:
            H_ash[word] = 1
        total_words += 1
    return [H_ash,total_words]

def read(in_file):
    try:
        f = open(in_file, 'r')
        return f.read()
    except IOError:
        print "Error reading or opening: ", in_file   

def creat_word_list(text):
    text=text.translate(table)
    word_list = text.split()
    return word_list

def for_file(in_file):
    word_list = read(in_file)
    word_list = creat_word_list(word_list)
    frequency = count_word_frequency(word_list)
    for words,num in frequency[0].iteritems():
        print words,num
    print "total words: ",frequency[1]

def for_string(in_file):
    word_list = creat_word_list(in_file)
    frequency = count_word_frequency(word_list)
    for words,mum in frequency[0].iteritems():
        print words,mum
    print "total words: ",frequency[1]

def main():
    n = raw_input("Type f to give me a file or s to give me a string as input:")
    if n.lower() == 'f':
        in_file = raw_input("Give me the file path: ") #for most app/software
        for_file(in_file)                              #users provide file path
    elif n.lower() == 's':
        in_file = raw_input("Give me the string/text: ")
        for_string(in_file)
    else:
        print "you did not provide any valid input"

if __name__ =="__main__":
    main()
