#Problem 22 Project Euler

with open('/Users/macbook/Downloads/name.txt','r') as f:
    #print(f.read())
    names = f.read()
    f.close()

#split the names into a list
list_names = names.strip().split(",")

list_names = [i[1:-1] for i in list_names]

#sorting
names = sorted(list_names)
#print(sorted_list)

#getting letter score - using ord() function
def letter_score(letter):
    letter_score = ord(letter) - 64 #The ord() function returns the number representing the unicode code of a specified character. For example: ord(a) = 65 => score of letter a is 65 - 64 = 1
    return letter_score

def name_value(name):
    return sum(letter_score(l) for l in name)

def name_score(name, index):
    return name_value(name) * (index + 1)

#The total of all the name scores in the file is
print(sum(name_score(names[i], i) for i in range(0, len(names)))) #871198282