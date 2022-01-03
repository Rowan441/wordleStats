def takeSecond(elem):
    return elem[1]

with open('5letterwords.txt') as f:
    lines = f.readlines()

    letterFreq = [[chr(ord('@')+i+1), 0] for i in range(26)]

    for line in lines:
        line = line.strip()

        for letter in line:
            index = ord(letter) - 97
            letterFreq[index][1] += 1


    linesWeight = lines.copy()
                
    for i, line in enumerate(lines):
        line = line.strip()
        score = 0

        for j, letter in enumerate(line):
            if line.find(letter) < j:
                continue
            index = ord(letter) - 97
            score += letterFreq[index][1]

        linesWeight[i] = [line, score]
    
    linesWeight.sort(key=takeSecond, reverse=True)

    print("Best words:")
    for i in range(min(10, len(lines))):
        print(linesWeight[i])

    print("most common letters:")
    for i, freq in enumerate(letterFreq):
        print(chr(ord('@')+i+1), ": ", freq[1])

    letterFreq.sort(key=takeSecond, reverse=True)

    print("most common letters SORTED:")
    for i, freq in enumerate(letterFreq):
        print(freq[0], ": ", freq[1]) 



