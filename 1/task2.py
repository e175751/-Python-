import os

def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    count = 0
    for i in range(1,len(caps)):
        if caps[i] == 'B': count += 1
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('People in positions',i ,end='')
            else:
                if count == 1:
                    print(' flip your caps!')
                    count = 0
                else:
                    print(' through', i-1, 'flip your caps!')
                    count = 0

if __name__ == "__main__":

    cap1 = ['F','F','B','B','B','F','B','B','B','F','F','B','F']
    cap2 = ['F','F','B','B','B','F','B','B','B','F','F','F','F']
    cap4 = ['F','B','F','B','F','B','F','B','F','B','F','B','B']
    pleaseConformOnepass(cap1)

