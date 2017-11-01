#Proves ignoreWords
import kwic

document="Hello there.\nHow are you doing today?\n"
assert(kwic.kwic(document, ignoreWords=["How"]) == [(['are','you','doing','today?','How'], 1),(['doing','today?','How','are','you'], 1),(['Hello', 'there.'], 0),
    (['there.', 'Hello'], 0),(['today?','How','are','you','doing'], 1),(['you','doing','today?','How','are'], 1)])
