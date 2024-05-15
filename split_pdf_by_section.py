from typing import Dict, Union
from pypdf import PdfReader, PdfWriter
import re

def bookmark_dict(bookmark_list, reader, **kw):
    result = kw.get('result', {})
    use_labels = kw.get('use_labels', False)
    for item in bookmark_list:
        if isinstance(item, list):
            bookmark_dict(item, reader, use_labels=use_labels, result=result)
        else:
            if "Table" not in item.title:
                page_index = reader.get_destination_page_number(item)
                page_label = reader.page_labels[page_index]
                key = page_label if use_labels else page_index
                if key not in result:
                    result[key] = []
                result[key].append(dict(title=item.title, page=key))
    print(result)
    return result
def split_and_save(result, reader):
    pdf_writer = PdfWriter()
    current_section = None
    for key, value in sorted(result.items(), key=lambda n: f"{str(n[0]):>5}"):
        for item in value:
            valid_filename = re.sub(r'[<>:"/\\|?*]', '_', item['title'])
            if '.' in valid_filename and valid_filename.split('.')[0].isdigit():
                section_title = f"Section {valid_filename.split('.')[0]}.0"
            else:
                section_title = valid_filename
            if current_section is None or section_title != current_section:
                if current_section is not None:
                    with open(f"./pdfs/{current_section}.pdf", 'wb') as output_file:
                        pdf_writer.write(output_file)
                pdf_writer = PdfWriter()
                current_section = section_title
            pdf_writer.add_page(reader.pages[key])
    if current_section is not None:
        with open(f"./pdfs/{current_section}.pdf", 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    reader = PdfReader("./RFP.pdf")
    bms = bookmark_dict(reader.outline, reader)
    split_and_save(bms, reader)