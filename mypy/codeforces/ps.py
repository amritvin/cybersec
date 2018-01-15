def compare(str1, str2):

    for i in range(0,len(str1)):
        if(str1.lower()[i]<str2.lower()[i]):
            return -1
        elif(str1.lower()[i]>str2.lower()[i]):
            return 1
    return 0
if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()

    print compare(str1,str2)
