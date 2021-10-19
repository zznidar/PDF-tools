# PDF_combine
Combine (merge) multiple PDF-files, rotate some pages for 180 degrees and exclude some pages.<br/>

## Usage
### Syntax 
After `import pdf_combine`, use its `combine(str outName, list inFiles)` function, where<br/>
* `outName` is a raw string with the path of the output file, e. g. `r"C:\Users\outputfile.pdf"`<br/>
* `inFiles` is a list of dictionaries with `path`, `rotate90`, `rotate180`, `rotate270` and `exclude` for each, where
  * `path` is a raw string with the path of the input file<br/>
  * `rotate90` _(optional)_ is a list of pages (1-based) to rotate for 90 degrees clockwise<br/>
  * `rotate180` _(optional)_ is a list of pages (1-based) to rotate for 180 degrees clockwise<br/>
  * `rotate270` _(optional)_ is a list of pages (1-based) to rotate for 270 degrees clockwise<br/>
  * `exclude` _(optional)_ is a list of pages (1-based) to exclude<br/>
  
### Example
```python
import pdf_combine
pdf_combine.combine(r"C:\Users\Test\Downloads\combined-output.pdf",  [{"path": r"C:\Users\Test\Downloads\input-file-1.pdf",
                 "rotate90": [22, 40],
                 "rotate180": [1, 2],
                 "rotate270": [55, 56, 57, 58],
                 "exclude": [1,34, 44]},

                {"path": r"C:\Users\Test\Downloads\input-file-2.PDF",
                 "rotate90": [],
                 "exclude": []},

                {"path": r"C:\Users\Test\Downloads\more-files....PDF",
                 "rotate270": [3],
                 "exclude": [6, 8]}])
```

## Note
If you are running Python from Windows Command Prompt, please note that cmd [is known to change characters when pasting](https://stackoverflow.com/questions/64707661/cmd-converts-em-dash-to-hyphen-on-pasting-any-workaround), e. g. if you paste a path/filename containing an en-dash (–), cmd will change it to a hyphen (-) without notice and you will get a FileNotFound error.


# PDF_blankify
Add blank pages into the PDF-file  

## Usage
### Syntax
After `import pdf_blankify`, use its `blankify(outName, inFile, start, step, blanks_per_step, end)` function, where<br/>
* `outName` is a raw string with the path of the output file, e. g. `r"C:\Users\outputfile.pdf"`<br/>
* `inName` is a raw string with the path of the input file, e. g. `r"C:\Users\inputfile.pdf"`<br/>
* `start` is the first page after which to add a blank page<br/>
* `step` tells per how many pages to add blank pages<br/>
* `blanks_per_step` represents how many blank pages to add each time<br/>
* `end` _(optional)_ after this page, do not add any more blank pages (I guess, never tried it)<br/>

### Example
``` py
import pdf_blankify
pdf_blankify.blankify(r"C:\output-file.pdf", r"C:\input-file.pdf", 1, 3, 2)
# Starts after the first page, adds 2 blank pages every 3 pages
```