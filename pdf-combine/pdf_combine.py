## based on # rotate_pages.py
from PyPDF2 import PdfFileReader, PdfFileWriter


def combine_pages(pdf_path, toRotate, toExclude, toRotate90, toRotate180, toRotate270):
    pdf_reader = PdfFileReader(pdf_path)

    numOfPages = pdf_reader.numPages

    for page in range (numOfPages):
        if (page+1) in toExclude:
            continue # We skip this page (do not add it)
        elif(page+1) in toRotate90:
            pdf_writer.addPage(pdf_reader.getPage(page).rotateClockwise(90))
        elif(page+1) in toRotate180:
            pdf_writer.addPage(pdf_reader.getPage(page).rotateClockwise(180))
        elif(page+1) in toRotate270:
            pdf_writer.addPage(pdf_reader.getPage(page).rotateClockwise(270))
        elif (page+1) in toRotate: # Rotate page for 180 degrees # Backwards-compatibility
            pdf_writer.addPage(pdf_reader.getPage(page).rotateCounterClockwise(180))
        else:
            pdf_writer.addPage(pdf_reader.getPage(page))

def combine(outName, inFiles):
    """
    Combine multiple PDF-files
    
    :param str outName: output path/filename (prefix string with r to make it raw)
    :param list inFiles: input files as dicts [{"path": r"file1.pdf", "exclude": [1,34, 44], "rotate90": [22, 40], "rotate180": [1, 2], "rotate270": [65, 33]}, ...]
    
    :raises SyntaxError (unicode error): if paths not prefixed with r
    """
    
    global pdf_writer
    pdf_writer = PdfFileWriter()

    for f in inFiles:
        combine_pages(f.get("path", {}), f.get("rotate", {}), f.get("exclude", {}), f.get("rotate90", {}), f.get("rotate180", {}), f.get("rotate270", {}))

    with open(outName, 'wb') as fh:
        pdf_writer.write(fh)
