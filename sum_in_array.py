# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

def main(arr: list, sum_target: int) -> list:
    for i, num in enumerate(arr):
        difference = sum_target - num

        if difference in arr[i+1:]:
            return [num, difference]

    else:
        return [-1]


if __name__ == "__main__":
    tests = [([-3, 1, 4, 6], 7), ([-3, 1, 4, 6], 8), ([-3, 0, 1, 4, 6], 1),]
    for t in tests:
        print(main(t[0], t[1]))