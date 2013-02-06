Secret Decoded
==============

Your task is to decode messages that were encoded with substitution ciphers. In a substitution cipher, all occurrences of a character are replaced by a different character. For example, in a cipher that replaces "a" with "d" and "b" with "e", the message "abb" is encoded as "dee".

The exact character mappings that are used in the substitution ciphers will not be known to you. However, the dictionary of words that were used will be given. You will be given multiple encoded messages to decode (one per line) and they may use different substitution ciphers. The same substitution cipher is used on all of the words in a particular message.

For each scrambled message in the input, your program should output a line with the input line, followed by the string " = " (without the quotes), followed by the decoded message.

NOTE: All inputs are from stdin and output to stdout. The input will be exactly like how it's given in the problem and

your output should exactly match the given example output

Example:

input file:

//dict
hello
there
yello
thorns
//secret
12334 51272
12334 514678


output:
12334 51272 = hello there
12334 514678 = hello thorns
