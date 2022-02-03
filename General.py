
number = '0123456789'
def worddigalpha(word):
    digit = [str(symbol) for symbol in word if symbol in number]
    for symbol in digit:
        word = word[:word.index(symbol)] + word[word.index(symbol) + 1:]
    digit = int(''.join(digit))
    return [digit, word]
def rearrange(sentence):
    new_sentence = ''
    dict_sentence = dict([worddigalpha(word) for word in sentence.split()])
    for word in range(1, len(dict_sentence)+1):
        new_sentence += dict_sentence[word] + ' '
    return new_sentence

sentence = str(input())
print(rearrange(sentence), end='')