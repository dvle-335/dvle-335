import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import re
from project import name_process
from project import journal_name_format
from project import cite_request

def main():
    input_request = input('Extract citation? ')
    if re.search(r'^y',input_request.lower()):
        cite_extract_name = 'cite_extract.bib'
        path = '/workspaces/dvle-335/'
        doi_input = input('Your doi: ')
        result = cite_request(doi_input)
        try:
            writer = BibTexWriter()
            with open(path+cite_extract_name,'w') as f:
                f.write(writer.write(result))
            print(f'citation saved in file',cite_extract_name)
        except AttributeError:
            print(f'Cant save to file', cite_extract_name)
            pass
    elif re.search(r'^n',input_request.lower()):
        pass
    else:
        print('Unclear command')
if __name__ == '__main__':
    main()