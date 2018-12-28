numbers_in_characters= {0:"", 1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine" , 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:" nineteen" , 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",100:"hundred", 1000:"thousand"}

def convert_to_letters(x):
    in_letters=0
    i=1
    s=[]
    for i in range(0, len(x)):
        s.append(x[i])


    if x[len(x) - 2] == '1' and int(x) > 9 :
        in_letters += len(numbers_in_characters[int(s.pop()) + 10 ])
        s.pop()

    else:
        in_letters += len(numbers_in_characters[int(s.pop())])

        if s!=[]:
            in_letters +=len(numbers_in_characters[int(s.pop())*10])

    if s != []:
        in_letters += len(numbers_in_characters[int(s.pop())])
        in_letters += len(numbers_in_characters[100])
        in_letters += len("and")
    if s != []:
        in_letters += len(numbers_in_characters[1000])


    return in_letters




#main function:

length=0
for i in range(1,1001):
    length+= convert_to_letters(str(i))
print(length)