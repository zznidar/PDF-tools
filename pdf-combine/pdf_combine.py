## based on # rotate_pages.py
from PyPDF2 import PdfFileReader, PdfFileWriter


def combine_pages(pdf_path, toRotate, toExclude):
    pdf_reader = PdfFileReader(pdf_path)

    numOfPages = pdf_reader.numPages

    for page in range (numOfPages):
        if (page+1) in toExclude:
            continue # We skip this page (do not add it)
        elif (page+1) in toRotate: # Rotate page for 180 degrees
            pdf_writer.addPage(pdf_reader.getPage(page).rotateCounterClockwise(180))
        else:
            pdf_writer.addPage(pdf_reader.getPage(page))

def combine(outName, inFiles):
    """
    Combine multiple PDF-files
    
    :param str outName: output path/filename (prefix string with r to make it raw)
    :param list inFiles: input files as dicts [{"path": r"file1.pdf", "rotate": [22, 40], "exclude": [1,34, 44]}, ...]
    
    :raises SyntaxError (unicode error): if paths not prefixed with r
    """
    
    global pdf_writer
    pdf_writer = PdfFileWriter()

    for f in inFiles:
        combine_pages(f["path"], f["rotate"], f["exclude"])

    with open(outName, 'wb') as fh:
        pdf_writer.write(fh)
