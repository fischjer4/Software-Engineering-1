import re
import copy

def alphaPairs(listPairs):
    for word in range(0,len(listPairs) - 1):
        if(cmp(listPairs[word][0][0],listPairs[word + 1][0][0]) == 0):
            if(cmp(listPairs[word][0][1],listPairs[word + 1][0][1]) == 1):
                bigger = listPairs[word]
                listPairs[word] = listPairs[word + 1]
                listPairs[word + 1] = bigger


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert(shiftList, y):
    word = 0
    #you should set shiftList jazz to variables so its not so long
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def alphabetize(shiftList):
    if(len(shiftList) > 1): #if shiftList has atleast 2 tuples in it
        for i in range(1,len(shiftList)): #insertion sort 
            insert(shiftList,i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ignore(word):
    return re.sub("[.,:;!?]","",word)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shift(shiftList,words, lineNum,**kwargs):
    for i in range(0,(len(words))):
        tup = (list(words),lineNum)  #must be typecasted to list() otherwise will be mutated on next go around
        if('ignoreWords' in kwargs and ignore(words[0].lower()) == str(kwargs['ignoreWords'][0]).lower()): #if ignoreWords is defined and the first word is it, skip it
            pass
        else:
            shiftList.append(tup)
        words.append(words[0])  #put the first word at the back
        words.remove(words[0])  #remove the first appearence of the first word... being the first word

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def confirmNoRepeat(tu,listPairs):
    for curTup in listPairs:
        if((tu[0][0] == curTup[0][0] and tu[0][1] == curTup[0][1]) or (tu[0][0] == curTup[0][1] and tu[0][1] == curTup[0][0])): #if the pairs are the same
            return False
    return True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stripPunc(shiftList):
    for line in range(0,len(shiftList)): #for the number of shifts
        for word in range(0,len(shiftList[line][0])): #for the number of words in that shift
             shiftList[line][0][word] = re.sub("(?<=[A-Za-z])[.,:;!?]","",shiftList[line][0][word]) #remove the punc
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def inOrder(pair):
    if(len(pair) == 2):
        if(cmp(pair[0],pair[1]) == 1):
            tmp = pair[0]
            pair[0] = pair[1]
            pair[1] = tmp
    return pair
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def checkPairs(bunch,listPairs):
    counter = 1 #counter starts at one because the pair is in the 'baseline' obviously
    for words in range(1,len(bunch[0][0])): #for the number of words in the first line in the bunch (our 'baseline')
        counter = 1
        for line in range(1,len(bunch)): #for the number of lines in the bunch that we are going to be searching through
            for secWords in range(1,len(bunch[line][0])): #for the number of words in the line we are currently comparing against
                if((cmp(bunch[0][0][words].lower(),bunch[line][0][secWords].lower()) == 0) and not(re.findall("[.!?]",bunch[line][0][secWords])) and not(re.findall("[.!?]",bunch[0][0][0])) and bunch[0][1] != bunch[line][1]): #if ther words are the same append them to the pair
                    if(cmp(bunch[0][0][0].lower(),bunch[line][0][secWords].lower()) != 0):
                        first = bunch[0][0][0].lower()
                        sec = bunch[line][0][secWords].lower()
                        counter = counter + 1
                        break
        if(counter > 1):
            pair = inOrder([first,sec]) #NOTE: alphabetizes the two words..althought this may be reduntant based off the fact that bunch was alphabetized
            tu = (tuple(pair),counter,);
            if(confirmNoRepeat(tu,listPairs)): #returns true if No repeat
                listPairs.append(tu) #add the tuple to the listPairs list
    alphabetize(listPairs)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def findPairs(shiftList):
    bunch = []
    listPairs = []
    stripPunc(shiftList)
    for cur in range(0, len(shiftList)-1): #for the number of tuples created -1 (don't need to check last tuple)
        itr = cur + 1
        del bunch[:]
        bunch.append(shiftList[cur])
        while(itr < len(shiftList) and cmp(shiftList[cur][0][0],shiftList[itr][0][0]) < 1): #while the first word of tuple i is ASCII smaller or equal to the y tuple add it to the bunch
            if(cmp(shiftList[cur][0][0],shiftList[itr][0][0]) == 0):
                bunch.append(shiftList[itr])
            itr = itr + 1
        if(len(bunch) > 1):
            checkPairs(bunch,listPairs) #see if there are pairs within the bunch
    alphaPairs(listPairs)    
    return listPairs

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def kwic(document, **kwargs):
    if(len(document) == 0): #if there are no lines
        shiftList = []
    else:
        if('periodsToBreaks' in kwargs):
            document = document.replace('\n', ' ')
            splitLines = re.split("(?<=[a-z]\.)\s",document)
        else:
            splitLines = document.split('\n')

        shiftList = []
        for i in range(0,len(splitLines)): #for the the number of lines
            splitWords = splitLines[i].split(' ')
            for x in splitWords[:]:     #remove the empty spaces due to sentences with spces after breaks like (hello there.   hi there)
                if x == '':
                    splitWords.remove(x)
            shift(shiftList,splitWords, i, **kwargs)

        alphabetize(shiftList) #alphabetize the tuples
    
    if('listPairs' in kwargs):       
        listPairs = findPairs(copy.deepcopy(shiftList))
        kwicResult = (shiftList,listPairs,); #return the shiftList as a tuple
    else:
        kwicResult = shiftList
        
    return kwicResult