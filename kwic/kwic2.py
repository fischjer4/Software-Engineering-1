def insert(shiftList, y):
    word = 0
    while(y > 0 and (word < len(shiftList[y-1][0]) and word < len(shiftList[y][0])) and (cmp(shiftList[y-1][0][word].lower(), shiftList[y][0][word].lower()) == 1 or cmp(shiftList[y-1][0][word].lower(), shiftList[y][0][word].lower()) == 0)):
        y1 = len(shiftList[y-1][0])
        y0 = len(shiftList[y][0])
        if((cmp(shiftList[y-1][0][word].lower(), shiftList[y][0][word].lower()) == 1) or (word+1 >= y0 and word+1 < y1)):
            bigger = shiftList[y-1]
            shiftList[y-1] = shiftList[y]
            shiftList[y] = bigger
            y = y - 1
            word = 0
        if(cmp(shiftList[y-1][0][word].lower(), shiftList[y][0][word].lower()) == 0):
            word = word + 1

def alphabetize(shiftList):
    if(len(shiftList) > 1): #if shiftList has atleast 2 tuples in it
        for i in range(1,len(shiftList)): #insertion sort 
            insert(shiftList,i)

def shift(shiftList,words, lineNum):
    for i in range(0,(len(words))):
        tup = (list(words),lineNum)  #must be typecasted to str() otherwise will be mutated on next go around
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
        shift(shiftList,splitWords, i)
    
    alphabetize(shiftList) #alphabetize the tuples

    return (shiftList); #return the shiftList as a tuple
        