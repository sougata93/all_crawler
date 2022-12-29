import sys
from PyPDF2 import PdfFileReader,PdfFileWriter
import re
import os

def nlChecker(nlText):
    if re.search(r'nl-\d{1,2}',nlText.lower()) or re.search(r'nl\d{1,2}',nlText.lower()) or re.search(r'nl \d{1,2}',nlText.lower()):
        return True
    else:
        return False
def nlRename(nlText):
    if re.search(r'nl-\d{1,2}',nlText.lower()):
        return re.findall(r'nl-\d{1,2}',nlText.lower())[0]
    elif re.search(r'nl\d{1,2}',nlText.lower()):
        return re.findall(r'nl\d{1,2}',nlText.lower())[0]
    elif re.search(r'nl \d{1,2}',nlText.lower()):
        return re.findall(r'nl \d{1,2}',nlText.lower())[0]
    else:
        return '0'
def PDFsplit(pdf,cname,year):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    start=0
    end=0      
    count=0
    totalpages = pdfReader.numPages
    for i in range(totalpages):
        pdfWriter = PdfFileWriter()
        nlFinder=pdfReader.pages[i].extract_text()
        nlName=nlRename(nlFinder)
        print(nlName)
        
        outputpdf = pdf.split('.pdf')[0] + nlName + '.pdf'

        for page in range(count,count+1):
            if nlChecker(nlFinder):
                pdfWriter.addPage(pdfReader.getPage(page))
        count+=1
        p=os.path.join(year, cname+'_'+outputpdf)
        with open(p, "wb") as f:
            pdfWriter.write(f)
    pdfFileObj.close()

#inputs
def run(pdf,cname,year):
    PDFsplit(pdf,cname,year)
    

run('future_2022-23_2nd Quarter (JUL-SEP).pdf','future','22-23')



  