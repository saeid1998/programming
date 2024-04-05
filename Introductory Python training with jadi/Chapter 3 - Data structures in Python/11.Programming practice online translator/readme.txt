Artadekht is preparing an online translator for his university thesis. The online translator that Artadekht is preparing has a dictionary and at the end this translator must translate a sentence.

In the first line of the input, there is a number n, which represents the number of words in the dictionary. Each of the next n lines contains two words, which shows that the second word is the meaning of the first word. The next line contains a sentence. A sentence consists of several words separated by a space. Now you have to help Artadekht and write a translator that reads the dictionary and the relevant sentence from the input and translates the sentence. In the translation process, if there is no word in the dictionary, print the word itself in the output. See sample input and sample output for more information.

Note: The online arbitration system uses Python 3.4, in this version the dictionaries do not remember the order of entering information and may not achieve the desired result if they are sorted, to solve this problem, use OrderedDict instead of dict. You can import this data structure from the collections library in the program.

Sample input:

5
hello salam
Goodbye Khodafez
say goftan
we ma
you shoma
we say goodbye to you tonight

Sample output:

ma goftan khodafez to shoma tonight