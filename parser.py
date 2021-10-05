import json

validChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
testDict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'nine' : 9,
    'twenty' : 20,
    'fifteen' : 15
}


class Parser:
    def listifyMe(txt):
        return [x for x in txt]

    def replaceBreaks(list):
        cleanPass = False
        while cleanPass == False:
            for x in list:
                if x == '\n':
                    print('Replacing line break')
                    list[list.index(x)] = ' '
                else:
                    cleanPass = True
        return list

    def removePunct(list, checkChar, validChar):
        cleanPass = False
        while cleanPass == False:
            if checkChar.lower() not in validChar:
                try: 
                    list.remove(checkChar)
                    print('removing ' + checkChar)
                except:
                    print('no more checkChar in list')
                    break
            else:
                cleanPass = True
        return list
    
    
    def depunctuateMe(list, validChar):
        list = Parser.replaceBreaks(list)
        for x in list:
            print('x is ' + x)
            list = Parser.removePunct(list, x, validChar)
        return list


    def concatMe(list):
        reString = ''
        for x in list:
            reString += list[list.index(x)]
        return reString
    
    def parseList(listifiedTxt):
        wordList = []
        for x in listifiedTxt:
            if x == ' ':
                concatWord = Parser.concatMe(listifiedTxt[0:listifiedTxt.index(x)])
                wordList.append(concatWord)
                print('appending ' + concatWord + ' to wordlist')
                listifiedTxt = listifiedTxt[listifiedTxt.index(x)+1:len(listifiedTxt)]
        wordList.append(Parser.concatMe(listifiedTxt))
        return wordList

    def fullParse(txt):
        txtList = Parser.listifyMe(txt)
        depunctList = Parser.depunctuateMe(txtList, validChar)
        wordList = Parser.parseList(depunctList)
        print(wordList)
        return wordList

class Codex:
    def __init__(self, wordDict):
        self.wordDict = wordDict
    
    def zipfCount(list):
        counter = 0
        firstWord = list[0]
        for word in list:
            if firstWord.lower() == word.lower():
                counter += 1
        return firstWord, counter

    def sortDict(dict):
        newDict= {}
        passNo = 0
        while dict != {}:
            passNo = 0
            greatestValue = 0
            greatestKey = ''
            print('This is pass number ' +str(passNo) + ' out of' + str(len(dict)))
            for key in dict.keys():
                if dict[key] > greatestValue:
                    greatestValue = dict[key]
                    greatestKey = key
            newDict[greatestKey] = greatestValue
            del dict[greatestKey]
            passNo += 1
        print('Finished in ' + str(passNo) + ' passes')
        return newDict
            
    def dictify(list):
        returnDict = {}
        while len(list) > 0:
            dictWord, dictCounter = Codex.zipfCount(list)
            dictWord = dictWord.lower()
            returnDict[dictWord] = dictCounter
            for word in list:
                if word.lower() == dictWord:
                    list.remove(word)
        return returnDict
    

def main():
    try:
        bigTxt = open('androids.txt','r', encoding='ascii', errors='ignore')
        bigTxt = bigTxt.read()
    except:
        print('Unicode crap')

    parsedList = Parser.fullParse(bigTxt)
     
    countThis = Codex.dictify(parsedList)
    sortThis = Codex.sortDict(countThis)
    print(sortThis)

    with open('data.txt', 'w') as outfile:
        json.dump(sortThis, outfile)

def debug():

    sorted = Codex.sortDict(testDict)

main()

# debug()

