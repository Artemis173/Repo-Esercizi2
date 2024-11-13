import os
import PyPDF2

#IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")

def CercaStringaInFileName(sFile,sString):
    return False

def CercaStringaInFileContent(sFilePathCompleto,sString):
    sOutFileName,sOutFileExt = os.path.splitext(sFilePathCompleto)
    if(sOutFileExt.lower()==".pdf"):
#print("Riconosciuto file pdf " + sFile)
        return CercaInFilePdf(sFilePathCompleto,sString)
    return False

def CercaInFilePdf(sFile,sString):
    print("Entro")
    sString = sString.lower()
    object = PyPDF2.PdfFileReader(sFile)
    numPages = object.getNumPages()
    print(f"Entro,  con pagine {numPages}")
    for i in range(0, numPages):
        pageObj = object.getPage(i)
        text = pageObj.extractText()
        text = text.lower()
        print(text)
        if(text.find(sString)!=-1):
            print("Trovata!!!")
            return True
    print(f"Non trovata {sString} in {sFile}")
    return False

def CercaStringaInFilename(sFilename,sStringaDaCercare):
    sFilename1 = sFilename.lower()
    sStringToSearch1 = sStringaDaCercare.lower()
    print("Cerco {0} in {1} ".format(sFilename1,sStringaDaCercare))
    iRet = sFilename1.find(sStringToSearch1)
    if(iRet>-1):
        print("Trovato")
        return True
    return False

#NAVIGA NEL FILE SYSTEM
for root, dirs, files in os.walk(sRoot):
    sToPrint = "Dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
    print(sToPrint)
    for filename in files:
        iRet = CercaStringaInFileName(filename,sStringaDaCercare)
        if(iRet == True):
            print("Trovato file: ",filename)
            iNumFileTrovati = iNumFileTrovati + 1
        else:
            sFilePathCompleto = os.path.join(root,filename)
            iRet = CercaStringaInFileContent(sFilePathCompleto,sStringaDaCercare)