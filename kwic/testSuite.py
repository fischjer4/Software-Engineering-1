
import kwic0

print('_______________________________________________________________________')
print('testkwic0')
document = ""
try:
    assert(kwic0.kwic(document) == [])
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic1')
document="Hello there.\n"
try:  
    assert(kwic0.kwic(document) == [(['Hello', 'there.'], 0), (['there.', 'Hello'], 0)])
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic2')
document="Hello there.\nHow are you doing today?\n"
try:  
    assert(kwic0.kwic(document) == [(['are','you','doing','today?','How'], 1),(['doing','today?','How','are','you'], 1),(['Hello', 'there.'], 0),
        (['How','are','you','doing','today?'], 1), (['there.', 'Hello'], 0),(['today?','How','are','you','doing'], 1),(['you','doing','today?','How','are'], 1)])
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic3')
document="Hello there.\nHow are you doing today?\n"
try:  
    assert(kwic0.kwic(document, ignoreWords=["How"]) == [(['are','you','doing','today?','How'], 1),(['doing','today?','How','are','you'], 1),(['Hello', 'there.'], 0),
        (['there.', 'Hello'], 0),(['today?','How','are','you','doing'], 1),(['you','doing','today?','How','are'], 1)])
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic4')
document="Hello there. How are you. doing today. "
try:  
    assert(kwic0.kwic(document,periodsToBreaks=True) == [(['are', 'you.', 'How'], 1), (['doing', 'today.'], 2), (['Hello', 'there.'], 0), 
        (['How', 'are', 'you.'], 1), (['there.', 'Hello'], 0), (['today.', 'doing'], 2), (['you.', 'How', 'are'], 1)])
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic5')
try:  
    document="hello there\nhello you there\nIm good\n"
    assert(kwic0.kwic(document,listPairs=True) == (([(['good', 'Im'], 2), (['hello', 'there'], 0), (['hello', 'you', 'there'], 1), 
        (['Im', 'good'], 2), (['there', 'hello'], 0), (['there', 'hello', 'you'], 1), (['you', 'there', 'hello'], 1)], [(('hello', 'there'), 2)])))
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic6')
document="Hello there\nHello to you there\nIm good\nYeah Im good"
try:  
    assert(kwic0.kwic(document,listPairs=True) == ([(['good', 'Im'], 2), (['good', 'Yeah', 'Im'], 3), (['Hello', 'there'], 0), (['Hello', 'to', 'you', 'there'], 1), 
        (['Im', 'good'], 2), (['Im', 'good', 'Yeah'], 3), (['there', 'Hello'], 0), (['there', 'Hello', 'to', 'you'], 1), 
        (['to', 'you', 'there', 'Hello'], 1), (['Yeah', 'Im', 'good'], 3), (['you', 'there', 'Hello', 'to'], 1)], [(('good', 'im'), 2), (('hello', 'there'), 2)]))
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic7')
try:  
    document="hello here!\nhello here. again\nhello again"
    assert(kwic0.kwic(document,listPairs=True) == ([(['again', 'hello'], 2), (['again', 'hello', 'here.'], 1), (['hello', 'again'], 2), 
        (['hello', 'here!'], 0), (['hello', 'here.', 'again'], 1), (['here!', 'hello'], 0), (['here.', 'again', 'hello'], 1)],
        [(('again', 'hello'), 2), (('hello', 'here'), 2)]))

except:
    print('***** FAILED testkwic0')

print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic8')
try:  
    document="Hello there!\nHello to you there?\nIm. good\nYeah Im. good"
    assert(kwic0.kwic(document,listPairs=True) == ([(['good', 'Im.'], 2), (['good', 'Yeah', 'Im.'], 3), (['Hello', 'there!'], 0), 
        (['Hello', 'to', 'you', 'there?'], 1), (['Im.', 'good'], 2), (['Im.', 'good', 'Yeah'], 3), (['there!', 'Hello'], 0), 
        (['there?', 'Hello', 'to', 'you'], 1), (['to', 'you', 'there?', 'Hello'], 1), (['Yeah', 'Im.', 'good'], 3), 
        (['you', 'there?', 'Hello', 'to'], 1)], [(('good', 'im'), 2), (('hello', 'there'), 2)]))
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('testkwic9')
document = "Hello there.\nHello there, buddy.\nHello and goodbye, buddy.\nHello is like buddy Goodbye!"
try:  
    assert(kwic0.kwic(document, listPairs=True) ==  ([(['and', 'goodbye,', 'buddy.', 'Hello'], 2), (['buddy', 'Goodbye!', 'Hello', 'is', 'like'], 3), 
        (['buddy.', 'Hello', 'and', 'goodbye,'], 2), (['buddy.', 'Hello', 'there,'], 1), (['Goodbye!', 'Hello', 'is', 'like', 'buddy'], 3), 
        (['goodbye,', 'buddy.', 'Hello', 'and'], 2), (['Hello', 'and', 'goodbye,', 'buddy.'], 2), (['Hello', 'is', 'like', 'buddy', 'Goodbye!'], 3), 
        (['Hello', 'there,', 'buddy.'], 1), (['Hello', 'there.'], 0), (['is', 'like', 'buddy', 'Goodbye!', 'Hello'], 3), 
        (['like', 'buddy', 'Goodbye!', 'Hello', 'is'], 3), (['there,', 'buddy.', 'Hello'], 1), (['there.', 'Hello'], 0)], 
        [(('buddy', 'goodbye'), 2), (('buddy', 'hello'), 3), (('goodbye', 'hello'), 2), (('hello', 'there'), 2)]))
except:
    print('***** FAILED testkwic0')
print('_______________________________________________________________________')
