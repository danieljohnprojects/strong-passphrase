"""
Randomly generate a password with the required entropy.
"""

import argparse
import secrets

from functools import reduce
from math import ceil, log2

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nBits", help="The minimum entropy of the outputted password.", type=int, default=70)
parser.add_argument("-w", "--wordlist", help="The path to a file containing a list of words", type=str, default="wordlist.txt")
parser.add_argument("-d", "--delimiter", help="A string containing the characters to be used as delimiters. One is randomly chosen each time.", type=str, default=" -./,;[]")
parser.add_argument("-c", "--capitalise", help="Randomly capitalise the first letter of each token. This makes stronger passwords.", action="store_true")
# parser.add_argument("-m", "--misspell", help="Randomly misspell each word in the password. This makes stronger passwords.", action="store_true")
args = parser.parse_args()

if args.nBits <= 0:
    raise ValueError(f"Minimum entropy must be positive! Got {args.nBits}")

with open(args.wordlist) as f:
    tokens = f.readlines()
tokens = [token.strip() for token in tokens]
# Remove duplicate tokens
tokens = list(set(tokens))
tokenEntropy = log2(len(tokens)) + 1 if args.capitalise else log2(len(tokens))

# Remove duplicate delimiters
delimiters = list(set(list(args.delimiter)))
delimiterEntropy = log2(len(delimiters))

# Total entropy = tokenEntropy * N + delimiterEntropy * (N-1)
#               = N*(tokenEntropy + delimiterEntropy) - delimiterEntropy
# We choose N so that the total entropy is at least as large as args.nBits

nTokens = ceil((args.nBits + delimiterEntropy) / (tokenEntropy + delimiterEntropy))

password = [secrets.choice(tokens) for _ in range(nTokens)]
if args.capitalise:
    password = [secrets.choice([token, token.capitalize()]) for token in password]
password = reduce(
    lambda x,y: x + secrets.choice(delimiters) + y,
    password
)

totalEntropy = nTokens*(tokenEntropy + delimiterEntropy) - delimiterEntropy
print("Password:")
print(password)
print("Entropy:")
print(f"{totalEntropy:.3f}")