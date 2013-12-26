#!/usr/bin/env python
import sys

def eratosthenes(n):
        multiples = []
        for i in xrange(2, n+1):
                if i not in multiples:
                        print i
                        for j in xrange(i*i, n+1, i):
                                multiples.append(j)


# Implementation of main        
def main():
        eratosthenes(100)
        raw_input()

if __name__ == '__main__':
        status = main()
        sys.exit(status)