#Caesar Cipher Decoder - www.101computing.net/caesar-cipher-decoder/

print("### Caesar Shift Decoder ###")
cipher = input("Enter your cipher text:\n")

total = 0

for i in range(0,25):
  #print("Key:" + str(i) + "A = " + str(65+i))
  plaintext = ""
for letter in cipher:
  plaintext = ""
  cipher = cipher.upper()
  total = total + 1
  ascii = ord(letter)
  if ascii > 90:
    ascii += 26
    plaintext = plaintext + chr(ascii)
  elif ascii >= 65 and ascii <= 90:
    ascii += total
    plaintext = plaintext + chr(ascii)
  else:
    plaintext = plaintext + chr(ascii)
print(plaintext)
