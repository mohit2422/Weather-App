# import PyPDF2
#
# pdfiles = ["sample1.pdf","sample2.pdf","sample3.pdf"]
# merger = PyPDF2.PdfMerger()
# for filename in pdfiles:
#     pdfFile = open(filename, 'rb')
#     pdfReader = PyPDF2.PdfReader(pdfFiles)
#     merger.append(pdfReader)
# pdfFile.close()
# merger.write('merged.pdf')

from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["sample1.pdf","sample2.pdf","sample3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()