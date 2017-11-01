#Proves that listPairs works WITH the lowercase AND stiping of punctuation
import kwic

document="hello here!\nhello here. again\nhello again"
assert(kwic.kwic(document,listPairs=True) == ([(['again', 'hello'], 2), (['again', 'hello', 'here.'], 1), (['hello', 'again'], 2), 
    (['hello', 'here!'], 0), (['hello', 'here.', 'again'], 1), (['here!', 'hello'], 0), (['here.', 'again', 'hello'], 1)],
    [(('again', 'hello'), 2), (('hello', 'here'), 2)]))
