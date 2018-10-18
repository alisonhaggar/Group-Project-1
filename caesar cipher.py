
def caesar_cipher(variable_name):
    import string
    alphabet = string.ascii_lowercase
    cypher = input("Do you want to encrypt or decrypt")
    key = int(input("What is the key"))
    if cypher == "encrypt" or "Encrypt":
        variable_name.lower()
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        table = str.maketrans(alphabet,shifted_alphabet)
        encrypted = variable_name.translate(table)
        print(encrypted)
    elif cypher == "decrypt" or "Decrypt":
        variable_name.lower()
        shifted_alphabet = alphabet[-key:] + alphabet[:-key]
        table = str.maketrans(alphabet,shifted_alphabet)
        decrypted = variable_name.translate(table)
        print(decrypted)
    else:
        print("That was an invalid option")
        return

caesar_cipher(variable_name)
