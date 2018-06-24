#! /usr/bin/env python3
# phoneAndEmail.py - Finds phone numbers and email
# addresses on the clipboard.


import pyperclip
import re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+         # username
    @                         # @ symbol
    [a-zA-Z0-9.-]+            # domain name
    (\.[a-zA-Z]{2,4})         # dot-something
    )''', re.VERBOSE)

QQRegex = re.compile(r'''(
    ([qQ]+)               # qq or QQ
    (\s|-|\.|:|：)*       # separator
    ([0-9]+)              # numbers
    )''', re.VERBOSE)


# get the text from clipboard
text = str(pyperclip.paste())
matches = []

# search for phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' ext ' + groups[8]
    matches.append(phoneNum)

# search for email addresses
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# search for QQ
for groups in QQRegex.findall(text):
    matches.append(': '.join([groups[1], groups[3]]))

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
