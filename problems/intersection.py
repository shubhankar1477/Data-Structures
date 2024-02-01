'''Given two arrays return common elements from them

input1 = [1,2,3,4,5] input2 = [0,1,2,4]
output = [1,2,4]

'''

def get_common(l1,l2):
    l1 = set(l1)
    l2 = set(l2)

    final = []
    for i in l1:
        if i in l2:
            final.append(i)
    return final

def get_common_second(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    if len(l1) > len(l2):
        return [x for x in l1 if x in l2]
    else:
        return [x for x in l2 if x in l1]

if __name__ == '__main__':
    l1 = [1,2,3,4,5,11]
    l2 = [0,1,3,7,9,0,10,11]
    assert get_common_second(l1,l2) == [1,3,11]