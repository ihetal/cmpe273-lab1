# Lab 1

Use any kind of [External Sorting](https://en.wikipedia.org/wiki/External_sorting) algorithm to sort all numbers from input/unsorted_*.txt files and save the sorted result into output/sorted.txt file amd async_sorted.txt file.

# Requirements

Implement your solution with or without [Asyncio](https://docs.python.org/3/library/asyncio.html).

* ext_merge_sort.py
* async_ext_merge_sort.py (uses Asyncio)

Finally, measure each execution time via

```sh
time python3 ext_merge_sort.py
time python3 async_ext_merge_sort.py
```

List of Files:

1. [ext_merge_sort.py](https://github.com/ihetal/cmpe273-lab1/blob/master/ext_merge_sort.py)
2. [async_ext_merge_sort.py](https://github.com/ihetal/cmpe273-lab1/blob/master/async_ext_merge_sort.py)
3. [all unsorted_*.txt files](https://github.com/ihetal/cmpe273-lab1/tree/master/input)
4. [all sorted_.txt files](https://github.com/ihetal/cmpe273-lab1/tree/master/output)
4. [time.txt](https://github.com/ihetal/cmpe273-lab1/blob/master/time.txt) and [async_time.txt](https://github.com/ihetal/cmpe273-lab1/blob/master/async_time.txt)



