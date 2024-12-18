# imported PdfMerger package from PyPDF2 
from PyPDF2 import PdfMerger

# storing PfgMerger Function in merger variable
merger = PdfMerger()

#creating pdfs Array/List
pdfs = ["A.pdf","B.pdf"]

# loop over the pdfs list
for pdf in pdfs:
    #adding pdf by append method
    merger.append(pdf)
merger.write("Merged.pdf")
merger.close()
