#!/usr/bin/env python3

import sys
from collections import Counter

# main
# use Counter to count items in string given as argument to script
def main():
    if (len(sys.argv) > 1):
        # Split by space
        sentence = sys.argv[1].split()
        cnt = Counter(sentence)
        for k,v in cnt.items():
            print(k + ":" + str(v))
    else:
        print("Please pass argument of type string to script e.g:'" + sys.argv[0] + " 'my foobar arg''")

if __name__  == "__main__":
    main()
