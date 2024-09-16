# SCT_CS_1

**Introduction**
This Python program implements the Caesar cipher, a simple substitution cipher where each letter of the plaintext is shifted a fixed number of positions down the alphabet.

**Usage**

1 Download python file:
    
    ceaser_cypher.py

2 Run the program:

    python caesar_cypher.py

3 Follow the prompts:

    Select the mode: 'e' for encryption or 'd' for decryption.
    Enter the shift value (the number of positions to shift the letters).
    Input the text to be encrypted or decrypted.

**Functionality**
**Encryption**: Shifts each letter of the plaintext to the right by the specified shift value.
**Decryption**: Shifts each letter of the ciphertext to the left by the specified shift value.
**Handling of non-alphabetic characters**: Non-alphabetic characters (e.g., numbers, symbols) are preserved unchanged.

**Customization**
**Shift value**: You can modify the shift value to change the encryption or decryption strength.
**Alphabet**: If you need to work with different alphabets or character sets, you can modify the "letters" variable in the code.

**Example**:

    Mode: e
    Shift value: 3
    Text: hello world
    Ciphertext: khoor zruog
