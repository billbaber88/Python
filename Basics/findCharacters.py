



def listSearch(word_list, char):
    newList = []
    for x in range(0, len(word_list)):
        if word_list[x].find(char) != -1:
            newList.append(word_list[x])
    print newList

test_list = ['hello','world','my','name','is','Anna', 'and', 'i', 'work', 'around', 'your', 'house']
listSearch(test_list, 'o')
