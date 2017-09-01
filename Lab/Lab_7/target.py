
from random import choice, sample
from collections import defaultdict

class Target:
    '''
    Generates a target, that is, a 3 x 3 grid of distinct letters
    such that at least one 9-letter word is made from all letters in the target.
    The aim of the puzzle is to find words consisting of distinct letters all in the target,
    one of which has to be the letter at the centre of the target.

    To create a target object, three keyword only arguments can be provided:
    - dictionary, meant to be the file name of a dictionary storing all valid words,
      with a default value named dictionary.txt, for a default dictionary supposed to be stored
      in the working directory;
    - target, with a default value of None, otherwise meant to be a 9-letter string defining
      a valid target (in case it is not valid, it will be ignored and a random target will be
      generated as if that argument had not been provided);
    - minimal_length, for the minimal length of words to discover, with a default value of 4.
    '''
    def __init__(self, *, dictionary = 'dictionary.txt', target = None, minimal_length = 4):
        if target:
            self.target = target
            self.length = minimal_length
            self.file = dictionary
            self._dic = defaultdict(list)
            self.flag = False
        else:
            A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.target = sample(A, 9)
            self.length = minimal_length
            self.file = dictionary
            self._dic = defaultdict(list)
            self.flag = True
        

    def __str__(self):
        target = ''
        for i in range(9):
            if i % 3 == 0:
                target += f'\n       ___________\n\n      | {self.target[i]} |'
            else:
                target += f' {self.target[i]} |'
        target += '\n       ___________\n'
        return target
        

        
    def __repr__(self):
        if self.flag:
            return (f'Target(dictionary = dictionary.txt, minimal_length = {self.length})')
        else:
            return (f'Target(dictionary = dictionary.txt, target = {self.target}, '
                   f'minimal_length = {self.length})')

       
    def number_of_solutions(self):
        T = self.target
        file_name = self.file
        with open(file_name) as file:
            for line in file:
                word = line.strip()
                if len(word) < self.length:
                    continue
                if len(word) != len(set(word)):
                    continue
                if (set(word).issubset(set(T)) or set(word) == set(T)) and self.target[4] in word:
                    self._dic[len(word)].append(word)
        
        print(f'In decreasing order of length between 9 and {self.length}:')
        for i in sorted(self._dic, reverse = True):
            print('    ', end = '')
            if len(self._dic[i]) == 1:
                print(f'l solution of length {i}')
            else:
                print(f'{len(self._dic[i])} solutions of length {i}')
        self._dic.clear()
        
    def give_solutions(self, minimal_length = None):
        '''
        By default, all solutions are displayed, unless minimal_length is passed as an argument,
        in which case only solutions of length at least that value are displayed.
        '''

        T = self.target
        file_name = self.file
        with open(file_name) as file:
            for line in file:
                word = line.strip()
                if len(word) < self.length:
                    continue
                if len(word) != len(set(word)):
                    continue
                if (set(word).issubset(set(T)) or set(word) == set(T)) and self.target[4] in word:
                    self._dic[len(word)].append(word)
    
        if minimal_length == None:
            for i in sorted(self._dic, reverse = True):
                if i != 9:
                    print()
                if len(self._dic[i]) == 1:
                    print(f'Solution of length {i}:')
                    print('    ',end = '')
                    print(self._dic[i][0])
                else:
                    print(f'Solutions of length {i}:')
                    for j in self._dic[i]:
                        print(f'    {j}')

        else:
            for i in sorted(self._dic, reverse = True):
                if i < minimal_length:
                    break
                if i != 9:
                    print()
                if len(self._dic[i]) == 1:
                    print(f'Solution of length {i}:')
                    print('    ',end = '')
                    print(self._dic[i][0])
                else:
                    print(f'Solutions of length {i}:')
                    for j in self._dic[i]:
                        print(f'    {j}')
                       
        self._dic.clear()



    def change_target(self, to_be_replaced, to_replace):
        '''
        Both arguments are meant to be strings.
        The target will be modified if:
        - to_be_replaced and to_replace are different strings of the same length;
        - all letters in to_be_replaced are distinct and occur in the current target;
        - replacing each letter in to_be_replaced by the corresponding letter in to_replace
          yields a valid target.
        If those conditions are not satisfied then the method prints out a message indicating
        that the target was not changed.
        If the target was changed but consists of the same letters, and with the same letter
        at the centre, then the method prints out a message indicating that the solutions
        are not changed.
        '''
        dic = {}
        for i in range(len(to_be_replaced)):
            dic[to_be_replaced[i]] = to_replace[i]

        T = self.target
        if len(set(to_be_replaced)) != len(to_be_replaced):
            print('The target was not changed.')
        elif not(set(to_be_replaced).issubset(set(T)) or set(to_be_replaced) == set(T)):
            print('The target was not changed.')
        elif to_be_replaced == to_replace:
            print('The target was not changed.')
        elif len(set(to_be_replaced)) != len(set(to_replace)):
            print('The target was not changed.')
        else:
            L = list(self.target)
            for i in range(len(L)):
                if L[i] in to_be_replaced:
                    L[i] = dic[L[i]]
            self.target = ''.join(L)
            if not self._is_value_target(self.target):
                self.target = T
                print('The target was not changed.')
            else:
                if set(T) == set(self.target) and T[4] == self.target[4]:
                    print('The solutions are not changed.')

        self._dic.clear()
    def _is_value_target(self, target):
        T = target
      
        file_name = self.file
        with open(file_name) as file:
            for line in file:
                word = line.strip()
                if len(word) < self.length:
                    continue
                if len(word) != len(set(word)):
                    continue
                if (set(word).issubset(set(T)) or set(word) == set(T)) and T[4] in word:
                    if len(word) == 9:
                        self._dic.clear()
                        return True
        self._dic.clear()
        return False
