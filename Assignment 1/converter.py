choices = {
    "1a": ">Windows XP",
    "1b": "> Macintosh Mac OS X 10.0",
    "2a": "Valid title",
    "2b": "Invalid title",
    "3a": "Valid date",
    "3b": "Invalid date",
    "4a": "Invalid time",
    "4b": "Valid time",
    "5a": "Valid date",
    "5b": "Invalid date",
    "6a": "Invalid time",
    "6b": "Valid time",
    "7a": "Australian location",
    "7b": "American location",
    "7c": "Invalid location",
    "8a": "Invalid name",
    "8b": "Valid name",
    "8c": "No name",
    "9a": "Invalid email",
    "9b": "Valid email",
    "9c": "No email",
    "10a": "Invalid phone",
    "10b": "Valid phone",
    "10c": "No phone",
    "11a": "Description included",
    "11b": "No description"
}

res = '''
1a 2a 3a 4b 5a 6b 7c 8a 9b 10b 11b
1b 2b 3b 4a 5b 6a 7a 8b 9a 10a 11a
1a 2a 3b 4a 5b 6b 7b 8c 9c 10c 11b
1b 2a 3a 4b 5a 6a 7a 8c 9c 10c 11a
1a 2b 3a 4b 5a 6b 7b 8b 9a 10a 11b
1b 2b 3b 4a 5b 6a 7c 8a 9b 10b 11a
1a 2a 3b 4b 5b 6b 7a 8b 9a 10b 11a
1b 2b 3b 4a 5a 6a 7b 8a 9c 10c 11b
1b 2b 3a 4a 5b 6b 7c 8c 9a 10c 11a
1a 2b 3b 4a 5a 6a 7b 8b 9b 10c 11a
1a 2a 3a 4b 5a 6b 7c 8b 9c 10a 11a
1a 2b 3a 4a 5b 6a 7a 8a 9b 10a 11b
1b 2a 3a 4b 5a 6a 7b 8c 9b 10b 11b
1b 2b 3b 4b 5a 6b 7c 8a 9a 10a 11a
1a 2b 3b 4b 5a 6b 7c 8c 9c 10a 11b
1b 2a 3b 4a 5b 6b 7a 8a 9c 10b 11b
'''

res = [line.split() for line in res.split('\n') if line]

for h in range(len(res)):
    line = res[h]
    print("Line num: " + str(h))
    for i in range(len(line)):
        line[i] = choices[line[i]] 
        print(line[i])
    print("\n")