numbers_in_characters= {0:"", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine" , 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen" , 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety",100:"Hundred", 1000:"Thousand"}

def convert_to_letters(x):
    length_in_letters=0
    string=''

    # in case x == 1000
    if x == "1000":
        length_in_letters = len(numbers_in_characters[1]) + len("Thousand")
        return length_in_letters


    i = len(x)

    if i==3:
        string = numbers_in_characters[int(x[0])] + "Hundred"
        #length_in_letters+= len(string)
        i-=1
        x= x[1] + x[2]
        # in case 300 don't need the "and"
        if int(x) != 0:
            string +="And"

    if i==2 and x[0]=='1':
        string += numbers_in_characters[int(x)]

    else:
        if i==2:
            #length_in_letters += len(numbers_in_characters[int(x[0]+"0")])
            string += numbers_in_characters[int(x[0]+"0")]
            i -=1
            x = x[1]

        if i==1:
            #length_in_letters += len(numbers_in_characters[int(x[0])])
            string += numbers_in_characters[int(x[0])]


    length_in_letters += len(string)

    return length_in_letters




# Main function:


length=0
for i in range(1,1001):
    length+= convert_to_letters(str(i))
print(length)
