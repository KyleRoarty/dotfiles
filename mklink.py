#!/usr/bin/env python

import os, errno
from argparse import ArgumentParser

FILE = 0
LOC = 1
DOT = 2

def getFile(file_path, mode):
    try:
        return open(file_path, mode)
    except IOError:
        print "No file. Exiting"
        exit(1)


# Non-empty lines
def neLines(f):
    return filter(None, (line.strip() for line in f))

# Takes in path parts, returns absolute path
def absPath(*p_parts):
    return os.path.expanduser(os.path.join(*p_parts))

def mkLinks(file_path):
    curr_dir = os.getcwd()

    f = getFile(file_path, 'r')

    for line in neLines(f):
        src_dst = line.split(',')
        s_path = absPath(curr_dir, 'configs', src_dst[FILE])
        d_path = absPath(src_dst[LOC], src_dst[DOT]+src_dst[FILE])

        try:
            os.makedirs(os.path.dirname(os.path.realpath(d_path)))
            print "Making path %s." %(absPath(src_dst[LOC]))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        if os.path.islink(d_path):
            if os.path.realpath(d_path) == s_path:
                print "Link already exists."
            else:
                print "%s symlinked to file that isn't %s. Re-linking %s." %(d_path, s_path, d_path)
                os.unlink(d_path)
                os.symlink(s_path, d_path)
        elif not os.path.isfile(s_path):
            print "%s does not exist. Oops..." %(s_path)
        elif os.path.isfile(d_path):
            if not os.path.islink(d_path):
                print "%s exists, but is not a link. Deleting and creating link." %(d_path)
                os.remove(d_path)
                os.symlink(s_path, d_path)
        elif not os.path.isfile(d_path):
            print "%s does not exist. Creating link with %s" %(d_path, s_path)
            os.symlink(s_path, d_path)

    f.close()

def parseArgs():
    parser = ArgumentParser(prog="mkSymLinks")
    parser.add_argument('file', type=str,
                        help='file containing file name:symlink path pairs')

    return parser.parse_args()

def main():
    args = parseArgs()
    mkLinks(args.file)

if __name__ == '__main__':
    main()
