# PDF_combine
Combine (merge) multiple PDF-files, rotate some pages for 180 degrees and exclude some pages.<br/>

## Usage
### Syntax 
After `import pdf_combine`, use its `combine(str outName, list inFiles)` function, where<br/>
* `outName` is a raw string with the path of the output file, e. g. `r"C:\Users\outputfile.pdf"`<br/>
* `inFiles` is a list of dictionaries with `path`, `rotate90`, `rotate180`, `rotate270` and `exclude` for each, where
  * `path` is a raw string with the path of the output file<br/>
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
