name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

"""
---------------------------------------------------------------------------------------------------------------
input
    Get data from the “outside world”. This might be reading data from a file, or even some kind of sensor like 
    a microphone or GPS. In our initial programs, our input will come from the user typing data on the keyboard. 
output
    Display the results of the program on a screen or store them in a file or perhaps write them to a device like
     a speaker to play music or speak text. 
sequential execution
    Perform statements one after another in the order they are encountered in the script. 
conditional execution
    Check for certain conditions and then execute or skip a sequence of statements. 
repeated execution
    Perform some set of statements repeatedly, usually with some variation. 
reuse
    Write a set of instructions once and give them a name and then reuse those instructions as needed throughout your program. 
----------------------------------------------------------------------------------------------------------------
"""