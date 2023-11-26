
import re

def validString():
    # get inputs
    string = input("Type in word: ")
    ans = input("Type in answer: ")

    # second string cannot be longer than first string
    if len(ans) > len(string):
        return False
    
    """ compare each letter of first and second strings
    if a number is reached, add the number to the index of the first string 
    i.e. skip X number of letters 
    this works because in the second string, the word will continue on immediately as the next letter
    e.g. helloperson and he3person
    the p continues immediately after the 3, so by adding to the index of helloperson, you can start
    comparing the p's 
    at the end, check that the end of the first string has been reached """
    i = 0
    for char in ans:
        if char.isdigit():
            i += int(char) -1
            if i >= len(string):
                return False
        else:
            if char != string[i]:
                return False
        i += 1
    if i != len(string):
        return False
    return True
    # for letter in string:
        # check each letter in answer and og string
        # when u reach number e.g. 3
        # skip the checks

def main():
    if validString():
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
   main()
