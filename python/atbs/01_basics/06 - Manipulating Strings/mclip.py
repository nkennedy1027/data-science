#! python3
# mclip.py - A multi-clipboard program

#------------------------------------#
# MULTI-CLIPBOARD AUTOMATIC MESSAGES #
#------------------------------------#

# There are some scenarios when you need to repeat large blocks of text
# over and over again, but because you can only hold one thing in your
# clipboard at once, you have to store those blocks and copy them 
# individually, when needed.  This program aims to alleviate this
# challenge.  

# Step 1: Data structures

TEXT = {
    'agree':"""Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a montly donation?"""
}

# Step 2: Handle command line arguments

import sys, pyperclip

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

# Step 3: Copy the right phrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + 'copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

