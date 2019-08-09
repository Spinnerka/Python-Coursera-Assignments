# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#        From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


name = input("Enter file:")
handle = open(name)

counts = dict()

#find 'from' lines in the txt file and get email address
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[5]
    words = words.split(':')
    words = words[0]
    counts[words] = counts.get(words, 0) + 1 #puts the email address in dictionary and counts it

lst = list()
for key, val in counts.items():
    lst.append((key,val))

lst = sorted(lst)

for key, val in lst:
    print(key,val)





#
