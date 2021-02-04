#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

#-------------------------------#
# ADDING BULLETS TO WIKI MARKUP #
#-------------------------------#

# When editing a Wikipedia article, you can create a bulleted list by putting each list item on its own line and placing a star in front. But say you have a really large list that you want to add bullet points to. You could just type those stars at the beginning of each line, one by one. Or you could automate this task with a short Python script.

# Step 1: Copy and Paste from the Clipboard
# Using the Wikipedia page 'List of lists of lists', copy one of the lists of lists 
import pyperclip
text = pyperclip.paste()
print(text)

# Step 2: Separate the Lines of Text and Add the Star
lines = text.split('\n')
print(lines)
for i in range(len(lines)):     # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # add star to each string in 'lines' list
print(lines)

# Step 3: Join the Modified Lines
text = '\n'.join(lines)
print(text)

pyperclip.copy(text)
