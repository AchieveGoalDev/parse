testString = "Thi&s is a string to be parsed. Parse me. The next sentence will have lots of goobledygoo and line breaks. %12 \n har&rowing P.light of d-u-p-lica-ti-on"

class Parse:
    def __init__(self, textString):
        self.textString = textString
        self.VALIDCHAR = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
        self.CLIP_TERMINATORS = [' ', '\n' ]
        self.clip = []
        self.stringTerm = False #Indicates whether or not a scanned string of text has terminated
        self.clipIndex = 0 #Indicates the index of the current string being scanned
        self.clipList = []

    def __repr__(self):
        me =str(self.clip) + '\n' + str(self.stringTerm) + '\n' + str(self.clipIndex) + '\n' + str(self.clipList)
        return me

    def clipString(self): #Clip a lexical unit of a string of text to terminate at any value defined in Parse.CLIP_TERMINATORS 
        self.stringTerm = False
        self.clip = []
        for char in self.textString[self.clipIndex:]:
            self.clipIndex += 1
            print('Checking Truthiness - ' + str(self.clipIndex) + ' >=' + str(len(self.textString)))
            if self.clipIndex > len(self.textString): #Indicates whether the index value has exceeded the length of the input string and triggers clipping termination if it has
                self.stringTerm = True
                print('Evaluated True')
                break
            elif char in self.CLIP_TERMINATORS:
                break
                print('terminating')
            else:
                self.clip.append(char)
                print('appending ' + char)

    def cleanString(self):
        cleanClip = ''
        for char in self.clip:
            if char.lower() not in self.VALIDCHAR:
                del self.clip[self.clip.index(char)]
        for char in self.clip:
            cleanClip += char
        self.clipList.append(cleanClip)
        return cleanClip

class Analyze:
    pass

class Corpus:
    def __init__(self, textList = [], freqDist =[], set=()):
        self.textList = textList,
        self.freqDist = freqDist,
        self.lexSet = lexSet 


longstring = Parse(testString)
longstring.clipString()
longstring.cleanString()
# def dataSort(clip, freqDist):
#     if freqDist['clip']:
#         freqDist['clip'] += 1
#     else freqDist['clip'] = 1
#     return freqDist


# clip = clipString(testString, 0)
# print(clip)
# clip = trimClip(clip['clip'], validChar)
# print(clip)