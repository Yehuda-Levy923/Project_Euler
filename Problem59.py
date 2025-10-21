# Function that decrypts a ciphertext using XOR with a repeating key
def xor_decrypt(cipher_bytes, key):
    res = []
    key_len = len(key)
    for i in range(len(cipher_bytes)):
        kb = ord(key[i % key_len])
        res.append(cipher_bytes[i] ^ kb)
    return bytes(res)

# Function that checks if all bytes are printable ASCII characters
def is_printable_ascii(data):
    for b in data:
        if b in (9, 10, 13):
            continue
        if b < 32 or b > 126:
            return False
    return True

# Function that generates all possible lowercase alphabetic keys of given length
def generate_keys(length):
    alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    if length <= 0:
        yield ""
        return

    def gen(prefix, remaining):
        if remaining == 0:
            yield prefix
            return
        for ch in alphabet:
            for k in gen(prefix + ch, remaining - 1):
                yield k

    for key in gen("", length):
        yield key

# Function that scores plaintext by checking if it contains the word "celebrated" (once successful and planing to minimize other outputs)
def score_plaintext(text):
    return "celebrated" in text.lower()

# Function that calculates the sum of the ascii values of the decrypted prompt
def sum_ascii(text):
    total = 0
    for ch in text:
        total += ord(ch)
    return total

# Function that brute-forces XOR decryption with all possible keys of given length
def brute_force_xor_with_sum(cipher_bytes):
    for key in generate_keys(3):
        decrypted = xor_decrypt(cipher_bytes, key)
        if is_printable_ascii(decrypted):
            text = decrypted.decode('ascii', errors='ignore')
            if score_plaintext(text):
                yield key, text, sum_ascii(text)

if __name__ == "__main__":
    raw = input("Enter ciphertext (comma-separated decimals): ")  # Inputs the ciphertext which we will decrypt
    ciphertext = bytes(int(x) for x in raw.split(","))  # Makes the input compatible with the code

    for key, text, ascii_sum in brute_force_xor_with_sum(ciphertext):  # Makes the output readable
        print("Key:", key, text, "\nASCII sum:", ascii_sum)  # Prints the valid output