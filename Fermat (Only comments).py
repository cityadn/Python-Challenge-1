"""Fermat's Little Theorem:
If 'n' is prime, and 'a' has no factors in common with 'n', then
the remainder when 'a^n-1' is divided by 'n', is always 1.

THE FERMAT TEST:
1) To test whether n is prime, pick a base 'a', then...
2) Look at the remainder from 'a^n-1'/'n'
3) If it's not 1, 'n' is not prime

A function called 'pow' gives you the remainder when 1 number
to the power of a second is divided by a third number

E.g. n =91
pow(2, n-1, n)
>> 64

n = 97
pow(2, n-1, n)
>> 1


Unfortunately, if we give the number 1729...
1729 = 7*13*19 = n
pow(2, n-1, n)
>> 1
It shouldn't be 1, as it's not prime

1729 is a false positive!
The remainder when a^1728 is divided by 1729 is 1, even though
1729 isn't prime.

2^1728/1729 gives remainder 1... Now halve the power
2^864/1729 gives remainder 1... Now halve it again
2^432/1729 gives remainder 1... Halve it again
2^216/1729 gives remainder 1... Halve it again
2^108/1729 gives remainder 1... Halve  it again
2^54/1720 gives remainder 1065

Compare and contrast 1729 with the case of 233, which really is prime
2^232/233 gives remainder 1
2^116/233 gives remainder 1
2^58/233 gives remainder 1
2^29/233 gives remainder 1... can't halve anymore, 29 is odd
we have had 1's all the way down

Sadly, this doesn't always work...
Compare with the case of 353. which is also prime
2^352/353 gives remainder 1
2^176/353 gives remainder 1
2^88/353 gives remainder 352
We eventually reach n-1 as the remainder


A BETTER TEST - THE MILLER RABIN TEST:
To test whether n is prime or not, pick a base 'a'. then...
1) Look at the remainder from 'a^n-1'/'n'
2) Look at the remainder from 'a^('(n-1)'/2)'/'n'
3) Look at the remainder from 'a^('(n-1)'/4)'/'n'
4) Keep doing this until the power is odd, as you can't halve
an odd power.

If n is prime, you're guaranteed to EITHER get 1's all the way
down, OR to get n-1 at some point.

Works with all numbers, except 3277 (3277=29*113)
A false positive again!

2^3276/3277 gives remainder 1
2^1638/3277 gives remainder 3276
3276 is n-1. the behaviour if a prime (This is a
Miller-Rabin Pseudo-Prime

Some numbers (e.g. 1729) give false positives under the Fermat test to any base.
No numbers do that under the Miller-Rabin Test


There's something called a Lucas test, based on a
generalisation of the Fibonacci numbers.
Combine a Miller-Rabin test or two, with a strong Lucas test
It's not known whether false positives (for the Lucas test) exists



