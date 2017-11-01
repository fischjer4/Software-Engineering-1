#Proves that periodsToBreaks works correctly
import kwic

document="Hello there. How are you. doing today. "
assert(kwic.kwic(document,periodsToBreaks=True) == [(['are', 'you.', 'How'], 1), (['doing', 'today.'], 2), (['Hello', 'there.'], 0), 
    (['How', 'are', 'you.'], 1), (['there.', 'Hello'], 0), (['today.', 'doing'], 2), (['you.', 'How', 'are'], 1)])

