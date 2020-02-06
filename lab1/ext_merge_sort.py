import os
import shutil

# CONSTANTS
tempDir = 'output'
inputDir = 'input'

def openFile(file):
    '''
        returns a list of lines from the opened file
    '''
    try:
        with open(file, 'r') as f:
            return [int(line.strip()) for line in f]
    except IOError as e:
        print(e)
        return []

def writeFile(data, dest):
    '''
        Writes the data into a file at the destination
        Expects data to be an iterabale of strings
    '''
    with open(dest, 'w') as f:
        f.write('\n'.join(data))

def quickSort(list, low, high):
    if low < high:
        partitionIndex = partition(list, low , high)
        quickSort(list, low, partitionIndex - 1)
        quickSort(list, partitionIndex + 1, high)
    
def partition(list, low, high):
    pivot = list[high]
    i = (low - 1)
    j = low
    while j <= high - 1:
        if list[j] < pivot:
            i += 1
            swap(list, i, j)
        j += 1
        
    swap(list, i+1, high)
    return i + 1

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def main():
    try:
        # create temporary directory
        if not os.path.isdir(tempDir):
            os.mkdir(tempDir)

        for file in os.listdir(inputDir):
            list = openFile('%s/%s' % (inputDir, file))
            quickSort(list, 0, len(list) - 1)

            # write sorted lists to temp files in temp dir
            tempFile = 'sorted_%s' % file.split('_')[-1]
            writeFile([str(line) for line in list], '%s/%s' % (tempDir, tempFile))

        sortedList = []
        for file in os.listdir(tempDir):
            if not file.startswith('async'):
                if not sortedList:
                    sortedList = openFile('%s/%s' % (tempDir, file))
                else:
                    list = openFile('%s/%s' % (tempDir, file))
                    sortedList.extend(list)
                    quickSort(sortedList, 0, len(sortedList) - 1)

        writeFile([str(line) for line in sortedList], '%s/sorted.txt' % tempDir)

    except Exception as e:
        print(e)

    
if __name__ == "__main__":
    main()