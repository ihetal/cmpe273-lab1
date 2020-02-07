import glob
import time
import asyncio
async def main():
    start = time.perf_counter()
    q = asyncio.Queue()
    #input_Data = await read_Files()
    inputFiles = glob.glob("input/*.txt")
    input_Data = [asyncio.create_task(read_Files(file,q)) for file in inputFiles]
    task = asyncio.create_task(sort(input_Data,q))
    await asyncio.gather(*input_Data)
    await q.join()
    await asyncio.gather(*task)
    result = await q.get()
    write_result(result)
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")

async def read_Files(file,q: asyncio.Queue):

    with open(file, "r") as f:
        temp =[]
        for line in f.readlines():
            temp.append(int(line.strip()))
        temp.sort()
        await q.put(temp)
        q.task_done()

async def sort(input_Data,q: asyncio.Queue):
    while q.qsize()>1:
        list1 =await q.get()
        list2 = await q.get()
        merged_File =sortedMerge(list1,list2)
        await q.put(merged_File)
        q.task_done()
    
def write_result(output):
    file =open('output/async_sorted.txt','w+')
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
    asyncio.run(main())





