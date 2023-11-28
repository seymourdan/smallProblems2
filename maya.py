'''
Check that an abbrievation of a word with a number of chars replaced with that number of digits is valid. e.g. hello and 2llo
Corner case that needed solving was: car and ca3. 
'''

def checkValidSting():

    word = input("Type in word: ")
    reply = input("Abbrievation: ")

    if (word.isnumeric()) or len(reply)>len(word):
        return False

    #Loop through the reply and word chars. When the char is a digit in reply, skip by the number of that digit in the index in the original word 
    i = 0
    j = 0
    while i < len(reply):
        replyChar = reply[i]
        wordChar = word[j]
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