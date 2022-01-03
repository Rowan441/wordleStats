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

    BEST_N_WORDS = 15

    print("Best", BEST_N_WORDS, "words:")
    for i in range(min(BEST_N_WORDS, len(lines))):
        print(linesWeight[i])

    print("\nBest word without an S")
    i = 0
    while True:
        if linesWeight[i][0].find("s") == -1:
            print(linesWeight[i])
            break
        if i == len(lines)-1:
            print("None found")
            break
        i += 1
        

    letterFreq.sort(key=takeSecond, reverse=True)

    print("\nMost common letters:")
    for i, freq in enumerate(letterFreq):
        print(freq[0], ": ", freq[1]) 
