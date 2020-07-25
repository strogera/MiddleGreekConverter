numerical=[]
description=[]
with open("./CharactersInfo", encoding="utf-8") as inpfile:
    for line in inpfile:
        if line[0] != '#':
            numerical.append(ord(line[0]))
            description.append(line[2:])
            #print(numerical[-1])
            #print(description[-1])

with open("./convData.py", "w+") as outfile:
    outfile.write("convDictoDescr={\n")
    for i, c in enumerate(numerical):
        outfile.write(str(c)+": \""+ description[i].replace("AND", "WITH").strip() + "\"") 
        if i!=len(numerical)-1:
                outfile.write(",\n")
        else:
                outfile.write("\n")
    outfile.write("}\n")
    outfile.write("convDictoCode={\n")
    for i, c in enumerate(numerical):
        outfile.write("\""+ description[i].replace("AND", "WITH").strip() + "\"" + " : "+ str(c)) 
        if i!=len(numerical)-1:
                outfile.write(",\n")
        else:
                outfile.write("\n")
    outfile.write("}")





