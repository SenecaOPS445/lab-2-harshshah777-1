#!/usr/bin/env python3

#Author: Harsh Mangeshkumar Shah
#Author_ID: hshah98
#Date Created: 2024/01/26

import sys

timer = 3

if len(sys.argv) > 1:
	timer = int(sys.argv[1])

while timer > 0:
	print(timer)
	timer -= 1

print('blast off!')

