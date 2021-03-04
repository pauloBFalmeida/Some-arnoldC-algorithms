filename = input("name without .obj of the file")
newLines = []

with open(filename+'.obj', 'r') as file:
    lines = file.read()
    for l in lines.split('\n'):
        if len(l) > 1:
            # save vertex as 0
            if l[0] == 'v':
                newL = "0"
                keep = False
                for c in l:
                    if c == ".":
                        keep = False
                    if c == " ":
                        keep = True
                    if keep:
                        newL += c
                newLines.append(newL)
            if l[0] == 'f':
                newL = "1"
                keep = False
                for c in l:
                   if c == "/":
                        keep = False
                   if c == " ":
                       keep = True
                   if keep:
                       newL += c
                newLines.append(newL)

with open(filename+'.txt', 'w') as file:
    for l in newLines:
        file.write(l+'\n')

