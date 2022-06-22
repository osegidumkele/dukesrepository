#Dumkele Osegi, PSID 1894081
string1 = input("")
#strings to hold word values
string2 = string1.replace(" ", "") 
#setting bool value
aPalindrome = True
#checking to see if wor
i, j = 0, len(string2)-1
#loop while int i < j
while i < j:
#if first and last char of word is different then break
    if string2[i] != string2[j]:

        aPalindrome = False

        break

    i += 1
    j -= 1

if aPalindrome:

    print("{} is a palindrome".format(string1))

else:

    print("{} is not a palindrome".format(string1))



