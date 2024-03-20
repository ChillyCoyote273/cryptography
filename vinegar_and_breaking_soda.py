import matplotlib.pyplot as plt
from vinegar_cipher import decrypt


def shift(c, k):
    return chr((ord(c) + ord(k) - 2 * ord('A')) % 26 + ord('A'))


def key_length(cipher_text, max_shift):  # key length is 6
    shifts = [0]
    for i in range(1, max_shift + 1):
        shifts.append(sum(1 if cipher_text[j] == cipher_text[j + i] else 0 for j in range(len(cipher_text) - i)))
    plt.bar(range(max_shift + 1), shifts)
    plt.show()


def frequency_plots(cipher_text, length):
    text_chunks = [cipher_text[i::length] for i in range(length)]
    frequency_dictionaries = [{chr(i): 0 for i in range(ord('a'), ord('z') + 1)} for _ in range(length)]
    for i in range(length):
        for c in text_chunks[i]:
            frequency_dictionaries[i][c] += 1
    sorted_frequencies = [
        list(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
        for dictionary in frequency_dictionaries
    ]
    fig, axs = plt.subplots(length, 1, constrained_layout=True, squeeze=True)
    for i, ax in enumerate(axs):
        ax.bar(range(26), [item[1] for item in sorted_frequencies[i]])
        ax.set_xticks(range(26))
        ax.set_xticklabels([item[0] for item in sorted_frequencies[i]])
    plt.show()


def get_key_from_common_letters(most_common):  # turing
    return ''.join(chr((ord(c) - ord('e') + 26) % 26 + ord('a')) for c in most_common)


def get_text():
    with open('encrypted_secret_message.txt', 'r') as f:
        return f.read()


def main():
    text = get_text()
    key_length(text, 20)


if __name__ == '__main__':
    main()
