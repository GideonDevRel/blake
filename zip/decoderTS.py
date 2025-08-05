filename = "ts2.txt"
mapper = {}   # Define an empty dictionary object

"""
The following mappings will allow you to modify the decoding process.
After you run a frequency analysis, you will have the most common letter in your
encoded text.  Suppose the letter Q is the most common in the encoded text. We
would expect that to be the letter E.  In the mapping below, change the E INSIDE
the mapper to a Q.  In other words, the first line would read:
mapper['Q']='E' and so on.  Ensure that each letter only occurs once inside the brackets.
So the Q (second up from the bottom) would need to change.

"""

mapper['I']='E'    # Expected 12.7%
mapper['B']='T'    # Expected 9.1%
mapper['E']='A'    # Expected 8.2%
mapper['W']='O'    # Expected 7.5%
mapper['R']='I'    # Expected 7.0%

mapper['H']='H'    # Expected 6.7%
mapper['M']='N'    # Expected 6.3%
mapper['P']='S'    # Expected 6.1%
mapper['O']='D'    # Expected 6.0%
mapper['Y']='R'    # Expected 4.3%

mapper['C']='L'    # Expected 1.0%
mapper['V']='U'    # Expected 2.8%
mapper['U']='M'    # Expected 2.8%
mapper['J']='W'    # Expected 2.4%
mapper['Q']='Y'    # Expected 2.4%

mapper['A']='C'    # Expected 2.2%
mapper['N']='F'    # Expected 2.0%
mapper['T']='B'    # Expected 2.0%
mapper['S']='G'    # Expected 1.9%
mapper['F']='P'    # Expected 1.5%

mapper['l']='K'    # Expected 1.0%
mapper['K']='V'    # Expected .8%
mapper['D']='J'    # Expected .15%
mapper['X']='X'    # Expected .15%
mapper['G']='Q'    # Expected .1%

mapper['Z']='Z'    # Expected .07%

f=""

while (f=="" or f=="error"):  #NOTE: Filename cannot be "error"
    #filename = input("What is the name of the file to open? ")
    try:
        f=open(filename)
    except:
        f="error"
        
intext = ""      
outtext = ""
for lett in f.read():
    if lett.upper() in mapper.keys():
        lett = lett.upper()
        intext += lett
        outtext += mapper[lett]
        
f.close()
print(intext)
print(outtext)