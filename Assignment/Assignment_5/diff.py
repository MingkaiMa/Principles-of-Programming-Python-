##Written by Mingkai Ma, reference from Eric Martin's levenshtein_distance.py from Lecture_7
##Special thanks to Dr.Martin

import os.path
import sys
import os
import re
from collections import defaultdict
class DiffCommands:
    def __init__(self, file_name = ''):
        self.file = file_name
        self.dic = {}
        self.d_left = []
        self.a_right = []
        self.c_left = []
        self.c_right = []
        if not self._meet_condition(file_name):
            raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')


    def _meet_condition(self, filename):
        List_left = []
        List_right = []
        dic_left = {}
        dic_right = {}
        T = []
        if not os.path.isfile(filename):
            T = filename.split('\n')
            if not T[0]:
                return True
        else:
            with open(filename) as file:
                for line in file:
                    T.append(line.strip('\n'))

        for line in T:
            if ' ' in line:
                return False
            if line.strip() == '':
                return False
            for word in line:
                if word.isupper():
                    
                    return False
            if any(not (c.isdigit() or c in ',dac') for c in line.strip('\n')):
                return False

            if sum(c.isalpha() for c in line) != 1:
                return False

            re_match = re.compile(r'^(\d+)(,\d+)?[acd](\d+)(,\d+)?$')
            if not re_match.match(line):
                return False
                
            
            if 'd' in line:
                s_left = line[:line.index('d')]
                s_right = line[line.index('d') + 1:]
                list_left = s_left.split(',')
                list_right = s_right.split(',')
                d_left = [int(i) for i in list_left]
                d_right = [int(i) for i in list_right]
                

                if len(d_right) != 1:
                    return False
                if len(d_left) != 1 and len(d_left) != 2:
                    return False

                
                
                if len(d_left) == 2:
                    dic_left[d_left[0] - 1] = d_right[0]
                    dic_left[d_left[1] + 1] = d_right[0] + 1
                    self.d_left += [i for i in range(d_left[0], d_left[1] + 1)]
                if len(d_left) == 1:
                    dic_left[d_left[0] - 1] = d_right[0]
                    dic_left[d_left[0] + 1] = d_right[0] + 1
                    self.d_left += d_left

            if 'a' in line:
                
                s_left = line[:line.index('a')]
                s_right = line[line.index('a') + 1:]
                list_left = s_left.split(',')
                list_right = s_right.split(',')
                a_left = [int(i) for i in list_left]
                a_right = [int(i) for i in list_right]
                

                if len(a_left) != 1:
                    return False
                if len(a_right) != 1 and len(a_right) != 2:
                    return False
            

                if len(a_right) == 2:
                    dic_left[a_left[0]] = a_right[0] - 1
                    dic_left[a_left[0] + 1] = a_right[1] + 1
                    self.a_right += [i for i in range(a_right[0], a_right[1] + 1)]
                if len(a_right) == 1:
                    dic_left[a_left[0]] = a_right[0] - 1
                    dic_left[a_left[0] + 1] = a_right[0] + 1
                    self.a_right += a_right

            if 'c' in line:
                s_left = line[:line.index('c')]
                s_right = line[line.index('c') + 1:]
                list_left = s_left.split(',')
                list_right = s_right.split(',')
                c_left = [int(i) for i in list_left]
                c_right = [int(i) for i in list_right]
         

                if len(c_left) != 1 and len(c_left) != 2:
                    return False
                if len(c_right) != 1 and len(c_right) != 2:
                    return False

                if len(c_left) == 2 and len(c_right) == 2:
                    dic_left[c_left[0] - 1] = c_right[0] - 1
                    dic_left[c_left[1] + 1] = c_right[1] + 1
                    self.c_left += [i for i in range(c_left[0], c_left[1] + 1)]
                    self.c_right += [i for i in range(c_right[0], c_right[1] + 1)]

                if len(c_left) == 1 and len(c_right) == 1:
                    dic_left[c_left[0] - 1] = c_right[0] - 1
                    dic_left[c_left[0] + 1] = c_right[0] + 1
                    self.c_left += c_left
                    self.c_right += c_right

                if len(c_left) == 1 and len(c_right) == 2:
                    dic_left[c_left[0] - 1] = c_right[0] - 1
                    dic_left[c_left[0] + 1] = c_right[1] + 1
                    self.c_left += c_left
                    self.c_right += [i for i in range(c_right[0], c_right[1] + 1)]

                if len(c_left) == 2 and len(c_right) == 1:
                    dic_left[c_left[0] - 1] = c_right[0] - 1
                    dic_left[c_left[1] + 1] = c_right[0] + 1
                    self.c_left += [i for i in range(c_left[0], c_left[1] + 1)]
                    self.c_right += c_right

        if 0 in dic_left:
            if dic_left[0] != 0:
                return False
        T = []
        for i in dic_left:
            T.append(dic_left[i])

        t = set(T)
        if len(t) != len(T):
            return False

        self.dic = dic_left
        
        return True

    def __str__(self):
        if not os.path.isfile(self.file):
            return self.file
        else:
            s = ''
            file = self.file
            with open(file) as f:
                for line in f:
                    s = s + line
            s = s.strip('\n')
            return s
    


    def output_diff_aid(self):
        if not os.path.isfile(self.file):
            return self.file.split('\n')
        else:
            L = []
            file = self.file
            with open(file) as f:
                for line in f:
                    L.append(line.strip('\n'))
            return L
        
                    
