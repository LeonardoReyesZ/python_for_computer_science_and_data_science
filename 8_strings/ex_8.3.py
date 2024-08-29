# ex_8.3: encrypt a phrase
import string

def generate_encryption_key( sentence ):
    """Generate an encryption key based on the input sentence."""
    # remove duplicates and sort characters from the sentence
    unique_chars = ''.join( sorted(set(sentence.lower().replace(' ', ''))) )

    # start with the alphabet and replace the beginning with unique characters from the sentence
    alphabet = list( string.ascii_lowercase )
    key = unique_chars + ''.join( [char for char in alphabet if char not in unique_chars] )

    return key
# end generate_encryption_key

def encrypt_word(word, key):
    """Encrypts a single word using the provided encryption key."""
    if len(word) <= 1:
        return word # do not encrypt single-letter words

    encrypted_word = ""
    alphabet = string.ascii_lowercase

    for char in word.lower():
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_word += key[index]
        else:
            encrypted_word += char # Non-alphabet characters remain unchanged

    return encrypted_word
# end encrypted_word

def encrypt_phrase( phrase, key):
    """Encrypts a phrase using the encryption key."""
    words = phrase.split() # tokenize the phrase into words
    encrypted_words = [encrypt_word(word, key) for word in words] # encrypt each word
    return ' '.join(encrypted_words) # reassemble the encrypted phrase
# end encrypt_phrase


# test the program
sentence = input("Enter a sentece to generate an encryption key: ")
key = generate_encryption_key( sentence )

phrase = input("Enter a phrase to encrypt: ")
encrypted_phrase = encrypt_phrase( phrase, key )

print( f"Encrypted phrase: {encrypted_phrase}" )