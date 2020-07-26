numerical=[]
description=[]

fonienta=['ALPHA', 'EPSILON', 'ETA', 'IOTA', 'OMICRON', 'UPSILON', 'OMEGA', 'RHO'] #there's rho with psili in the characters but I don't think it has any practical use

with open("./Unicode.Chars_Descr.Greek_and_GreekExtended", encoding="utf-8") as inpfile:
    for line in inpfile:
        if line[0] != '#':
            numerical.append(ord(line[0]))
            description.append(line[2:])

with open("./convData.py", "w+") as outfile:
    outfile.write("convDictoDescr={\n")
    for i, c in enumerate(numerical):
        for fonien in fonienta:
            if fonien in description[i]:
                outfile.write(str(c)+": \""+ description[i].replace("AND", "WITH").strip() + "\"") 
                if i!=len(numerical)-1:
                        outfile.write(",\n")
                else:
                        outfile.write("\n")
    outfile.write("}\n")
    outfile.write("convDictoCode={\n")
    for i, c in enumerate(numerical):
        for fonien in fonienta:
            if fonien in description[i]:
                outfile.write("\""+ description[i].replace("AND", "WITH").strip() + "\"" + " : "+ str(c)) 
                if i!=len(numerical)-1:
                        outfile.write(",\n")
                else:
                        outfile.write("\n")
    outfile.write("}")





