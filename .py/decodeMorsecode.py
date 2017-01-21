def decodeWord(word):

    letter = word.split()
    length = len(letter) -1
    while length >= 0:
        letter[length] = MORSE_CODE[letter[length]]
        length -= 1
    return letter
        
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    letter = morseCode.split("   ")
    sentence = []
    
    for pos,val  in enumerate(letter):
        sentence.extend(decodeWord(val))
        if pos < len(letter) - 1 and len(sentence) > 0:
            sentence.extend([" "])
        
    return "".join(sentence)
