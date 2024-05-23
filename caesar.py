
# 알파벳 정의
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# shift 값을 범위 내에 유지하는 함수
def normalize_shift(shift):
    return shift % 26

# 암호화 함수 
def encrypt(text, shift):
    shift = normalize_shift(shift)
    cipher_text = "" # 암호화된 문자 
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

# 복호화 함수
def decrypt(cipher_text, shift):
    shift = normalize_shift(shift)
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter
    print(f"The decoded text is {plain_text}")

def cipher_program():
    should_end = False
    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))  # shift 값을 26으로 나눈 나머지를 사용하여 범위 제한

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")

# 함수 호출
cipher_program()
