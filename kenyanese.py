def decrypt(filename):
    cipher = {'y':'a', 'q':'z', 'e':'o', 'j':'u', 'p':'r', 'm':'l', 's':'n', 'l':'g', 'c':'e', 'k':'i', 'd':'s',
              'x':'m', 'u':'j', 'v':'p', 'n':'b', 'r':'t', 'i':'d', 'b':'h', 't':'w', 'a':'y', 'h':'x', 'w':'f',
              'f':'c', 'g':'v', 'o':'k', 'z':'q', " ":" "}
    text = []
    ctext = []
    file = open(filename, 'r')
    for line in file:
        text.append(line[:-1])
    file.close()   
    
    for z in text:
        if text.index(z) == 0:
           continue
        else:
           translist = [cipher.get(y) for y in list(z)]
           ctext.append('Case #' + str(text.index(z))+ ': ' +"".join(translist))
    for case in ctext:
        print(case)


