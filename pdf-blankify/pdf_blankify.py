# Based on pdf_combine.py
from PyPDF2 import PdfFileReader, PdfFileWriter


def blankify(outName, inFile, start, step, blanks_per_step, end=float("Inf")):
    """
    Add blank pages into the PDF-file
    
    :param str outName: output path/filename (prefix string with r to make it raw)
    :param str inFile: input path/filename (prefix string with r to make it raw)
    :param int start: first page after which to add a blank page
    :param int step: per how many pages to add blank pages
    :param int blanks_per_step: how many blank pages to add each time
    :param int end (optional): after this page, do not add any more blank pages (I guess, never tried it)
    
    :raises SyntaxError (unicode error): if paths not prefixed with r
    """


    ## Convert 1-based input to 0-based pages
    start -= 1
    end -= 1
    
    global pdf_writer
    pdf_writer = PdfFileWriter()

    pdf_reader = PdfFileReader(inFile)
    numOfPages = pdf_reader.numPages

    for page in range (numOfPages):
        pdf_writer.addPage(pdf_reader.getPage(page))
        
        if(page >= start and page < end and (page - start)%step == 0):
            for s in range(blanks_per_step):
                pdf_writer.addBlankPage()
                
    with open(outName, 'wb') as fh:
        pdf_writer.write(fh)
