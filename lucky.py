# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

import re

def regex_search(seq_num: int) -> str:
    # first cast value from int to str
    seq_str = str(seq_num)

    seqs = re.findall(r'[5-6]+', seq_str)
    
    seq_longest = ''
    for i in range(len(seqs)):
        if len(set(map(int, seqs[i]))) < 2:
            continue

        if len(seqs[i]) > len(seq_longest):
            seq_longest = seqs[i]

    return seq_longest



def pure_loop_search(seq_num: int) -> str:
    # first cast value from int to str
    seq_str = str(seq_num)

    lucky_series = '0'
    lucky_numbers = [str(5), str(6)]

    # let's define a search state
    search_state = 0 # meaning there has been no first entry from lucky series

    index = 0
    while (index < len(seq_str)):
        num_str = seq_str[index]

        if search_state == 0 and num_str in lucky_numbers:
            first_index = index
            search_state = 1  

        elif search_state == 1 and num_str not in lucky_numbers:
            last_index = index

            new_series = seq_str[first_index:last_index]

            if len(new_series) > len(lucky_series) and len(set(map(int, new_series))) == 2:
                lucky_series = new_series

            search_state = 0

        
        elif search_state == 1 and num_str in lucky_numbers and index == len(seq_str)-1:
            new_series = seq_str[first_index:]
            if len(new_series) > len(lucky_series) and len(set(map(int, new_series))) == 2:
                lucky_series = new_series

            search_state = 0


        index += 1

    return lucky_series
    

if __name__ == "__main__":
    test = [6666666666, 66666666666666665, 5454455556432455555555566666666, 4556432455665334, 5656556565, 566436, 55555]
    for t in test:
        print(f"REGEX the longest lucky sequence of {t} is {regex_search(t)}")
        print(f"LOOP the longest lucke seq of {t} is {pure_loop_search(t)}")