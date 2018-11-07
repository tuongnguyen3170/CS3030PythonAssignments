#!/usr/bin/env python3
"""
This module is used to detect the first 25 error from the input link
"""
from __future__ import print_function
import urllib.request
from itertools import groupby
import sys


def page_check(link):
    """
    This function use to check the conditions
    link:
        the input link from the argument
    """
    url = urllib.request.urlopen(link)
    my_file = url.read() #read in the file

    my_list = str(my_file, 'utf-8').split() #cast the data to string type
    #findinf the errors that match the condition
    the_list = [x for x in my_list if '/var/www/html/' in x
                or '/htdocs' in x or '/home/' in x or '/usr/' in x]
    subl = []

    for item in the_list:
        if item not in subl:
            subl.append(item)
        else:
            continue
    dic = {}
    print('***Top 25 ERRORS***')
    for log, duplicates in groupby(sorted(my_list)): # sort and group duplicates
        if log in subl:
            count = len(list(duplicates)) # count how many times the word occurs
            dic[log]=count
            #print('Count: {count}\tPage: {log}'.format(log=log, count=count))
        else:
            continue
    final_list = [(k, dic[k]) for k in sorted(dic, key=dic.get, reverse=True)]
    count_error = 1
    for page,count in final_list:
        if count_error < 26:
            print('Count: {count}\tPage: {page}'.format(page=page,count=count))
            count_error +=1
        else:
            continue
def main():
    """
    Test the program
    """
    #count the argument
    arg = len(sys.argv)-1

    #No argument passed
    if arg == 0:
        print('Usage is: ./tuong_nguyen_hw6.py <file Input>')
        print('Usage is: ./tuong_nguyen_hw6.py --help')
        exit(0)

    #Call the function help
    elif sys.argv[1] == '--help':
        print('Usage is: ./tuong_nguyen_hw6.py --help')
        print('Usage is: ./tuong_nguyen_hw6.py <file Input>')

    #Call the page_check function
    else:
        page_check(sys.argv[1])

if __name__ == "__main__":
    main()
    exit(0)
