class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        return input_str[::-1]

    def is_english_vowel(self, character):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if character in vowels:
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        words = [i for i in sentence.split(" ")] # words stored in list
        word_length = [len(i) for i in words]    # length of each word
        index = word_length.index(max(word_length)) 
        return words[index]

    def get_word_lengths(self, text):
        words = [i for i in text.split(" ")]
        word_length = [len(i) for i in words]
        return word_length