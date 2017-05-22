import os
from urllib.parse import urlparse
import sys
import urllib.request as req

# from urllib.parse import urlparse


def downloadAll(*urls):
    result = []
    for item in urls:
        result.append(download(item))
    return result

def download(url, to=None):
    # print('trying to download the file!')
    data = req.urlopen(url).read()
    if to and check_file(to):
        write_file(data, to)
    else:
        return data

def usage():
    res = "downloads content from url to specified filename\nExample: 'python webget.py www.google.com google.txt'"


def write_file(data, file_name):
    print('trying to write the file!')
    with open(file_name, "w") as f:
        f.write(str(data))

def check_file(file_name):
    return not os.path.isfile(file_name)



def check_args(input):
    print(input[0])
    if len(input) > 2:
        return False

    result = urlparse(url=input[0])
    print('result: {0}'.format(result))
    if result.scheme and result.netloc:
        print('URL OK: {0}'.format(result))
    else:
        print('INVALID URL')
        usage()
        sys.exit(2)
    if len(input)<2:
        input.append(input[0].split('/')[-1])
    if check_file(input[1]):
        return True
    else:
        print('FILE ALREADY EXIST: {0}'.format(input[1]))
        usage()
        sys.exit(2)



def run(arguments):
    if check_args(arguments):
        download(arguments[0], arguments[1])

if __name__ == '__main__':
    run(sys.argv[1:])
