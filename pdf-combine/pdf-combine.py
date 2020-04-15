## based on # rotate_pages.py

from PyPDF2 import PdfFileReader, PdfFileWriter

def combine_pages(pdf_path, zaObrniti, zaIzvzeti):
    pdf_reader = PdfFileReader(pdf_path)

    steviloStrani = pdf_reader.numPages

    for stran in range (steviloStrani):
        if (stran+1) in zaIzvzeti:
            continue # Strani ne dodajamo, ker ni potrebe
        elif (stran+1) in zaObrniti: # Obrnemo stran za 180 stopinj
            pdf_writer.addPage(pdf_reader.getPage(stran).rotateCounterClockwise(180))
        else:
            pdf_writer.addPage(pdf_reader.getPage(stran))


if __name__ == '__main__':
    outName = "combined-output.pdf" ## Output file name
    datoteke = [{"path": "input-file-1.PDF",
                 "obrni": [22, 40],
                 "izvzemi": [34, 44]},

                {"path": "input-file-2.PDF",
                 "obrni": [],
                 "izvzemi": []},

                {"path": "more-files....PDF",
                 "obrni": [],
                 "izvzemi": [6, 8]}]

    pdf_writer = PdfFileWriter()

    for d in datoteke:
        combine_pages(d["path"], d["obrni"], d["izvzemi"])

    with open(outName, 'wb') as fh:
        pdf_writer.write(fh)
