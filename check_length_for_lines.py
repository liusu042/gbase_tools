#!/usr/bin/env python
# encoding:utf8

# @FileName: check_length_for_lines.py
# @Author: liulizeng@gbase.cn
# @CreateDate: 2017-12-03
# @Description: check length of each line.

import sys


def check_length_for_lines(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            lineLength = len(line.rstrip('\n'))
            result[lineLength] = result.get(lineLength, 0) + 1
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: python %s filename" % sys.argv[1]
        sys.exit(1)
    result = check_length_for_lines(sys.argv[1])
    for k in result:
        print "length of %d lines is %d." % (result[k], k)
