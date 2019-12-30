import os
def pleaseConform(caps):
    start = forword = backword = 0
    intervals = []
    for i in range(1,len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start,i-1,caps[start]))
            if caps[start] == 'F':
                forword += 1
            elif caps[start] == 'B':
                backword += 1
            else:
                pass
            start = i
    intervals.append((start, len(caps)-1, caps[start]))
    print(intervals)
    if caps[start] == 'F':
        forword += 1
    elif caps[start] == 'B':
        backword += 1
    else:
        pass
    if forword < backword:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
                print('Pepple at position', t[0], 'flip your caps!')
            else:
                print('People in positions', t[0], 'through', t[1], 'flip your caps!')

if __name__ == "__main__":
    cap3 = ['F','F','B','H','B','F','B','B','B','F','H','F','F']
    pleaseConform(cap3)


