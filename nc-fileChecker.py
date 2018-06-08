from os import walk
from io import StringIO
import json

dir = '/media/yoz/34100F45100F0D94/py/apps/'

def load_json(file):
    io = open('ex.json')
    return(json.load(io))
    io.close()

checklist = load_json('ex.json')
missingList = {}

missing = []

for fileList in walk(dir):

    for fileName in checklist.values():

        if fileName in fileList[2]:

            if fileName in missingList.keys():
                missingList[fileName] += 1
            else:
                missingList[fileName] = 1

        else:
            if not fileName in missingList.keys():
                missingList[fileName] = 0

print('Result:')
for key in missingList.keys():
    if missingList[key] == 0:
        print(f'{key} is missing. Alert!')
    elif missingList[key] > 1:
        print(f'{key} has duplicates. Alert!')
    else:
        print(f'{key} is found {missingList[key]} times.')
