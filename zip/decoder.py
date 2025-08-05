filename=""
#filename = "ts1.txt"    #Uncomment this to specify a file - useful for testing with the same input file
mapper = {}   # Define an empty dictionary object

"""
The following mappings will allow you to modify the decoding process.
After you run a frequency analysis, you will have the most common letter in your
encoded text.  Suppose the letter Q is the most common letter in the encoded text. We
would expect that to be the letter E.  In the mapping below, change the E INSIDE
the mapper to a Q.  In other words, the first line would read:
mapper['Q']='E' and so on.  This key-value mapping defines the substitution, so this is saying map Q -> E.

Ensure that each letter only occurs once inside the brackets - each key-value mapping should occur only once. So the Q (second up from the bottom)
would need to change based on the change above.

"""
mapper['J']='E'    # J=12.58% -> E=12.7%
mapper['E']='T'    # E=9.21% -> T=9.1%
mapper['L']='A'    # L=8.26% -> A=8.2%
mapper['A']='O'    # A=7.76% -> O=7.5%
mapper['M']='I'    # M=7.16% -> I=7.0%

mapper['U']='N'    # U=6.96% -> N=6.7%
mapper['X']='S'    # X=6.75% -> S=6.1%
mapper['V']='H'    # V=5.78% -> H=6.0%
mapper['D']='R'    # D=5.56% -> R=5.9%
mapper['C']='L'    # C=4.43% -> L=4.0%

mapper['G']='C'    # G=3.57% -> C=2.8%
mapper['B']='U'    # B=2.76% -> U=2.8%
mapper['Y']='M'    # Y=2.72% -> M=2.4%
mapper['R']='W'    # R=2.29% -> W=2.4%
mapper['F']='F'    # F=2.26% -> F=2.2%

mapper['S']='G'    # S=2.19% -> G=2.0%
mapper['Z']='P'    # Z=2.17% -> P=1.9%
mapper['I']='B'    # I=2.13% -> B=1.5%
mapper['K']='Y'    # K=1.97% -> Y=1.0%
mapper['H']='D'    # H=1.44% -> D=4.3%

mapper['W']='V'    # W=1.08% -> V=0.8%
mapper['T']='K'    # T=0.57% -> K=0.8%
mapper['N']='J'    # N=0.11% -> J=0.15%
mapper['Q']='Q'    # Q=0.11% -> Q=0.1%
mapper['P']='X'    # P=0.09% -> X=0.15%

mapper['O']='Z'    # O=0.07% -> Z=0.07%

f=""

while (f=="" or f=="error"):  #NOTE: Filename cannot be "error"
    if filename=="":
        filename = input("What is the name of the file to open? ")
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
print("Original Text",intext)
print("Decrypted Text",outtext)