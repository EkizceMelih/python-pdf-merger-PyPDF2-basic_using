from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()

pdf_merger.append("pdf1.pdf")
pdf_merger.append("pdf2.pdf")

pdf_merger.write("merged_pdf.pdf")
