from pypdf import PdfReader
import os

file_path = "./docs/"

file_list = os.listdir(file_path)
for file in file_list:
    if file.endswith('.pdf'):
        pdf_file = open(file_path + file, 'rb')

        pdf_reader = PdfReader(pdf_file)
        x = len(pdf_reader.pages)
        pageobj = pdf_reader.pages[0]
        text = pageobj.extract_text()
        file_name = file.split(".")[0]
        with open(file_name + ".txt", "w", encoding='utf-8') as file:  # Specify the encoding
            file.writelines(text)
        file.close()  # Close the file after writing to it