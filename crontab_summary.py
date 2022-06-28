#!/usr/bin/python3
import os
import sys
import re

# exception exit:
# 1: insufficient argument!
# 2: error in the argument amount for the specific option
# 3: argument content error

if len(sys.argv) < 3:
    print("insufficient argument!")
    exit(1)

target_crontab = sys.argv[-1]

if not os.path.exists(target_crontab):
    print('file', target_crontab, 'does not exist')
    exit(0)
else:
    pass

if os.stat(target_crontab).st_size < 2:
    print("no crontab commands")
    exit(0)
else:
    pass


# this function is the main control
def option_execution(opt):
    if opt == "-a":
        option_a()
    elif opt == "-u":
        option_u()
    elif opt == "-t":
        option_t()
    elif opt == "-v":
        option_v()
    else:
        print("error! no such option")
        exit(3)


def option_a():
    length_validation(3)
    fin = open(target_crontab)
    # search the content after the forth comma
    for line in fin:
        x = re.split(',', line.rstrip())
        print(x[4])
    # empty files are handled by operation in line 24


def option_u():
    length_validation(4)
    user_name = sys.argv[-2]
    fin = open(target_crontab)
    match_result = []
    for line in fin:
        x = re.split(',', line.rstrip())
        if x[3] == user_name:
            match_result += [line.rstrip()]

    if len(match_result) == 0:
        print("no crontab lines for user", user_name)
    else:
        print("crontab lines for user", user_name, ":")
        for item in match_result:
            print(item)


def option_t():
    length_validation(4)
    argv_time = sys.argv[-2]
    argv_time_elem = re.split(':', argv_time)
    # verify the argument's format
    if len(argv_time_elem) > 3:
        print("argument error")
        exit(3)
    fin = open(target_crontab)
    match_result = []
    for line in fin:
        x = re.split(',', line)
        if int(x[2]) < int(argv_time_elem[2]):
            continue
        elif int(x[2]) > int(argv_time_elem[2]):
            match_result += [line.rstrip()]
        # the following case list_time_elem[2] = argv_time_elem[2]
        elif int(x[1]) < int(argv_time_elem[1]):
            continue
        elif int(x[1]) > int(argv_time_elem[1]):
            match_result += [line.rstrip()]
        # the following case list_time_elem[1] = argv_time_elem[1]
        elif int(x[0]) < int(argv_time_elem[0]):
            continue
        else:
            match_result += [line.rstrip()]
    if len(match_result) == 0:
        print("no crontab lines on or after", argv_time)
    else:
        print("crontab lines on or after", argv_time, ":")
        for item in match_result:
            print(item)


def option_v():
    length_validation(3)
    print("Student Name: Hin Hang Ho")
    print("Student ID: 10620084")
    print("Date of completion: 26 May 2022")


def length_validation(argv_num):
    if len(sys.argv) != argv_num:
        print("input amount error")
        exit(2)


option = sys.argv[1]
option_execution(option)
