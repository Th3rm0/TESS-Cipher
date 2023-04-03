# TESS Cipher
The TESS Cipher is a more complex version of a standard Caeser Cipher.
TESS stands for Transformation Enhanced Shift System. The acronym is named after my rabbit.

The TESS Cipher is quite alike to the Caesar Cipher, however as the name implies, the value that the shift changes as the message is encrypted. It encrypts using the character set of a standard keyboard, but can be expanded upon if one wanted to.

## Encrypting

It works by making a for each loop for each character, and finds the character in the `characterSet` using the variable `i` to hold the index value of the character

```
i = 0

while character != characterSet[i]:

  i += 1
```

After finding the character's index in `characterSet`, `numberShift` is incremented, and `numberShift` is added to `i`

```
numberShift += shift

i += numberShift
```

Since `i` can grow to quite large numbers, there is a `while loop` to decrement `i` until `i` is within `characterSet`

```
while i >= len(characterSet):
  
  i -= len(characterSet)
```

After making `i` within the index value of `characterSet`, `characterSet[i]` is added to the `encryptedPhrase`

## Decrypting

Decryption is similar to encryption. It starts with a for loop to go through each character, and then finds the character's index value in `characterSet`

```
i = 0

while character != characterSet[i]:

  i += 1
```

After finding the character's index in `characterSet`, `numberShift` is incremented, and the `numberShift` is subtracted from `i`

```
numberShift += shift

i -= numberShift
```

There is another while loop to increase `i` to be within the bounds of `characterSet`

```
while i < 0:

  i += len(characterSet)
```

After making `i` within the index value of `characterSet`, `characterSet[i]` is added to `encryptedPhrase`
