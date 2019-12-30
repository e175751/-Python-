import os

def Decryption(string): #暗号化
    word_list = []
    strings = ""
    for i in string:
        word_list.append(i)
    result = WordCheck(word_list)
    for i in result:
        num1,num2,string = i[0],i[1],i[2]
        renum = num2 - num1 + 1
        strings += str(renum) + string
    print(strings)

def Encryption(): #符号化
    pass


def WordCheck(List):
    words = []
    count = 0
    for i in range(1,len(List)):
        if List[count] != List[i]:
            words.append((count,i-1,List[count]))
            count = i
    words.append((count,len(List)-1,List[count]))
    return words

if __name__ == "__main__":
    strings = "BWWWWWBWWWW"
    Decryption(strings)
