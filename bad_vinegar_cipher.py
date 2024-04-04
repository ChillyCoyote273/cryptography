from vinegar_cipher import encrypt, decrypt


def get_key(start=0, step=1):
    return ''.join(chr((i * step + start) % 26 + ord('a')) for i in range(26))


def main():
    text = input("Enter the text: ")
    start = input("Enter the start: ")
    start = ord(start) - ord('a')
    step = int(input("Enter the step: "))
    key = get_key(start, step)
    print(f'Encrypt: {encrypt(text, key)}')
    print(f'Decrypt: {decrypt(text, key)}')


if __name__ == '__main__':
    main()
