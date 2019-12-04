def countSigns(index, inputString, counter, sign):
    #check na zakres
    if index + 1 < inputString.__len__():
        if inputString[index + 1] == sign:
            return countSigns(index + 1, inputString, counter + 1, sign)
        else:
            if counter == 2 and sign == '.':
                return inputString
            return sliceString(inputString, index - counter, index)
    else:
        return inputString

def sliceString(inputString, start, end):
    return inputString[:start] + inputString[end:]

def text_analyer(filePath):
    try:
        with open (filePath, 'r+') as fileHandler:
            linesList = fileHandler.readlines()
            output = ["\n"]
            for line in linesList:
                letterIndex = 0
                changesCount = 0
                while letterIndex < line.__len__():
                    if line[letterIndex] == '.':
                        if line.__len__() > 1 and line[letterIndex-1] != '.':
                            line = countSigns(letterIndex, line, 0, '.')
                            changesCount += 1
                        if line.__len__() > 1 and line[letterIndex - 1] == ' ':
                                line = sliceString(line, letterIndex - 1, letterIndex)
                                changesCount += 1
                        if (letterIndex + 1) < line.__len__() and line[letterIndex + 1] != ' ':
                            line =line[:letterIndex] + ' ' + line[letterIndex:]
                            changesCount += 1
                    elif line[letterIndex] == ',':
                        line = countSigns(letterIndex, line, 0, ',')
                        changesCount += 1
                        if line.__len__() > 1 and line[letterIndex - 1] == ' ':
                                line = sliceString(line, letterIndex - 1, letterIndex)
                                changesCount += 1
                        if (letterIndex + 1) < line.__len__() and line[letterIndex + 1] != ' ':
                            line =line[:letterIndex] + ' ' + line[letterIndex:]
                            changesCount += 1
                    elif line[letterIndex] == ' ':
                        line = countSigns(letterIndex, line, 0, ' ')
                        changesCount += 1
                    letterIndex += 1
                output.append(line)
            fileHandler.writelines(output)
    except FileNotFoundError:
        print("Wrong file path")


text_analyer("inputfile.txt")






