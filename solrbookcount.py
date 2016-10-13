import urlopen
import PDFResourceManager, process_pdf
import TextConverter
import LAParams
import StringIO
import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = open("Solr.in.Action.pdf")
outputString = readPDF(pdfFile)
print(outputString)

pdfFile.close()