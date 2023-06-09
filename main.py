import os
from docx import Document
from docx_parser import DocxParser, DocxTable, fulfil_table
from pdf_parser import PDFParser


# ../../Documents/ОУД_СБПэй/20220830_ОУД4_СБПэй
# ../../Documents/ОУД_СБП/202220829_ОУД4_СБП


def main():
    print("<------------ Simple document parser ------------>")
    directory = input("[*] Enter the path to work directory --> ")
    columns = int(input("[*] Enter number of columns --> "))
    table_filename = input("[*] Enter file name for table --> ")

    doc_table = DocxTable(columns=columns, filename=table_filename)
    table_handler = doc_table.get_table()

    count = 0
    fulfil_table(count, "", "", "", table_handler)
    for file in sorted(os.listdir(path=directory), key=lambda x: int(x[11:14])):
        path = directory + '/' + file
        if file.endswith('.pdf'):
            title = PDFParser.get_title_or_description(path)
            description = PDFParser.get_title_or_description(path, description=True)
        elif file.endswith('.docx'):
            title, description = DocxParser.get_title_or_description(path)
        else:
            title = file
            description = f'Unknown type of file ---> {file}'
        count += 1
        fulfil_table(count, file, title, str(description), table_handler)

    doc_table.save_table()


if __name__ == '__main__':
    main()
