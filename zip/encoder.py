"""
This use a mapping between the position in the alphabet variable to the same index position in mapper.
So initially A=E,B=T,C=A and so on.

To change how a text is encoded, simply rearrange the order of the mapper variable.

"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mapper = "ETAOINSHRDLCUMWFGYPBVKJXQZ"    
outfilename = "out2.txt"

f=""

while (f=="" or f=="error"):  #NOTE: Filename cannot be "error"
    filename = input("What is the name of the file to open? ")
    try:
        f=open(filename)
    except:
        f="error"
        
intext = ""      
outtext = ""
for lett in f.read():
    if lett.upper() in alphabet:
        lett = lett.upper()
        intext += lett
        outtext += mapper[alphabet.find(lett)]
    else:
        intext += lett
        outtext += lett
        
f.close()

f=open(outfilename,'w')
f.write(outtext)
f.close()
