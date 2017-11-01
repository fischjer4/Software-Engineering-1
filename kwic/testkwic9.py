#Fixing stipPunc to stip all common punctuation that occurs in results.txt
#Testing that the 'big test example' works 
import kwic

document = "Hello there.\nHello there, buddy.\nHello and goodbye, buddy.\nHello is like buddy Goodbye!"
assert(kwic.kwic(document, listPairs=True) ==  ([(['and', 'goodbye,', 'buddy.', 'Hello'], 2), (['buddy', 'Goodbye!', 'Hello', 'is', 'like'], 3), 
    (['buddy.', 'Hello', 'and', 'goodbye,'], 2), (['buddy.', 'Hello', 'there,'], 1), (['Goodbye!', 'Hello', 'is', 'like', 'buddy'], 3), 
    (['goodbye,', 'buddy.', 'Hello', 'and'], 2), (['Hello', 'and', 'goodbye,', 'buddy.'], 2), (['Hello', 'is', 'like', 'buddy', 'Goodbye!'], 3), 
    (['Hello', 'there,', 'buddy.'], 1), (['Hello', 'there.'], 0), (['is', 'like', 'buddy', 'Goodbye!', 'Hello'], 3), 
    (['like', 'buddy', 'Goodbye!', 'Hello', 'is'], 3), (['there,', 'buddy.', 'Hello'], 1), (['there.', 'Hello'], 0)], 
    [(('buddy', 'goodbye'), 2), (('buddy', 'hello'), 3), (('goodbye', 'hello'), 2), (('hello', 'there'), 2)]))
