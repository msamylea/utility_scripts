from pdf2docx import parse
from typing import Tuple
import os

path = 
def convert_pdf2docx(pages: Tuple = None):
    """Converts PDF to DOCX"""
    for root, dirs, files in os.walk(path):
        # Iterate through each file in the current directory
        for file in files:
            # Check if the file has a .pdf extension
            if file.endswith('.pdf'):
                # Construct the full file path
                input_file = os.path.join(root, file)
                # Construct the output file path
                output_file = os.path.splitext(input_file)[0] + '.docx'
                if pages:
                    pages = [int(i) for i in list(pages) if i.isnumeric()]
                result = parse(pdf_file=input_file, docx_with_path=output_file, pages=pages)
                summary = {
                    "File": input_file,
                    "Pages": str(pages),
                    "Output File": output_file
                }
                # Printing Summary
                print("## Summary ########################################################")
                print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
                print("###################################################################")

if __name__ == "__main__":
    convert_pdf2docx()