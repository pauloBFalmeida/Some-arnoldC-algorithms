filename = input("name without .obj of the file")
vertex = []
faces = []

with open(filename+'.obj', 'r') as file:
    lines = file.read()
    for l in lines.split('\n'):
        if len(l) > 1:
            if l[0] == 'v':
                newL = ""
                keep = False
                for c in l:
                    if c == ".":
                        keep = False
                    if c == " ":
                        keep = True
                    if keep:
                        newL += c
                v = tuple(newL.split(' '))
                vertex.append(v)
            if l[0] == 'f':
                newL = ""
                keep = False
                for c in l:
                   if c == "/":
                        keep = False
                   if c == " ":
                       keep = True
                   if keep:
                       newL += c
                f = tuple(newL.split(' '))
                faces.append(f)




