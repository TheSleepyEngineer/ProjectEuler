numbers_in_characters= {0:"", 1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine" , 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:" nineteen" , 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",100:"hundred", 1000:"thousand"}

def convert_to_letters(x):
    length_in_letters=0

    # in case x == 1000
    if x == "1000":
        length_in_letters = len(numbers_in_characters[1]) + len("thousand")
        return length_in_letters


    i = len(x)

    if i==3:
        string = numbers_in_characters[int(x[0])] + "hundred"
        length_in_letters+= len(string)
        i=-1
        x= x[1] + x[2]
        # in case 300 don't need the "and"
        if int(x) != 0:
            length_in_letters+= len("and")

    if i==2:
        length_in_letters += len(numbers_in_characters[int(x[0]+"0")])
        i = -1
        x = x[1]

    if i==1:
        length_in_letters += len(numbers_in_characters[int(x[0])])

    return length_in_letters




# Main function:


length=0
for i in range(1,1001):
    length+= convert_to_letters(str(i))
print(length)
