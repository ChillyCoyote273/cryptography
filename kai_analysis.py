from bad_vinegar_cipher import get_key, decrypt


def chi_squared(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))


def letter_frequencies(text):
    text = text.lower()
    return [text.count(chr(i)) / len(text) for i in range(ord('a'), ord('z') + 1)]


def english_frequencies():
    return [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
            0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
            0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]


def main():
    with open('kai_analysis.txt') as f:
        text = f.read().strip()
    best = (float('inf'), 0, 0)
    for start in range(26):
        for step in range(1, 26):
            key = get_key(start, step)
            decrypted = decrypt(text, key)
            observed = letter_frequencies(decrypted)
            expected = english_frequencies()
            score = chi_squared(observed, expected)
            if score < best[0]:
                best = (score, start, step)
    key = get_key(best[1], best[2])
    decrypted = decrypt(text, key)
    print(f'Start: {chr(best[1] + ord("a"))}')
    print(f'Step: {best[2]}')
    print(f'Decrypted: {decrypted}')
    print(f'Chi-squared: {best[0]}')
    with open('kai_analysis_decrypted.txt', 'w') as f:
        f.write(decrypted)


if __name__ == '__main__':
    main()
