import sys, getopt
import codecs
import convData as data

def convertChar(c):
    # Rules are remove psili and varia
    # Macron and vrachy are extra but don't really matter
    if not (c in data.convDictoDescr.keys()):
        return c
    descriptionOfc=data.convDictoDescr[c]
    if "PSILI" in descriptionOfc:
        descriptionOfc=descriptionOfc.replace(" WITH PSILI", "")
    if "VARIA" in descriptionOfc:
        descriptionOfc=descriptionOfc.replace(" WITH VARIA", "")
    if not (descriptionOfc in data.convDictoCode.keys()):
        print("Letter \""+descriptionOfc+"\" is missing")
        return c
    return(data.convDictoCode[descriptionOfc])


def convertFile(inputFilePath, outputFilePath):
    with codecs.open(inputFilePath, "r", encoding='utf-8') as inputFile:
        with codecs.open(outputFilePath, "w+", encoding='utf-8') as outputFile:
            for line in inputFile:
                for c in line:
                    cc=convertChar(ord(c))
                    outputFile.write(chr(cc))

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
            print("convert.py -i <inputFile> -o <outPutFile>")
            sys.exit(2)

    if not opts:
        if len(argv)>=2:
            inputfile=argv[0]
            outputfile=argv[1]
        else:
            print("convert.py -i <inputFile> -o <outPutFile>")
            sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print("convert.py -i <inputFile> -o <outPutFile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print ('Input file is %s'%inputfile)
    print ('Output file is %s'%outputfile)
    convertFile(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
