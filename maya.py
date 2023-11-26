# Take as input word
#computer
#7 letter
#c6 valid
#com4 valid
#c1 not valid
# one number in word

#1 number
#check len(abb)+number = len(word)
#valid checks

# Corner cases: hello with eh3

def checkValidSting():

    word = input("Type in word: ")
    reply = input("Abbrievation: ")

    if (word.isnumeric()) or len(reply)>len(word):
        return False

    i = 0
    j = 0
    #ca3 currently passes
    while i < len(reply):
        replyChar = reply[i]
        print(replyChar)
        wordChar = word[j]
        print(wordChar)
        if replyChar.isdigit():
            j += int(replyChar)
            if len(reply) + int(replyChar) - 1 != len(word):
                return False
        else:
            if replyChar != wordChar:
                return False
            else:
                j += 1
        i += 1       

    return True
        

def main():
    if checkValidSting():
        print("Valid Abbrievation")
    else:
        print("Invalid Abbrievation")

if __name__ == '__main__':
    main()

# import re

# wordLetters = re.findall(r"[a-zA-Z]", word)
# could also use split here with replyLetters = re.split(r"[a-zA-Z]+", reply)
    # replyNumbers = re.findall(r"(\d)", reply)
    # print(replyNumbers)
    # print(len(replyNumbers))
    # replyLetters = re.findall(r"[a-zA-Z]", reply)
    # print(replyLetters)
    # print(len(replyLetters))

    # try:
    #     number = replyNumbers[0]
    # except: 
    #     return False
    
    # #check if string. still leaves open weird edge cases hell e1e
    # skip = 0
    # i = 0 
    # for i in reply[count]:
    #     for j in word:
    #         if skip == 0:
    #             if i.isnumeric():
    #                 skip = i
    #             else:
    #                 if i != j:
    #                     return valid == False
    #         else:
    #             skip =- 1
    #             count += 1 



    # if len(replyNumbers) != 1:
    #     return False
    # elif int(number) + len(replyLetters) != wordLength:
    #     return False
    # return