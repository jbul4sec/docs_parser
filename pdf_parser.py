from PyPDF2 import PdfReader


class PDFParser:

    @classmethod
    def get_title_or_description(cls, path_to_file: str, description: bool = False) -> str:
        """
        Returns title, i.e., first line, or description from the document at path_to_file
        :param description: choice between title and description
        :param path_to_file: path to file
        :return: title or description.
        """
        if not description:
            reader = PdfReader(path_to_file)
            title = reader.pages[0].extract_text().split('\n')[0:2]

            return title

        reader = PdfReader(path_to_file)
        descr = " ".join(reader.pages[0].extract_text().split('\n')[2:22])

        return descr
