from collections import defaultdict, deque
import sys

dictionary_file = 'dictionary.txt'
def get_all_poss():
    lexicon = set()
    slots_list = defaultdict(list)
    with open(dictionary_file) as dictionary:
        for word in dictionary:
            word = word.rstrip()
            lexicon.add(word)
            for i in range(len(word)):
                slots_list[word[: i], word[i + 1: ]].append(word)

    closest_words = defaultdict(set)
    for slot in slots_list:
        for i in range(len(slots_list[slot])):
            for j in range(i + 1, len(slots_list[slot])):
                closest_words[slots_list[slot][i]].add(slots_list[slot][j])
                closest_words[slots_list[slot][j]].add(slots_list[slot][i])
    return lexicon, closest_words

def word_ladder(word_1, word_2):
    lexicon, closest_words = get_all_poss()
    if len(word_1) != len(word_2):
        return
    word_1 = word_1.upper()
    word_2 = word_2.upper()
    if word_1 not in lexicon or word_2 not in lexicon:
        return
    if word_1 == word_2:
        return [[word_1]]
    solutions = []
    queue = deque([[word_1]])
    while queue:
        word_sequence = queue.pop()
        last_word = word_sequence[-1]
        for word in closest_words[last_word]:
            if word == word_2:
                if not solutions or len(solutions[-1]) > len(word_sequence):
                    solutions.append(word_sequence + [word])
            if not solutions and word not in word_sequence:
                queue.appendleft(word_sequence + [word])
    return solutions
                
    
                
    
