#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/10
#
#Purpose:       The purpose of this is to write a complete python program
#               that is given a list of words and finds the anagrams formed by the words.

from time import ctime

def displayTerminationMessage():
    print(f"""
Programmed by Farjad Tariq
Date: {ctime()}
End of processing.\n""")

def getWords(filename):
    """ filename -> list of words from the file / document
        Given the name of a file return a list of words from
        the file."""
    # filename - the name of the file containing the words
    # infile - the file descriptor
    # data - the content of the file as one string
    infile = open(filename, 'r')
    data = infile.read()
    infile.close()
    return data.split()

def sortLettersInWord(word): 
    #word = word from list of words
    return ''.join(sorted(word)) 

def buildSortedWordsList(words):
    #sortedWords = list of sorted words
    #word = word from list of words
    #words = list of words
    #sWord = sorted word in list of sorted words
    sortedWords = []
    for word in words:
        sWord=sortLettersInWord(word)
        sortedWords.append(sWord)
    return sortedWords

def buildAnagramLists(words, sortedWords):
    #unique = list of unique words
    #anagrams = list of anagrams
    #word = word from list of words
    #sortedWord = sorted word in list of sorted words
    unique = []
    anagrams = []
    for word, sortedWord in zip(words, sortedWords):
        if sortedWord not in unique:
            unique.append(sortedWord)
            anagrams.append([word])
        else:
            anagrams[unique.index(sortedWord)].append(word)
    return unique, anagrams

def displayAnagrams(uniqueSortedWords, anagramWordLists): 
    #unique = list of unique words
    #anagrams = list of anagrams
    #an = word in anagrams
    print('\n%-10s %s' % ('Letters','Words'))

    for unique, anagrams in zip (uniqueSortedWords, anagramWordLists):
        print('%-10s' % unique, end=' ')
        for an in anagrams:
            print('%s' % an, end=' ')
        print()

def main():
    print('\n' + '-' * 80)
    #filename = the name of file containing the words
    #words = list of words
    #sortedWords = list of sorted words
    #unique = list of unique words
    #anagrams = list of anagrams
    filename = input('Enter the name of the file containing the words: ').strip()
    words = getWords(filename)
    sortedWords = buildSortedWordsList(words)
    unique, anagrams = buildAnagramLists(words, sortedWords)
    displayAnagrams(unique, anagrams)
    displayTerminationMessage()

main()