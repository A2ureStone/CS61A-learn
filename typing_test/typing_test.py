""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    file = open(path,mode='r')
    result = readlines(file)
    close(file)
    def clear(line):
        j = 0
        while (line[j] == ' ') | (line[j] == '\n') | (line[j] == '\t'):
            if j == len(line) - 1:
                break
            j += 1
        k = len(line) - 1
        while (line[k] == ' ') | (line[k] == '\n') | (line[k] == '\t'):
            if k == 0:
                break
            k -= 1
        temp = line[j:k + 1]
        if (temp == ' ') | (temp == '\t') | (temp == '\n'):
            temp = ''
        return temp
    i=0
    for i in range(0,len(result)):
        result[i]=clear(result[i])
        i+=1
    return result

def new_sample(path,i):
    file = open(path, mode='r')
    for j in range(0,i+1):
        result=readline(file)
    def clear(line):
        j = 0
        while (line[j] == ' ') | (line[j] == '\n') | (line[j] == '\t'):
            if j == len(line) - 1:
                break
            j += 1
        k = len(line) - 1
        while (line[k] == ' ') | (line[k] == '\n') | (line[k] == '\t'):
            if k == 0:
                break
            k -= 1
        temp = line[j:k + 1]
        if (temp == ' ') | (temp == '\t') | (temp == '\n'):
            temp = ''
        return temp
    close(file)
    return clear(result)

def analyze(sample_paragraph, typed_string, start_time, end_time):
    def word_speed(typed_string,start_time,end_time):
        valid_lenth=len(typed_string)/5
        return valid_lenth/(end_time - start_time)*60
    def accuracy(sample_paragraph,typed_string):
        sample = split(sample_paragraph)
        typed = split(typed_string)
        count=0
        if len(typed)<len(sample):
            for i in range(0,len(typed)):
                if sample[i] == typed[i]:
                    count+=1
        else:
            for i in range(0,len(sample)):
                if sample[i] == typed[i]:
                    count+=1
        if len(typed) == 0:
            return float(0)
        return count/min( len(sample) , len(typed) )
    return [  word_speed(typed_string ,start_time,end_time),  100*accuracy(sample_paragraph,typed_string) ]

def pig_latin(word):
    """
    >>> pig_latin('dog')
    'ogday'
    >>> pig_latin('brush')
    'ushbray'
    >>> pig_latin('elephant')
    'elephantway'
    >>> pig_latin('nth')
    'nthay'
    """
    vowels = ['a','e','i','o','u']
    countvowels=0
    def isvovels(w):
        for i in vowels:
            if w == i:
                return True
        return False
    i=0
    if isvovels(word[0]):
        return word + 'way'
    while not isvovels( word[i] ):
        if i == len(word)-1:
            i+=1
            break
        i+=1
    return word[i:len(word)]+word[0:i]+'ay'

def autocorrect(user_input,words_list,score_function):
    if user_input in words_list:
        return user_input
    score = score_function(user_input,words_list[0])
    correct_string = words_list[0]
    for i in range(0,len(words_list)):
        if score_function(user_input , words_list[i] ) < score:
            score = score_function(user_input , words_list[i] )
            correct_string = words_list[i]
    return correct_string

def swap_score(str1,str2):
    """"
    count = 0
    for i in range(0, min(len(str1) , len(str2) )):
        if str1[i] != str2[i]:
            count+=1
    return count
    """
    if str1 == str2:
        return 0
    end = min(len(str1), len(str2))
    if str1[0] == str2[0]:
        return swap_score(str1[1:end], str2[1:end])
    return 1+ swap_score(str1[1:end],str2[1:end])
# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == word2: # Fill in the condition
        # BEGIN Q6
        return 0
        # END Q6

    elif (len(word1) == 0) | (len(word2) == 0): # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        if not len(word1):
            return len(word2)
        if not len(word2):
            return len(word1)
        # END Q6
    else:
        "*** YOUR CODE HERE ***"
    if word1[0] != word2[0]:
        val1 = 1 + score_function(word1[1:], word2)
        val2 = 1 + score_function(word1, word2[1:])
        val3 = 1 + score_function(word1[1:], word2[1:])
        return min(val3, val2, val1)
    return score_function(word1[1:], word2[1:])

        # END Q6



KEY_DISTANCES = get_key_distances()

get_key_distances()
# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1,word2):
    if word1 == word2:  # Fill in the condition
        # BEGIN Q6
        return 0
        # END Q6

    elif (len(word1) == 0) | (len(word2) == 0):  # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        if not len(word1):
            return len(word2)
        if not len(word2):
            return len(word1)
        # END Q6
    else:
        "*** YOUR CODE HERE ***"
    if word1[0] != word2[0]:

        val1 = 1 + score_function_accurate(word1[1:], word2)
        val2 = 1 + score_function_accurate(word1, word2[1:])
        val3 = KEY_DISTANCES[word1[0],word2[0]] + score_function_accurate(word1[1:], word2[1:])
        return min(val3, val2, val1)
    return score_function_accurate(word1[1:], word2[1:])

memory = {}

def score_function_final(word1,word2):
    if word1 == word2:  # Fill in the condition
        # BEGIN Q6
        return 0
        # END Q6
    elif (len(word1) == 0) | (len(word2) == 0):  # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        if not len(word1):
            return len(word2)
        if not len(word2):
            return len(word1)
        # END Q6
    else:
        "*** YOUR CODE HERE ***"
    if word1[0] != word2[0]:
        if (word1[1:] + ',' + word2) in memory:
            val1 = 1 + memory[word1[1:] + ',' + word2]
        else:
            memory[word1[1:]+','+word2] = score_function_final(word1[1:], word2)
            memory[word2 + ',' + word1[1:]] = memory[word1[1:]+','+word2]
            val1 = 1 + memory[word1[1:]+','+word2]
        if (word1 + ',' + word2[1:]) in memory:
            val2 = 1 + memory[word1 + ',' + word2[1:]]
        else:
            memory[word1+','+word2[1:]] = score_function_final(word1, word2[1:])
            memory[word2[1:] + ',' + word1] = memory[word1+','+word2[1:]]
            val2 = 1 + memory[word1+','+word2[1:]]
        if (word1[1:] + ',' + word2[1:]) in memory:
            val3 = KEY_DISTANCES[word1[0],word2[0]] + memory[word1[1:] + ',' + word2[1:]]
        else:
            memory[word1[1:] + ',' + word2[1:]] = score_function_final(word1[1:], word2[1:])
            memory[word2[1:] + ',' + word1[1:]] = memory[word1[1:] + ',' + word2[1:]]
            val3 = KEY_DISTANCES[word1[0],word2[0]] + memory[word1[1:] + ',' + word2[1:]]
        return min(val3, val2, val1)
    else:
        if (word1[1:] + ',' + word2[1:]) in memory:
            return memory[word1[1:] + ',' + word2[1:]]
        else:
            memory[word1[1:] + ',' + word2[1:]] = score_function_final(word1[1:], word2[1:])
            memory[word2[1:] + ',' + word1[1:]] = memory[word1[1:] + ',' + word2[1:]]
            return memory[word1[1:] + ',' + word2[1:]]

# END Q7-8

