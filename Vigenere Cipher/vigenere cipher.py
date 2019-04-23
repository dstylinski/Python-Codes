def vigenere():
    '''encodes text by Vigenere Cipher'''
    plaintext_list = []  # creates empty list plaintext_list
    j = 0  # sets keyword index to 0
    plaintext = input('Plaintext: ')  # gets plaintext from user
    keyword = input('Keyword: ')  # gets keyword from user
    for i in range(len(plaintext)):
        if j >= len(keyword):  # checks if keyword index is greater than or equal length of keyword
            j = j - len(keyword)  # resets keyword index value
        if plaintext[i].islower():  # checks if character in string plaintext is lower case letter
            # converts ASCII index of a letter to alphabetical index and makes shift by keyword[j]
            plaintext_list.append(chr((((ord(plaintext[i]) - 97) + ((ord(keyword[j]) - 97) % 26)) % 26) + 97))
            j += 1  # increment keyword index value
        elif plaintext[i].isupper():  # checks if character in string plaintext is upper case letter
            # converts ASCII index of a letter to alphabetical index and makes shift by keyword[j]
            plaintext_list.append(chr((((ord(plaintext[i]) - 65) + ((ord(keyword[j]) - 65) % 26)) % 26) + 65))
            j += 1  # increment keyword index value
        else:
            # if i is not alphabetical, appends i from string plaintext to plaintext_list without making shift
            plaintext_list.append(plaintext[i])
    print('Ciphertext: ', end = ''.join(plaintext_list))  # prints plaintext_list not as array but string
vigenere()
