def caesar():
    '''encodes text by Caesar Cipher'''
    plaintext_list = []  # creates empty list plaintext_list
    plaintext = input('Plaintext: ')  # gets plaintext from user
    n = int(input('Shift: '))  # gets shift value from user
    for i in range(len(plaintext)):
        if plaintext[i].islower():  # checks if character in string plaintext is lower case letter
            plaintext_list.append(chr((((ord(plaintext[i]) - 97) + n) % 26) + 97))  # converts ASCII index of a letter to alphabetical index and makes shift
        elif plaintext[i].isupper():  # checks if character in string plaintext is upper case letter
            plaintext_list.append(chr((((ord(plaintext[i]) - 65) + n) % 26) + 65))  # converts ASCII index of a letter to alphabetical index and makes shift
        else:
            plaintext_list.append(plaintext[i])  # if i is not alphabetical, appends i from string plaintext to plaintext_list without making shift
    print('Ciphertext: ', end = ''.join(plaintext_list))  # prints plaintext_list not as array but string

caesar()
