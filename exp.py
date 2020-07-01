#coding:utf-8

'''
pip install requests
'''

import sys
import requests

from payload.payload import exploit

if __name__ == '__main__':
	if len(sys.argv)!=2:
		print '[usage]:python exp.py url'
		exit(-1)
	url=sys.argv[1]
	exploit(url)