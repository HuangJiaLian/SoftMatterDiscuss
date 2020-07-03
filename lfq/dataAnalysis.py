import numpy as np 

# Load all.csv
data = np.loadtxt('all.csv', delimiter = ',')
# Leave the last 10000 rows
# Remove the first 3 columns
data = data[-2000:, 3:]

print(data)
print(data.shape)

numRows = data.shape[0]
numAtomsPerGroup = 5
boxSize = 30
box = [30,30,30,90., 90., 90.]
print('Number of rows: {}'.format(numRows))

# Group
# Group Num: |0, 0, 0, 0, 0,| 1, 1, 1, 1, 1,|  ..., |399, 399, 399, 399, 399|.
# Position:  |0, 1, 2, 3, 4,| 0, 1, 2, 3, 4,|  ..., | 0,  1,   2,   3,   4|.
groupNumList = []
positionNumList = []
for i in range(numRows):
    groupNum = int(i/numAtomsPerGroup)
    groupNumList.append(groupNum)

    positionNum = i % numAtomsPerGroup
    positionNumList.append(positionNum)

# print(groupNumList[-20:], type(groupNumList))
# print(positionNumList[-20:], type(positionNumList))

# Convert list to np array
groupNumArray = np.array(groupNumList)
positionNumArray = np.array(positionNumList)

# print(groupNumArray, type(groupNumArray))
# print(positionNumArray, type(positionNumArray))

# Change shape from a row to a colum
groupNumArray = np.reshape(groupNumArray, (2000, 1))
positionNumArray = np.reshape(positionNumArray, (2000, 1))

# print(groupNumArray)
# print(positionNumArray)

# Concatenate groupNumArray, positionNumArray and data.
frameData = np.concatenate((groupNumArray, positionNumArray, data), axis=1)
# print(data)
# print(data[0:20,:]) # data[:20,:]
numGroups = int(groupNumArray.shape[0]/numAtomsPerGroup)
print('Number of groups: {}'.format(numGroups))

# print(frameData)

# Use a boolean mask to select one group. 
# https://stackoverflow.com/questions/58079075/numpy-select-rows-based-on-condition
def getOneGroupData(frameData, groupNum):
    mask = frameData[:, 0] == groupNum 
    return frameData[mask, :]

print(getOneGroupData(frameData, 2))

# Loop all group
numGroups = 4
for i in range(numGroups):
    headGroup = getOneGroupData(frameData, i)
    for j in range(numGroups):
        # `i != j` indicates group `i` is not group `j`
        if i != j:
            tailGroup = getOneGroupData(frameData, j)
            tailGroupXYZ = tailGroup[:,2:]
            # print(tailGroupXYZ.shape)
            # print(i, j)
            for k in range(numAtomsPerGroup):
                headAtom = headGroup[k,:]
                headAtomXYZ = headGroup[k,2:].reshape((1,-1))
                # print(headAtomXYZ.shape)
                # Get One-To-Five vectors
                vectors = headAtomXYZ - tailGroupXYZ
                print(vectors.shape)
                # Calculate lengths of vectors
                # -- To do @lfq --

                # Save data or other operation
                # -- To do @lfq --           


