#!/usr/bin/python3
"""
Python script takes URL from stdin and compute exact metrics
"""
import sys
import traceback


if __name__ == "__main__":

    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    file_list = []
    stat_dict = {}
    file_size = 0
    line_num = 0

    for stat in codes:
        stat_dict[stat] = 0
    try:
        for line in sys.stdin:
            try:
                file_list = line.split(" ")
                flist_length = len(file_list)
                if flist_length != 9:
                    pass
                if file_list[-2] in codes:
                    stat_dict[file_list[-2]] += 1
                if file_list[-1][-1] == '\n':
                    file_list[-1][:-1]
                file_size += int(file_list[-1])
            except:
                pass
            line_num += 1
            if line_num % 10 == 0:
                print("File size: {}".format(file_size))
                for stat in sorted(stat_dict.keys()):
                    if stat_dict[stat] != 0:
                        print("{}: {}".format(stat, stat_dict[stat]))
        print("File size: {}".format(file_size))
        for stat in sorted(stat_dict.keys()):
            if stat_dict[stat] != 0:
                print("{}: {}".format(stat, stat_dict[stat]))
    except KeyboardInterrupt as error:
        print("File size: {}".format(file_size))
        for stat in sorted(stat_dict.keys()):
            if stat_dict[stat] != 0:
                print("{}: {}".format(stat, stat_dict[stat]))
        raise
