#Proves that listPairs works(minus the lowercase, and stiping of punctuation)
import kwic

document="hello there\nhello you there\nIm good\n"
assert(kwic.kwic(document,listPairs=True) == (([(['good', 'Im'], 2), (['hello', 'there'], 0), (['hello', 'you', 'there'], 1), 
    (['Im', 'good'], 2), (['there', 'hello'], 0), (['there', 'hello', 'you'], 1), (['you', 'there', 'hello'], 1)], [(('hello', 'there'), 2)])))
