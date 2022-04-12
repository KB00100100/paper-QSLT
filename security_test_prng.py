# -*- coding:utf-8 -*-
#!/usr/bin/env python

# sp800_22_tests.py
# 
# Copyright (C) 2017 David Johnston
# This program is distributed under the terms of the GNU General Public License.
# 
# This file is part of sp800_22_tests.
# 
# sp800_22_tests is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# sp800_22_tests is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with sp800_22_tests.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import argparse
import sys
import time
import random

def read_from_bytes(random_bytes):
    bitlist = list()
    for bytech in random_bytes:
        if sys.version_info > (3,0):
            byte = bytech
        else:
            byte = ord(bytech) 
        for i in range(8):
            bit = (byte >> i) & 1
            bitlist.append(bit)   
    #print(len(bitlist))
    return bitlist

# X 3.1  Frequency (Monobits) Test
# X 3.2  Frequency Test within a Block
# X 3.3  Runs Test
# X 3.4  Test for the Longest Run of Ones in a Block
# X 3.5  Binary Matrix Rank Test
# X 3.6  Discrete Fourier Transform (Specral) Test
# X 3.7  Non-Overlapping Template Matching Test
# X 3.8  Overlapping Template Matching Test
# X 3.9  Maurers Universal Statistical Test
# X 3.10 Linear Complexity Test
# X 3.11 Serial Test
# X 3.12 Approximate Entropy Test
# X 3.13 Cumulative Sums Test
# X 3.14 Random Excursions Test
# X 3.15 Random Excursions Variant Test 

def sp800_22_test(bits):
    testlist = [
        'monobit_test',
        'frequency_within_block_test',
        'runs_test',
        'longest_run_ones_in_a_block_test',
        'binary_matrix_rank_test',
        'dft_test',
        'non_overlapping_template_matching_test',
        'overlapping_template_matching_test',
        'maurers_universal_test',
        'linear_complexity_test',
        'serial_test',
        'approximate_entropy_test',
        'cumulative_sums_test',
        'random_excursion_test',
        'random_excursion_variant_test']

    print("Tests of Distinguishability from Random")

    results = list()
    
    for testname in testlist:
        #print("TEST: %s" % testname)
        m = __import__ ("sp800_22_"+testname)
        func = getattr(m,testname)
        
        (success,p,plist) = func(bits)

        summary_name = testname
        if success:
            #print("  PASS")
            summary_result = "PASS"
        else:
            #print("  FAIL")
            summary_result = "FAIL"
        
        if p != None:
            #print("  P="+str(p))
            summary_p = str(p)
            
        if plist != None:
            #for pval in plist:
                #print("P="+str(pval))
            summary_p = str(min(plist))
        
        results.append((summary_name,summary_p, summary_result))

    print()
    print("SUMMARY")
    print("-------")
    
    pass_ratio = 0.0
    for result in results:
        (summary_name,summary_p, summary_result) = result
        print(summary_name.ljust(40),summary_p.ljust(18),summary_result)
        if summary_result == "PASS":
            pass_ratio += 1.0
    pass_ratio = pass_ratio/15.0
    print("\nPASS Ratio:\t" + str(pass_ratio))
    return str(pass_ratio)

#def count_ones_zeroes(bits):
#    ones = 0
#    zeroes = 0
#    for bit in bits:
#        if (bit == 1):
#            ones += 1
#        else:
#            zeroes += 1
#    print("Zeroes:\t"+str(zeroes)+"\tOnes:\t"+str(ones))
#    res = float(zeroes/(zeroes+ones))
#    print("P:\t"+str(res))
#    return str(res)

# Function to create the
# random binary string
def rand_key(p):
   
    # Variable to store the
    # string
    key1 = ""
 
    # Loop to find the string
    # of desired length
    for i in range(p):
         
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))
 
        # Concatenation the random 0, 1
        # to the final result
        key1 += temp
         
    return(key1)


with open('security_result/prng-25K.txt','a+') as f1:
    res_last = 0.0
    for i in range(1,101):
        random_string = rand_key(204800)
        res = (float(sp800_22_test(list(map(int,random_string)))) + res_last*(i-1)) / i
        f1.write(str(res))
        f1.write('\n')
        time.sleep(1)
        res_last = res
