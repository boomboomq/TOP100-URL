import os
import sys
import time
import findKthSmallest as KS

def topkURL(input_file, k):
    # build a HashMap
    frequencyMap = dict()
    with open(input_file, "r") as f:
        for url in f:
            freq = 1
            if url in frequencyMap:
                freq = frequencyMap[url]+1
            frequencyMap[url] = freq
    hash_size = sys.getsizeof(frequencyMap)
    print("The size of HashMap is %d bytes"%hash_size)
    
    # get a list of unique frequencies and find the kth largest frequency
    frequencies = []
    for value in frequencyMap.values():
        if value not in frequencies:
            frequencies.append(value)
    n = len(frequencies)
    kthLargestFreq = KS.kthSmallest(frequencies, 0, n-1, n-k)

    # remove records with frequency less than kth largest
    for key, value in frequencyMap.items():
        if value < kthLargestFreq:
            frequencyMap.pop(key)
    
    # sort by frequency and url name to get top k
    topK = sorted(frequencyMap.items(), key = lambda x:(-x[1], x[0]))[:k]
    for item in topK:
        print(item)

if __name__=="__main__":
    time_0 = time.time()
    DIRECTORY = ""
    input_file = os.path.join(DIRECTORY, "record_10e5.txt")
    topkURL(input_file, 100)
    time_1 = time.time()
    print("Total execution time is %.2f seconds"%(time_1-time_0))
