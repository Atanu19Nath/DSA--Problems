
import string
def txt(s):
    lowercase_text = s.lower()
    list = []

    special_char = string.punctuation

    for i in lowercase_text:
        if i == ' ' or i in special_char:
            continue

        list.append(i)

    print(list)

    i = 0
    j = len(list) -1

    while(i < j):

        if list[i] != list[j]:
            return False
        i +=1
        j -=1

    return True



print(txt("h0!PnNp)0!H"))