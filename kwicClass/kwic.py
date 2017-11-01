import re
from eventspec import EventSpec 
from copy import deepcopy

class Kwic:
    def __init__(self, **kwargs):
        self.shiftList = []
        self.splitLines = []
        self.LP = []
        self.ig = ''
        self.fsm = EventSpec('kwic.fsm')
        self.runningText = ''
        self.lineNum = -1
        self.computeLP = False
        self.pb = False
        if(kwargs):
            if('ignoreWords' in kwargs):
                self.ig = kwargs['ignoreWords']
            if('periodsToBreaks' in kwargs):
                if(kwargs['periodsToBreaks'] == True):
                    self.pb = True
        self.fsm.event('callConstructor')

    def inOrder(self,pair):
        if(len(pair) == 2):
            if(cmp(pair[0],pair[1]) == 1):
                tmp = pair[0]
                pair[0] = pair[1]
                pair[1] = tmp
        return pair
    
    def confirmNoRepeat(self,first,sec):
        for curTup in self.LP:
            if((first == curTup[0][0] and sec == curTup[0][1]) or (first == curTup[0][1] and sec == curTup[0][0])): #if the pairs are the same
                return False
        return True

    def checkPairs(self,bunch):    
        counter = 1 #counter starts at one because the pair is in the 'baseline' obviously
        for words in xrange(1,len(bunch[0][0])): #for the number of words in the first line in the bunch (our 'baseline')
            counter = 1
            for line in xrange(1,len(bunch)): #for the number of lines in the bunch that we are going to be searching through
                checkingStr = ' '.join(bunch[line][0])
                my_regex = r'\b(?=\w)' + re.escape(bunch[0][0][words]) + r"\b(?!\w)"
                m = re.search(my_regex,checkingStr,re.IGNORECASE)
                if m:
                    if(cmp(bunch[0][0][0].lower(),m.group().lower()) != 0 and (bunch[0][1] != bunch[line][1]) and not(re.findall("[.!?]",bunch[0][0][0]+m.group()))):
                        if self.confirmNoRepeat(bunch[0][0][0].lower(),m.group().lower()):
                            first = bunch[0][0][0].lower()
                            sec = m.group().lower()
                            counter = counter + 1
                        else:
                            break
            if(counter > 1):
                pair = self.inOrder([first,sec]) #NOTE: alphabetizes the two words..althought this may be reduntant based off the fact that bunch was alphabetized
                tu = (tuple(pair),counter,);
                self.LP.append(tu) #add the tuple to the listPairs list
    
    def findPairs(self,lenShift):
        bunch = []
        listPairs = []
        shiftList = deepcopy(self.shiftList)
        for line in xrange(0,lenShift): #for the number of shifts
            for word in xrange(0,len(shiftList[line][0])): #for the number of words in that shift
                    shiftList[line][0][word] =re.sub("(?<=[A-Za-z])[.,:!?]","",shiftList[line][0][word]) #remove the punc
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
                    self.checkPairs(bunch) #see if there are pairs within the bunch
        self.LP.sort()    
        self.fsm.event('finishedCheckingPairs')    

    def alphabetize(self,leng):
        if(leng > 1): #if shiftList has atleast 2 tuples in it
            for y in xrange(1, leng): #insertion sort 
                word = 0
                #you should set shiftList jazz to variables so its not so long
                while(y > 0 and (word < len(self.shiftList[y-1][0]) and word < len(self.shiftList[y][0])) and (cmp(self.shiftList[y-1][0][word].lower(), self.shiftList[y][0][word].lower()) == 1 or self.shiftList[y-1][0][word].lower() == self.shiftList[y][0][word].lower()) ):
                    y1 = len(self.shiftList[y-1][0])
                    y0 = len(self.shiftList[y][0])
                    if((cmp(self.shiftList[y-1][0][word].lower(), self.shiftList[y][0][word].lower()) == 1) or (word+1 >= y0 and word+1 < y1)):
                        bigger = self.shiftList[y-1]
                        self.shiftList[y-1] = self.shiftList[y]
                        self.shiftList[y] = bigger
                        y = y - 1
                        word = 0
                    if( self.shiftList[y-1][0][word].lower() == self.shiftList[y][0][word].lower()):
                        word = word + 1
    
    def ignore(self, word):
        return re.sub("[.,:;!?]","",word)
    
    def shift(self, words):
        for i in xrange(0,(len(words))):
            if((self.ig) and self.ignore(words[0].lower()) in [x.lower() for x in self.ig]): #if ignoreWords is defined and the first word is it, skip it
                    pass
            else:
                tup = (list(words),self.lineNum)  #must be typecasted to list() otherwise will be mutated on next go around
                self.shiftList.append(tup)
            words.append(words[0])  #put the first word at the back
            words.remove(words[0])  #remove the first appearence of the first word... being the first word
    
    def beginShift(self, splitLines):
        self.fsm.event('splitWords')
        for i in xrange(0,len(self.splitLines)): #for the the number of lines
            self.lineNum = self.lineNum + 1
            splitWords = splitLines[i].split(' ')
            for x in splitWords[:]:     #remove the empty spaces due to sentences with spces after breaks like (hello there.   hi there)
                if x == '':
                    splitWords.remove(x)
            self.shift(splitWords)
        self.fsm.event('finishedShift')
    
    def addText(self,document):
        self.fsm.event('callAddText')        
        self.computeLP = True
        if(len(document) != 0): #if there are no lines
            if(self.pb == True):
                self.fsm.event('periodsToBreaks')       
                if(document[len(document)-1][0] == '.' or document[len(document)-1][0] != ' '):
                    self.fsm.event('breakingByPeriods')                                    
                    self.runningText = self.runningText + document
                    document = self.runningText
                    document = document.replace('\n', ' ')
                    self.splitLines = re.split("(?<=[a-z]\.)\s",document)
                    self.beginShift(self.splitLines)
                    self.alphabetize(len(self.shiftList))
                    self.runningText = ''
                else:
                    self.fsm.event('runningText')                
                    self.runningText = self.runningText + document
                    document = self.runningText
                
            else:
                self.fsm.event('regularBreaks')
                if(document[len(document)-1][0] == ' '):
                    self.fsm.event('runningText')                
                    self.runningText = self.runningText + document
                    document = self.runningText
                else:             
                    self.fsm.event('breakingRegularly')       
                    self.runningText = self.runningText + str(document)
                    document = self.runningText                    
                    self.splitLines = document.split('\n')
                    try:
                        self.splitLines.remove('')
                    except:
                        pass
                    self.beginShift(self.splitLines)
                    self.alphabetize(len(self.shiftList))
                    self.runningText = ''

    def index(self):
        self.fsm.event('callIndex')       
        if(self.runningText != '' and self.pb == True):
            self.fsm.event('completeRunningIndexWithP')       
            self.fsm.event('breakingByPeriods')                                    
            self.runningText = self.runningText.replace('\n', ' ')
            self.splitLines = re.split("(?<=[a-z]\.)\s",self.runningText)
            self.runningText = self.splitLines[-1]
            self.splitLines = self.splitLines[:-1]
            
            self.beginShift(self.splitLines)
            self.alphabetize(len(self.shiftList))
            
        if(self.runningText != '' and self.pb == False):
            self.fsm.event('completeRunningIndex')
            self.fsm.event('breakingRegularly')       
            self.splitLines = self.runningText.split('\n')
            self.runningText = self.splitLines[-1]
            self.splitLines = self.splitLines[:-1]
            
            self.beginShift(self.splitLines)
            self.alphabetize(len(self.shiftList))
        self.fsm.event('printingIndex')
        
        idx = []
        for i in self.shiftList:
            idx.append(i)
        return idx

    def reset(self):
        self.fsm.event('callReset')        
        self.lineNum = -1
        self.fsm.reset()
        del self.shiftList[:]
        del self.LP[:]
        self.runningText = ''

    def listPairs(self):
        self.fsm.event('callListPairs')        
        lp = []
        if(self.computeLP == True):
            self.fsm.event('completeListPairs')        
            self.findPairs(len(self.shiftList))
            self.computeLP = False
        self.fsm.event('printLP')        
        for i in self.LP:
            lp.append(i)
        return lp

# kc = Kwic(periodsToBreaks=True, ignoreWords=["the"])
# kc.addText("a. b. c ")

# kc = Kwic(ignoreWords=["the"])
# kc.addText("This is some text.\n")
# kc.addText("By the old hotel at lakeside, looking southern cross the sea.\n There's ")
# kc.addText("a bright campfire a burning and I know it burns for me.\n For the wind is in the ")

# x = kc.index()
# v = kc.listPairs()
# kc.fsm.printLog()

# kc.reset()

# kc.fsm.printLog()
# print

# kc = Kwic(periodsToBreaks=True, ignoreWords=["the"])
# kc.addText("This is some text.")
# kc.addText("By the old hotel at lakeside, looking southern cross the sea. There's ")
# kc.addText("a bright campfire a burning and I know it burns for me. For the wind is in the ")
# kc.fsm.printLog()

# # for i in x:
#     print(i)