'''
MIT License

Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk).
Project: Harmony (https://harmonydata.ac.uk)
Maintainer: Thomas Wood (https://fastdatascience.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

from harmony.parsing.text_parser import convert_text_to_instruments
from harmony.parsing.util.tika_wrapper import parse_pdf_to_plain_text
# from harmony.parsing.util.tesseract_wrapper import parse_image_pdf_to_plain_text
# from harmony.parsing.util.camelot_wrapper import parse_pdf_to_tables
from harmony.schemas.requests.text import RawFile, Instrument

def convert_pdf_to_instruments(file: RawFile) -> Instrument:
    # file is an object containing these properties:
    # content: str - The raw file contents so if it's a PDF this is a byte sequence in base 64 encoding
    # text_content: str - this is empty but we will use Tika to populate this in this method
    # tables: list - this is a list of all the tables in the document. The front end has populated this field.

    if not file.text_content:
        file.text_content = parse_pdf_to_plain_text(file.content) # call Tika to convert the PDF to plain text

    # TODO: New PDF parsing algorithm should go here, together with return statement.

    return convert_text_to_instruments(file)
