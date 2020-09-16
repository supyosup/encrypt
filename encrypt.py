#!/usr/local/bin/python3

# prompt user for message & key
user_message = input('Enter your message: ')
user_key = input('Enter your key: ')

# initialize variables
encrypted_message = ['-']
encrypted_string = ''
i = 0
decrypted_string = ''
overflow_flag = [0] * len(user_message) 

# loop thru entire user_message
for char in user_message:
    # convert user_message char to ascii
    ascii_char = ord(char)
    
    # check if we are at the end of our user_key, reset to starting index
    if i == len(user_key):
        i = 0
    
    # convert user_key char to ascii
    ascii_key = ord(user_key[i])
    
    # check for overflow, set flag if overflow
    if (ascii_char + ascii_key) > 255:
        converted_char = (ascii_char + ascii_key) % 255
        overflow_flag[i] = 1
    else:
       converted_char = ascii_char + ascii_key
        
    # append the converted char to the encrypted_message
    encrypted_message.append(converted_char)
    encrypted_message.append('-')

    # convert the ascii to a char and add to encrypted_string
    encrypted_string += chr(converted_char)

    # advance to the next index user_key
    i += 1

# remove the trailing '-' from the encrypted_message, print the encrypted_message & encrypted_string
encrypted_message.pop()
print('\nEncrypted message:', end = '')
for num in encrypted_message:
    print(num, end='')

print('\nEncrypted string: {}'.format(encrypted_string))

# decrypt the encrypted_message
i = 0
for num in encrypted_message:
    if num == '-':
        continue

    # check if we are at the end of our user_key, reset to starting index
    if i == len(user_key):
            i = 0
    
    # convert user_key char to ascii
    ascii_key = ord(user_key[i])
    
    # if overflow flag is set for particular index, we must add 255 to get the correct value
    if overflow_flag[i] == 1:
       decrypt_char = num + 255 - ascii_key
    else:
        decrypt_char = num - ascii_key
    
    # convert decrypt_char from ascii to chr, add to decrypt_string
    decrypted_string += chr(decrypt_char)

    # advance to the next index in user_key
    i += 1

# finally, we print our decrypted_string
print('\nDecrypted string: {}'.format(decrypted_string))
