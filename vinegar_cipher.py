def shift(c, k):
    return chr((ord(c) + ord(k) - 2 * ord('a')) % 26 + ord('a'))


def invert_key(key):
    return ''.join(chr(26 - ord(c) + 2 * ord('a')) for c in key)


def encrypt(plain_text, key):
    plain_text = plain_text.lower()
    key = key.lower()
    key_len = len(key)
    key = key * (len(plain_text) // key_len) + key[:len(plain_text) % key_len]
    return ''.join(shift(c, k) for c, k in zip(plain_text, key))


def decrypt(cipher_text, key):
    return encrypt(cipher_text, invert_key(key.lower()))


def main():
    while True:
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            plain_text = input('Enter the plain text: ')
            key = input('Enter the key: ')
            print('Cipher text:', encrypt(plain_text, key))
        elif choice == '2':
            cipher_text = input('Enter the cipher text: ')
            key = input('Enter the key: ')
            print('Plain text:', decrypt(cipher_text, key))
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
