import re

path ="archivo.txt"

try:
    archivo= open(path, 'r')
except:
    print ("el archivo no existe")
    quit()

texto= ""

for linea in archivo:
    texto += linea


print (texto)
print ("________________________________________________________________________________")


varia= r'([A-Za-z-_]+\s*[=|;])'
varir = re.findall(varia,texto)
print("\n ESTAS SON LAS VARIABLES:\n", varir)
print("\n")
print ("________________________________________________________________________________")

print("\n")
nente= r'[+,-]?[0-9]+'
ndeci = r'[[0-9]*[.]]?[0-9]+'
enteR = re.findall(nente,texto)
deciR = re.findall(ndeci,texto)
print("\n ESTOS SON LOS ENTEROS:\n", enteR)
print("\nESTOS SON LOS DECIMALES:\n", deciR)
print("\n")
print ("________________________________________________________________________________")

print("\n")
arit = r'[A-Za-z|0-9]+[+*/%-]+[A-Za-z|0-9|]'
aritR = re.findall(arit, texto)
print("ESTOS SON LOS OPERADORES ARITMETICOS: \n", aritR)
print("\n")
print ("________________________________________________________________________________")

print("\n")
rela = r'[A-Za-z|0-9]+\s*[|<|>|!=|<=|>=]+\s*[A-Za-z|0-9]+'
relaR = re.findall(rela, texto)
print("\n ESTOS SON LOS OPERADORES RELACIONALES: \n", relaR)
print("\n")
print ("________________________________________________________________________________")

print("\n")
reser = r'\b(false|def|if|raise|none|del|import|return|true|elif|int|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
reserR = re.findall(reser, texto)
print("\n ESTAS SON LAS PALABRAS RESERVADAS: ", reserR)
print ("")
print("\n")
print ("________________________________________________________________________________")