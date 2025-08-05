alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
freq={}
totalLetters = 0

for lett in alphabet:
    freq[lett]=0
    
f=""

while (f=="" or f=="error"):
    #NOTE: Filename cannot be "error"
    filename = \
    input("What is the name of the file to open? ")
    
    try:
        f=open(filename)
    except:
        f="error"
        
for lett in f.read():
    if lett.upper() in alphabet:
        lett =lett.upper()
        freq[lett] += 1
        totalLetters += 1
        
sorted_freq = sorted(freq.items(), \
        key=lambda x: x[1], reverse=True)        
        
for i in sorted_freq:
    print(f"The letter {i[0]} occurred {i[1]} times," + \
          f"which is {100*i[1]/totalLetters:06.4f}%" \
          .format(i[0],i[1],100*i[1]/totalLetters))