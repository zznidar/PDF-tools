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


## Note
If you are running Python from Windows Command Prompt, please note that cmd [is known to change characters when pasting](https://stackoverflow.com/questions/64707661/cmd-converts-em-dash-to-hyphen-on-pasting-any-workaround), e. g. if you paste a path/filename containing an en-dash (–), cmd will change it to a hyphen (-) without notice and you will get a FileNotFound error.
