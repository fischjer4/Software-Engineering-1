import re
import copy


def alphaPairs(listPairs):
    listPairs.sort()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def alphabetize(shiftList,leng):
    if(leng > 1): #if shiftList has atleast 2 tuples in it
        for y in xrange(1, leng): #insertion sort 
            word = 0
            #you should set shiftList jazz to variables so its not so long
            while(y > 0 and (word < len(shiftList[y-1][0]) and word < len(shiftList[y][0])) and (cmp(shiftList[y-1][0][word].lower(), shiftList[y][0][word].lower()) == 1 or shiftList[y-1][0][word].lower() == shiftList[y][0][word].lower()) ):
                y1 = len(shiftList[y-1][0])
                y0 = len(shiftList[y][0])
                if((cmp(shiftList[y-1][0][word].lower(), shiftList[y][0][word].lower()) == 1) or (word+1 >= y0 and word+1 < y1)):
                    bigger = shiftList[y-1]
                    shiftList[y-1] = shiftList[y]
                    shiftList[y] = bigger
                    y = y - 1
                    word = 0
                if( shiftList[y-1][0][word].lower() == shiftList[y][0][word].lower()):
                    word = word + 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ignore(word):
    return re.sub("[.,:;!?]","",word)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shift(shiftList,words, lineNum,**kwargs):
    for i in xrange(0,(len(words))):
        if('ignoreWords' in kwargs and ignore(words[0].lower()) == str(kwargs['ignoreWords'][0]).lower()): #if ignoreWords is defined and the first word is it, skip it
            pass
        else:
            tup = (list(words),lineNum)  #must be typecasted to list() otherwise will be mutated on next go around
            shiftList.append(tup)
        words.append(words[0])  #put the first word at the back
        words.remove(words[0])  #remove the first appearence of the first word... being the first word

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def confirmNoRepeat(first,sec,listPairs):
    for curTup in listPairs:
        if((first == curTup[0][0] and sec == curTup[0][1]) or (first == curTup[0][1] and sec == curTup[0][0])): #if the pairs are the same
            return False
    return True

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
    for words in xrange(1,len(bunch[0][0])): #for the number of words in the first line in the bunch (our 'baseline')
        counter = 1
        for line in xrange(1,len(bunch)): #for the number of lines in the bunch that we are going to be searching through
            checkingStr = ' '.join(bunch[line][0])
            my_regex = r'\b(?=\w)' + re.escape(bunch[0][0][words]) + r"\b(?!\w)"
            m = re.search(my_regex,checkingStr,re.IGNORECASE)
            if m:
                if(cmp(bunch[0][0][0].lower(),m.group().lower()) != 0 and (bunch[0][1] != bunch[line][1]) and not(re.findall("[.!?]",bunch[0][0][0]+m.group()))):
                    if confirmNoRepeat(bunch[0][0][0].lower(),m.group().lower(),listPairs):
                        first = bunch[0][0][0].lower()
                        sec = m.group().lower()
                        counter = counter + 1
                    else:
                        break
        if(counter > 1):
            pair = inOrder([first,sec]) #NOTE: alphabetizes the two words..althought this may be reduntant based off the fact that bunch was alphabetized
            tu = (tuple(pair),counter,);
            listPairs.append(tu) #add the tuple to the listPairs list
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def findPairs(shiftList,lenShift):
    bunch = []
    listPairs = []
    for line in xrange(0,lenShift): #for the number of shifts
        for word in xrange(0,len(shiftList[line][0])): #for the number of words in that shift
                shiftList[line][0][word] = re.sub("(?<=[A-Za-z])[.,:!?]","",shiftList[line][0][word]) #remove the punc
    for cur in xrange(0, lenShift-1): #for the number of tuples created -1 (don't need to check last tuple)
        itr = cur + 1
        del bunch[:] 
        if not(re.findall("[.!?]",shiftList[cur][0][0])):         
            bunch.append(shiftList[cur])
            while(itr < lenShift and (cmp(shiftList[cur][0][0],shiftList[itr][0][0]) < 1)): #while the first word of tuple i is ASCII smaller or equal to the y tuple add it to the bunch
                if(cmp(shiftList[cur][0][0],shiftList[itr][0][0]) == 0):
                    bunch.append(shiftList[itr])
                itr = itr + 1
            if(len(bunch) > 1):
                checkPairs(bunch,listPairs) #see if there are pairs within the bunch
    alphaPairs(listPairs)    
    return listPairs

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def beginShift(splitLines,shiftList, **kwargs):
    for i in xrange(0,len(splitLines)): #for the the number of lines
        splitWords = splitLines[i].split(' ')
        for x in splitWords[:]:     #remove the empty spaces due to sentences with spces after breaks like (hello there.   hi there)
            if x == '':
                splitWords.remove(x)
        shift(shiftList,splitWords, i, **kwargs)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def kwic(document, **kwargs):
    lenShift = 0
    splitLines =[]
    if(len(document) == 0): #if there are no lines
        shiftList = []
    else:
        if('periodsToBreaks' in kwargs):
            document = document.replace('\n', ' ')
            splitLines = re.split("(?<=[a-z]\.)\s",document)
        else:
            splitLines = document.split('\n')

        shiftList = []
        beginShift(splitLines,shiftList, **kwargs)
        lenShift = len(shiftList)
        alphabetize(shiftList,lenShift) #alphabetize the tuples

    if('listPairs' in kwargs):
        listPairs = findPairs(copy.deepcopy(shiftList),lenShift)
        kwicResult = (shiftList,listPairs,); #return the shiftList as a tuple
    else:
        kwicResult = shiftList

    return kwicResult