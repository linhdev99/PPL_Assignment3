x = [['a', 'b', [1, 23, [3, 4,[3,4,5,6,[65,65,[54]]]]]], ['c']]
y = [1,2,3]
print(x)
def extList(lst):
    ele = []
    if not isinstance(lst, list):
        return lst
    else:
        for x in lst:
            if isinstance(x, list):
                ele.extend(extList(x))
            else:
                ele.append(x)
        return ele

print(extList(y))
