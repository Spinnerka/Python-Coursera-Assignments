# for sample data
import re
hand = open('sample.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1: continue
    for pos in stuff:
        num = int(pos)
        numlist.append(num)

print('Sum of all numbers', sum(numlist))


#for actual data
import re
hand = open('actual.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1: continue
    for pos in stuff:
        num = int(pos)
        numlist.append(num)

print('Sum of all numbers', sum(numlist))
