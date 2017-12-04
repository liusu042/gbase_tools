#!/usr/bin/env python
# encoding:utf8

# @FileName: del_utf8_to_fixed_len_gbk.py
# @Author: liulizeng@gbase.cn
# @CreateDate: 2017-12-03
# @Description: transform a utf8 decoding text with delimiter to gbk(gb18030) encoding file with fixed length.

import sys
from optparse import OptionParser


def del_utf8_to_fixed_length_gbk(
        delimiter,
        colLenList,
        sourceFile,
        targetFile,
        sourceEncoding='utf8',
        targetEncoding='gb18030'):
    with open(sourceFile) as fr:
        with open(targetFile, 'w') as fw:
            for line in fr:
                tmpList = line.rstrip("\n").split(delimiter)
                for i in range(len(colLenList)):
                    tmpStr = tmpList[i].decode(sourceEncoding).encode(targetEncoding)
                    blankCount = colLenList[i] - len(tmpStr)
                    if blankCount >= 0:
                        fw.write(tmpStr + " " * blankCount)
                    else:
                        blankCount = 0
                        writeStr = ""
                        while True:
                            try:
                                writeStr = tmpStr[:colLenList[i] - blankCount].decode(targetEncoding)
                                break
                            except Exception:
                                blankCount += 1
                        fw.write(writeStr.encode(targetEncoding) + " " * blankCount)
                fw.write('\n')
    return 0


if __name__ == "__main__":
    # if len(sys.argv) < 5:
    #     print "usage  : python %s delimiter colLenList sourceFile targetFile" % sys.argv[0]
    #     print "example: python %s '|' '10,10,10' /tmp/1.txt /tmp/1.txt.gbk" % sys.argv[0]
    #     sys.exit(1)
    parser = OptionParser()
    parser.add_option('-d', '--delimiter', dest='delimiter',
                      help='delimiter of columns', metavar='DELIMITER')
    parser.add_option('-l', '--column_length_list', dest='columnLengthList',
                      help="the fixed lenth list of colums, separated by comma, for example '2,10,2'",
                      metavar='COLUMN_LENGTH_LIST')
    parser.add_option('-s', '--sourceFile', dest='sourceFile',
                      help='filepath to transform', metavar='FILENAME')
    parser.add_option('-t', '--targetFile', dest='targetFile',
                      help='output filepath', metavar='FILENAME')
    options, args = parser.parse_args()

    if None not in (options.delimiter, options.columnLengthList, options.sourceFile, options.targetFile):
        delimiter = options.delimiter.decode('string_escape')
        colLenList = [int(x) for x in options.columnLengthList.split(',')]
        sourceFile = options.sourceFile
        targetFile = options.targetFile
        rc = del_utf8_to_fixed_length_gbk(delimiter, colLenList, sourceFile, targetFile)
        sys.exit(rc)
    else:
        print "ERROR: please input arguments.\n"
        parser.print_help()
        sys.exit(1)
