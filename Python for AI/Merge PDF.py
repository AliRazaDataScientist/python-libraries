from pypdf import PdfWriter
merge = PdfWriter()
for all in ['1.pdf','2.pdf','3.pdf','4.pdf']:
    merge.append(all)
merge.write('All-PDFs.pdf')
merge.close()