class DiffCommandsError(Exception):
    def __init__(self, message):
        self.message = message


class OriginalNewFiles:
    def __init__(self, word_1, word_2, insertion_cost = 1, deletion_cost = 1, substitution_cost = 2):
        L1 = []
        L2 = []
        with open(word_1) as file1:
            for line in file1:
                L1.append(line.strip('\n'))
        with open(word_2) as file2:
            for line in file2:
                L2.append(line.strip('\n'))
                
            
        self.word_1 = L1
        self.word_2 = L2
        self.word_1_length = len(L1)
        self.word_2_length = len(L2)
        self.insertion_cost = insertion_cost
        self.deletion_cost = deletion_cost
        self.substitution_cost = substitution_cost
        self._table = self._get_distances_and_backtraces_table()
        self._backtraces = [[self._table[i][j][1]
                                  for j in range(self.word_2_length + 1)]
                                       for i in range(self.word_1_length + 1)]
        self.aligned_pairs = self.get_aligned_pairs()
        
    def _get_distances_and_backtraces_table(self):
        N_1 = self.word_1_length + 1
        N_2 = self.word_2_length + 1
        d = {'H' : 0, 'V' : 0, 'D' : 0}
        table = [[[0, []] for j in range(N_2)] for i in range(N_1)]
        for i in range(1, N_1):
            table[i][0] = [i, ['H']]
        for j in range(1, N_2):
            table[0][j] = [j, ['V']]
        for i in range(1, N_1):
            for j in range(1, N_2):
                d['H'] = table[i - 1][j][0] + self.deletion_cost
                d['V'] = table[i][j - 1][0] + self.insertion_cost
                if self.word_1[i - 1] == self.word_2[j - 1]:
                    d['D'] = table[i - 1][j - 1][0]
                else:
                    d['D'] = table[i - 1][j - 1][0] + self.substitution_cost
                distances_and_directions = sorted((d[x], x) for x in d)
                table[i][j][0] = distances_and_directions[0][0]
                table[i][j][1].append(distances_and_directions[0][1])
                if distances_and_directions[1][0] == distances_and_directions[0][0]:
                    table[i][j][1].append(distances_and_directions[1][1])
                    if distances_and_directions[2][0] == distances_and_directions[1][0]:
                        table[i][j][1].append(distances_and_directions[2][1])
        return table
    
    def _compute_alignments(self, i, j, entwined_aligned_pairs):
        if i == j == 0:
            return entwined_aligned_pairs
        deletion_pairs = []
        insertion_pairs = []
        substitution_pairs = []
        for direction in self._backtraces[i][j]:
            if direction == 'H':
                deletion_pairs = [pair + str(i) + ',' + '*,' for pair in entwined_aligned_pairs]
                deletion_pairs = self._compute_alignments(i - 1, j, deletion_pairs)
            elif direction == 'V':
                insertion_pairs = [pair + '*,' + str(j) + ',' for pair in entwined_aligned_pairs]
                insertion_pairs = self._compute_alignments(i, j - 1, insertion_pairs)
            else:
                substitution_pairs = [pair + str(i) + ',' + str(j) + ','
                                                               for pair in entwined_aligned_pairs]
                
                substitution_pairs = self._compute_alignments(i - 1, j - 1, substitution_pairs)

        return deletion_pairs + insertion_pairs + substitution_pairs
        
    def get_aligned_pairs(self):
        entwined_aligned_pairs = self._compute_alignments(self.word_1_length,
                                                          self.word_2_length,
                                                          [''])

        aligned_pairs = []
        for pair in entwined_aligned_pairs:
            b = pair.strip(',')
            c = b.split(',')
            n = len(c) // 2 - 1
            word_1_index = [c[2 * i] for i in range(n, -1, -1)]
            word_2_index = [c[2 * i + 1] for i in range(n, -1, -1)]
            aligned_pairs.append((word_1_index, word_2_index))
        return aligned_pairs

    def get_all_diff_commands(self):
        L = []
        for pair in self.aligned_pairs:
            s = self.get_diff(pair)
            if s not in L:
                L.append(s)
            else:
                continue
        T = sorted(L)
        R = []
        for i in T:
            c_class = DiffCommands(i)
            R.append(c_class)
        return R
            

    def get_diff(self, pair):
        word1 = self.word_1
        word2 = self.word_2
        a= pair
        word_1 = a[0]
        word_2 = a[1]
        delete_list = []
        match_list = []
        match_index_list = []
        leap = []
        add_dic = defaultdict(list)
        delect_dic = {}
        change_dic = {}

        all_dic = defaultdict(list)

        for i in range(len(word_1)):
            if word_1[i] != '*' and word_2[i] != '*':
                if word1[int(word_1[i]) - 1] == word2[int(word_2[i]) - 1]:
                    match_list.append(int(word_1[i]))
                    match_index_list.append(i)

        for i in range(len(match_index_list) - 1):
            if match_index_list[i] != match_index_list[i + 1] - 1:
                leap.append((match_index_list[i], match_index_list[i + 1]))



        list_1 = []
        list_2 = []
        for x in leap:
            i = x[0] + 1
            j = x[1]
            for k in range(i, j):
                if word_1[k] != '*':
                    list_1.append(int(word_1[k]))
                if word_2[k] != '*':
                    list_2.append(int(word_2[k]))

            if len(list_1) == 0 and len(list_2) != 0:
                n = min(list_2)
                m = max(list_2)
                if n == m:
                    add_dic[int(word_1[i - 1])] = n
                else:
                    add_dic[int(word_1[i - 1])] = (n, m)

                list_1.clear()
                list_2.clear()
            elif len(list_1) != 0 and len(list_2) == 0:
                n = min(list_1)
                m = max(list_1)
                if n == m:
                    delect_dic[n] = int(word_2[i - 1])
                else:
                    delect_dic[(n,m)] = int(word_2[i - 1])

                list_1.clear()
                list_2.clear()

            elif len(list_1) != 0 and len(list_2) != 0:
                n = min(list_1)
                m = max(list_1)
                n_1 = min(list_2)
                m_1 = max(list_2)

                if n == m and n_1 == m_1:
                    change_dic[n] = (n_1)
                elif n == m and n_1 != m_1:
                    change_dic[n] = (n_1, m_1)
                elif n != m and n_1 != m_1:
                    change_dic[(n,m)] = (n_1, m_1)
                elif n != m and n_1 == m_1:
                    change_dic[(n,m)] = (n_1)

            

                list_1.clear()
                list_2.clear()


        min_match = min(match_index_list)
        max_match = max(match_index_list)

        a = (0, min_match)
        if max_match == len(word_1) - 1:
            leap_out = [a]
        else:
            b = (max_match + 1, len(word_1))
            leap_out = [a,b]

        list_11 = []
        list_22 = []
        for x in leap_out:
            if x[0] == 0:
                i = x[0]
                j = x[1]
            else:
                i = x[0]
                j = x[1]

            for k in range(i, j):
                if word_1[k] != '*':
                    list_11.append(int(word_1[k]))
                if word_2[k] != '*':
                    list_22.append(int(word_2[k]))

            
            if len(list_11) == 0 and len(list_22) != 0:
                n = min(list_22)
                m = max(list_22)
                if n == m:
                    if i == 0:
                        add_dic[0] = n
                    else:
                        add_dic[word_1[i - 1]] = n
                else:
                    if i == 0:
                        add_dic[0] = (n, m)
                    else:
                        add_dic[int(word_1[i - 1])] = (n, m)

                list_11.clear()
                list_22.clear()
            elif len(list_11) != 0 and len(list_22) == 0:
                n = min(list_11)
                m = max(list_11)
                if n == m:
                    if i == 0:               
                        delect_dic[n] = 0
                    else:
                        delect_dic[n] = int(word_2[i - 1])
                else:
                    if i == 0:
                        delect_dic[(n,m)] = 0
                    else:
                        delect_dic[(n,m)] = int(word_2[i - 1])
                    

                list_11.clear()
                list_22.clear()

            elif len(list_11) != 0 and len(list_22) != 0:
                n = min(list_11)
                m = max(list_11)
                n_1 = min(list_22)
                m_1 = max(list_22)
                
                if n == m and n_1 == m_1:
                    change_dic[n] = (n_1)
                elif n == m and n_1 != m_1:
                    change_dic[n] = (n_1, m_1)
                elif n != m and n_1 != m_1:
                    change_dic[(n,m)] = (n_1, m_1)
                elif n != m and n_1 == m_1:
                    change_dic[(n,m)] = (n_1)

                list_11.clear()
                list_22.clear()

            


        for i in add_dic:
            if isinstance(i, tuple):
                all_dic[min(i)].append(i)
                all_dic[min(i)].append(add_dic[i])
                all_dic[min(i)].append('a')
                all_dic[min(i)].append('@')
            else:        
                all_dic[int(i)].append(add_dic[i])
                all_dic[int(i)].append('a')

        for i in delect_dic:
            if isinstance(i, tuple):
                all_dic[min(i)].append(i)
                all_dic[min(i)].append(delect_dic[i])
                all_dic[min(i)].append('d')
                all_dic[min(i)].append('@')
            else:
                all_dic[int(i)].append(delect_dic[i])
                all_dic[int(i)].append('d')

        for i in change_dic:
            if isinstance(i, tuple):
                all_dic[min(i)].append(i)
                all_dic[min(i)].append(change_dic[i])
                all_dic[min(i)].append('c')
                all_dic[min(i)].append('@')
            else:
                all_dic[int(i)].append(change_dic[i])
                all_dic[int(i)].append('c')
            
            
        result = ''
        for i in sorted(all_dic):
            if all_dic[i][-1] == '@':
                if isinstance(all_dic[i][0], tuple):
                    result += str(all_dic[i][0][0]) + ',' + str(all_dic[i][0][1])
                else:
                    result += str(all_dic[i][0])

                result += str(all_dic[i][2])

                if isinstance(all_dic[i][1], tuple):
                    result += str(all_dic[i][1][0]) + ',' +str(all_dic[i][1][1])
                else:
                    result += str(all_dic[i][1])

                result += '\n'
            else:
                result += str(i) + str(all_dic[i][1])
                if isinstance(all_dic[i][0], tuple):
                    result += str(all_dic[i][0][0]) + ',' +str(all_dic[i][0][1])
                else:
                    result += str(all_dic[i][0])

                result += '\n'
        result = result.strip('\n')
        return result


    def is_a_possible_diff(self, command):
        file_1_list = []
        file_2_list = []
        for i in range(len(self.word_1) + 1):
            if i in command.d_left or i in command.c_left:
                continue
            file_1_list.append(i)

        for i in range(len(self.word_2) + 1):
            if i in command.a_right or i in command.c_right:
                continue
            file_2_list.append(i)
        if len(file_1_list) != len(file_2_list):
            return False
        dic = {}

        for i in range(len(file_1_list)):
            dic[file_1_list[i]] = file_2_list[i]

        for i in dic:
            if i in command.dic:
                if command.dic[i] != dic[i]:
                    return False
        dic_left = dic
     
        L = self.word_1
        T = self.word_2
        R = []
        for i in dic_left:
            if i - 1 >= 0 and i - 1 < len(L):
                if dic_left[i] - 1 < 0 or dic_left[i] - 1 >= len(T):
                    return False
            else:
                if dic_left[i] - 1 >= 0 and dic_left[i] - 1 < len(T):
                    return False
        for i in dic_left:
            if i - 1 >= 0 and i - 1 < len(L) and dic_left[i] - 1 >= 0 and dic_left[i] - 1 < len(T):
                R.append(i - 1)
                if L[i - 1] != T[dic_left[i] - 1]:
                    return False
        if len(R) == 0:
            return False
        return True

    def output_diff(self, command):
        L = command.output_diff_aid()
        w_1 = self.word_1
        w_2 = self.word_2

        for i in L:
            print(i)
            if 'd' in i:
                a = i.split('d')
                front_number_str = a[0]
                back_number_str = a[1]
                front_number = [int(k) for k in a[0].split(',') ]
                back_number = [int(k) for k in a[1].split(',')]
                if len(front_number) == 1:
                    print('<', w_1[front_number[0] - 1])
                else:
                    for i in range(front_number[0] - 1, front_number[1]):
                        print('<', w_1[i])

            elif 'a' in i:
                a = i.split('a')
                front_number_str = a[0]
                back_number_str = a[1]
                front_number = [int(k) for k in a[0].split(',') ]
                back_number = [int(k) for k in a[1].split(',')]
                if len(back_number) == 1:
                    print('>', w_2[back_number[0] - 1])
                else:
                    for j in range(back_number[0] - 1, back_number[1]):
                        print('>', w_2[j])

            elif 'c' in i:
                a = i.split('c')
                front_number_str = a[0]
                back_number_str = a[1]
                front_number = [int(k) for k in a[0].split(',') ]
                back_number = [int(k) for k in a[1].split(',')]
                if len(front_number) == 1:
                    print('<', w_1[front_number[0] - 1])
                else:
                    for i in range(front_number[0] - 1, front_number[1]):
                        print('<', w_1[i])
                print('---')
                if len(back_number) == 1:
                    print('>', w_2[back_number[0] - 1])
                else:
                    for j in range(back_number[0] - 1, back_number[1]):
                        print('>', w_2[j])

    def output_unmodified_from_original(self, command):
        file_1_list = []
        file_2_list = []
        for i in range(len(self.word_1) + 1):
            if i in command.d_left or i in command.c_left:
                continue
            file_1_list.append(i)

        for i in range(len(self.word_2) + 1):
            if i in command.a_right or i in command.c_right:
                continue
            file_2_list.append(i)

        dic = {}
        
        for i in range(len(file_1_list)):
            dic[file_1_list[i]] = file_2_list[i]
            


        
        w_1 = self.word_1
        w_2 = self.word_2
        L = []
        
        for i in dic:
            if i - 1>= 0 and i - 1 < len(w_1):
                L.append(i - 1)
        
        if L[0] != 0:
            print('...')
        if len(L) == 1:
            print(w_1[L[0]])
            if L[0] != len(w_1) - 1:
                print('...')
            return
        for i in range(len(L) - 1):
            if L[i] == L[i + 1] - 1:
                print(w_1[L[i]])
            else:
                print(w_1[L[i]])
                print('...')
        print(w_1[L[-1]])
        if L[-1] != len(w_1) - 1:
            print('...')


    def output_unmodified_from_new(self, command):

        file_1_list = []
        file_2_list = []
        for i in range(len(self.word_1) + 1):
            if i in command.d_left or i in command.c_left:
                continue
            file_1_list.append(i)

        for i in range(len(self.word_2) + 1):
            if i in command.a_right or i in command.c_right:
                continue
            file_2_list.append(i)

        dic = {}

        for i in range(len(file_1_list)):
            dic[file_1_list[i]] = file_2_list[i]


        w_2 = self.word_2
        L = []
        for i in dic:
            if dic[i] - 1 >= 0 and dic[i] - 1 < len(w_2):
                L.append(dic[i] - 1)
        
        if L[0] != 0:
            print('...')
        if len(L) == 1:
            print(w_2[L[0]])
            if L[0] != len(w_2) - 1:
                print('...')
            return
        for i in range(len(L) - 1):
            if L[i] == L[i + 1] - 1:
                print(w_2[L[i]])
            else:
                print(w_2[L[i]])
                print('...')
        print(w_2[L[-1]])
        if L[-1] != len(w_2) - 1:
            print('...')



