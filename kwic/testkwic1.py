#Proves that a line can be kwic'd
import kwic

document="Hello there.\n"
assert(kwic.kwic(document) == [(['Hello', 'there.'], 0), (['there.', 'Hello'], 0)])