# wordleStats
Some analysis on best starting word for the viral webgame [Wordle](https://www.powerlanguage.co.uk/wordle/)

calculates the frequency of each letter for all the possible five letter words, then finds the word whose letters's freqency has the highest sum

The dictionary used for Wordle is not public, so I have used the [Standford Graphbase five-letter words list](https://www-cs-faculty.stanford.edu/~knuth/sgb.html) as my dictionary

## Results 

Best words:
```
[word, score]
['arose', 12215]
['raise', 11892]
['arise', 11892]
['aloes', 11891]
['stoae', 11890]
['laser', 11886]
['earls', 11886]
['reals', 11886]
['tears', 11885]
['rates', 11885]
['stare', 11885]
['aster', 11885]
['tares', 11885]
['snare', 11585]
['earns', 11585]
['nears', 11585]
['saner', 11585]
['nares', 11585]
['aisle', 11568]
['least', 11561]
```

Most common letters:
```
[letter, occurences]
A :  2348
B :  715
C :  964
D :  1181
E :  3009
F :  561
G :  679
H :  814
I :  1592
J :  89
K :  596
L :  1586
M :  843
N :  1285
O :  1915
P :  955
Q :  53
R :  1910
S :  3033
T :  1585
U :  1089
V :  318
W :  505
X :  139
Y :  886
Z :  135
```

Most common letters SORTED:
```
[letter, occurences]
S :  3033
E :  3009
A :  2348
O :  1915
R :  1910
I :  1592
L :  1586
T :  1585
N :  1285
D :  1181
U :  1089
C :  964
P :  955
Y :  886
M :  843
H :  814
B :  715
G :  679
K :  596
F :  561
W :  505
V :  318
X :  139
Z :  135
J :  89
Q :  53
```

## Chart

![Occurences vs  Letter](https://user-images.githubusercontent.com/63263642/147895752-fc57e04f-99a9-42e2-9d37-a0274490d09f.png)
