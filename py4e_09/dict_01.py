# QUIZ
# Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sender = []
counts = {}
common_email = None
largest_count = None

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    sender_email = words[1]
    sender.append(sender_email)

for email in sender:
    counts[email] = counts.get(email, 0) + 1

for word,count in counts.items():
    if common_email == None or count > largest_count:
        common_email = word
        largest_count = count

print(common_email, largest_count)
