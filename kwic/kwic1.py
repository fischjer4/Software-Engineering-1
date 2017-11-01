def shift(shiftList,words, lineNum,**kwargs):
    for i in range(0,(len(words))):
        tup = (list(words),lineNum)  #must be typecasted to list() otherwise will be mutated on next go around
        if('ignoreWords' in kwargs and ignore(words[0].lower()) == str(kwargs['ignoreWords'][0]).lower()): #if ignoreWords is defined and the first word is it, skip it
            pass
        else:
            shiftList.append(tup)
        words.append(words[0])  #put the first word at the back
        words.remove(words[0])  #remove the first appearence of the first word... being the first word

def kwic(document, **kwargs):
    if(len(document) == 0): #if there are no lines
        return []

    splitLines = document.split('\n')
    splitLines.remove('')   #remove the empty elements that split('\n') creates 
    
    shiftList = []
    for i in range(0,len(splitLines)): #for the the number of lines
        splitWords = splitLines[i].split(' ')
        shift(shiftList,splitWords, i, **kwargs)

    return shiftList
        