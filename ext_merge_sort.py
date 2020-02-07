import glob
import time
def main():
    start = time.perf_counter()
    inputFiles = glob.glob("input/*.txt")
    input_Data =[]
    for file in inputFiles:
        with open(file, "r") as f:
            temp =[]
            for line in f.readlines():
                temp.append(int(line.strip()))
            temp.sort()
            input_Data.append(temp)
    result = sort(input_Data)
    write_result(result)
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
def sort(input_Data):
    no_of_files = len(input_Data)
    interval = 1
    while interval < no_of_files:
        for i in range(0, no_of_files - interval, interval * 2):
            input_Data[i] = sortedMerge(input_Data[i], input_Data[i + interval])
        interval *= 2
    return input_Data[0] if no_of_files > 0 else input_Data
    
def write_result(output):
    file =open('output/sorted.txt','w+')
    for number in output:
        file.write(str(number))
        file.write("\n")
        
def sortedMerge(list1, list2): 
    # Sorting a[] and b[] 
    i,j = 0,0
    n = len(list1)
    m =len(list2)
    merged = []
    while (i < n and j < m):
        if (list1[i] < list2[j]):
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while (i < n):
        merged.append(list1[i])
        i += 1
    while (j < m):
        merged.append(list2[j])
        j += 1
    return merged

if __name__ == '__main__':
    main()





