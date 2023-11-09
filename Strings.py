def Replace(S1, S2, S3):
    S = S1.find(S2)
    E = S + len(S2)
    NewString = S1[0:S]
    NewString = NewString + S3
    NewString = NewString + S1[E:E + len(S1)]
    return NewString

Phrase = "Strings are the root of physics."
Word1 = "are"
Word2 = "may be"
print((Phrase, Word1, Word2))
#Replace
