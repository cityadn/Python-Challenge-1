def NumberWords():
    global digits
    global characters
    digits = "0123456789"
    characters = "abcdABCD@#!£"
    
NumberWords()
alphanumerics = digits + characters
print(alphanumerics)
