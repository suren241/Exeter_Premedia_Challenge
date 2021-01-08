import csv
import time
import os, psutil
start = time.time()
dictionary={}
counter={}
uniquewords=set()
count=0
z=""
with open("E:/exeter project/french_dictionary.csv", "r") as file: #my system file location
    reader = csv.reader(file)
    for row in reader:
        dictionary[row[0]]=row[1]
f = open("E:/exeter project/find_words.txt", "r")
for x in f:
  x.rstrip('\n')
  counter[x.rstrip('\n')]=1
#reading the t8.shakespeare file and finding the number of times a word was replaced
with open('E:/exeter project/t8.shakespeare.txt','r') as file:    
    for line in file:
        for word in line.split():
            s=word
            temp=word.rstrip(',').rstrip('.').rstrip('\'').rstrip('!').rstrip(';').rstrip('\"')
            if(counter.get(temp) and dictionary.get(temp)):
                uniquewords.add(temp)
                counter[temp]=counter[temp]+1
                count+=1
                z+=s.replace(temp,dictionary[temp])+" "
            else:
                z+=s+" "
for k,v in counter.items():
     counter[k]=counter[k]-1
file1 = open('E:/exeter project/t8.shakespeare.txt', 'w')
file1.write(z)
file1.close()
end = time.time() 
process = psutil.Process(os.getpid()) 
print("Unique list of words that was replaced with French words from the dictionary\n")
print(uniquewords)
print("\nNumber of times a word was replace :")
print(count)
print("\nFrequency of each word replaced :")
print(counter)
print("\nTime taken to process :")
print(end-start)
print("\nMemory taken to process :")
print(process.memory_info().rss," bytes")
print("\nreplaced file")
print(z)
