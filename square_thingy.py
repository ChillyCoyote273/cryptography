def encrypt(text):
    square = {
        'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
        'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '24', 'k': '25',
        'l': '31', 'm': '32', 'n': '33', 'o': '34', 'p': '35',
        'q': '41', 'r': '42', 's': '43', 't': '44', 'u': '45',
        'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55'
    }
    inv = {
        '11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
        '21': 'f', 'g': '22', '23': 'h', '24': 'i', '25': 'k',
        '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p',
        '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u',
        '51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'
    }
    a = ''
    b = ''
    for c in text:
        a += square[c][0]
        b += square[c][1]

    a += b
    encrypted = ''
    for i in range(len(text)):
        encrypted += inv[a[i * 2: i * 2 + 2]]

    return encrypted


def decrypt(text):
    square = {
        'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
        'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '24', 'k': '25',
        'l': '31', 'm': '32', 'n': '33', 'o': '34', 'p': '35',
        'q': '41', 'r': '42', 's': '43', 't': '44', 'u': '45',
        'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55'
    }
    inv = {
        '11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
        '21': 'f', 'g': '22', '23': 'h', '24': 'i', '25': 'k',
        '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p',
        '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u',
        '51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'
    }
    a = ''.join(square[c] for c in text)

    decrypted = ''
    for a, b in zip(a[:len(text)], a[len(text):]):
        decrypted += inv[a + b]

    return decrypted


def main():
    while True:
        choice = input("Enter 1 to encfrypt, 2 to decrypt, 3 to exit: ")
        if choice == '1':
            text = input("Enter the text: ")
            print(encrypt(text))
        elif choice == '2':
            text = input("Enter the text: ")
            print(decrypt(text))
        else:
            break


if __name__ == '__main__':
    main()
