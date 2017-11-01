#Proves that listPairs works WITH the lowercase AND stiping of punctuation AND the pairs themselves are alphabetized
import kwic

document="Hello there!\nHello to you there?\nIm. good\nYeah Im. good"
assert(kwic.kwic(document,listPairs=True) == ([(['good', 'Im.'], 2), (['good', 'Yeah', 'Im.'], 3), (['Hello', 'there!'], 0), 
    (['Hello', 'to', 'you', 'there?'], 1), (['Im.', 'good'], 2), (['Im.', 'good', 'Yeah'], 3), (['there!', 'Hello'], 0), 
    (['there?', 'Hello', 'to', 'you'], 1), (['to', 'you', 'there?', 'Hello'], 1), (['Yeah', 'Im.', 'good'], 3), 
    (['you', 'there?', 'Hello', 'to'], 1)], [(('good', 'im'), 2), (('hello', 'there'), 2)]))