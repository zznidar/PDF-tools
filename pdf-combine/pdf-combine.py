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


if __name__ == '__main__':
    outName = "combined-output.pdf" ## Output file name
    datoteke = [{"path": "input-file-1.PDF",
                 "rotate": [22, 40],
                 "exclude": [34, 44]},

                {"path": "input-file-2.PDF",
                 "rotate": [],
                 "exclude": []},

                {"path": "more-files....PDF",
                 "rotate": [],
                 "exclude": [6, 8]}]

    pdf_writer = PdfFileWriter()

    for d in datoteke:
        combine_pages(d["path"], d["rotate"], d["exclude"])

    with open(outName, 'wb') as fh:
        pdf_writer.write(fh)
