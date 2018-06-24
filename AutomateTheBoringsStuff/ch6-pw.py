#! /usr/bin/env python3
# pw.py - An insecure password locker program.
'''To use this program, do the following:
1 - open terminal
2 - paste in: /Users/luffy/Desktop/CS/AutomateTheBoringsStuff/ch6-pw.py
3 - type the account name you want the password for, ex, email
4 - press enter'''


import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line argv is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
