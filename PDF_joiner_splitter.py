"""
PDF Joiner/Splitter Script

It can be used for joining several PDF files together.
Specific pages of each PDF files can be selected. Thus, it can be used also for splitting PDF file.
"""

from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
merger.append('1', pages=(11, 15))
merger.append('2', pages=(11, 15))
merger.append('3', pages=(11, 15))

merger.write("final_pdf.pdf")
merger.close()