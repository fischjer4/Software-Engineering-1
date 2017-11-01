#Proves that an empty line doesn't produce results
import kwic

document = ""
assert(kwic.kwic(document) == [])