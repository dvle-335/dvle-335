import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import sys
import json
import re
import requests

def create_bib_file(newname):
#creating a new file, automatic skip if the new file is already existed
    namefile, fileform = newname.split('.')
    if 'bib' not in fileform:
        sys.exit('Not correct fileform.')
    try:
        open(newname,'x')
    except FileExistsError:
        pass
def read_bib_file(newfile):
#open the new input file contain citations
    if newfile == '':
        sys.exit('No file name provided.')
    elif '.bib' not in newfile:
        newfile = newfile+'.bib'
    try:
        with open(newfile) as file:
            citedata = bibtexparser.load(file)
    except FileNotFoundError:
        sys.exit('File does not exist.')
    return citedata

def journal_name_format(name_in, mark = 'unknown title'):
#read out a journal name and output the abbreviated version.
#the journal abbreviation is based on the datafile journals.json from better.bib
#the customizee_journal.json is for customized abbreviation in case of no matches found.
    with open('/workspaces/dvle-335/abbreviations/journals.json') as file:
        main_dat = json.load(file)
#this is the main file that contain all the journal name
#original code is from https://github.com/jxhe/bib-journal-abbreviation
    with open('/workspaces/dvle-335/abbreviations/customize_journal.json') as file:
        sup_dat = json.load(file)
#this is a secondary file for adding missing journal name
    if re.search(r'^([a-zA-Z]+\.?\s?)*(?:\:?\s?)([a-zA-Z]+\.\s?)+$', name_in.strip()) is None:
        try: 
            name_out = main_dat[name_in]
        except KeyError:
            try:
                name_out = sup_dat[name_in]
            except KeyError:
                name_out = name_in
                print('Journal name not found in database for:', mark)
                pass
    else: 
        name_out = name_in
    return name_out

def name_process(name):
#this code specfically deal with wrong name format, a.k.a author name got stick together in a string.
    newname = re.sub(r'(\w+)([A-Z]\w+)',r'\2,\1',name)
    return newname

def cite_sort(citedata_in):
#take an input as the bibdata object, output the version that only contain relevent information.
    list_data = [
    'title','author','journal','year','number','pages','volume','ID','ENTRYTYPE','doi','month','abstract','school','publisher', 'institution' 
    ]
#print(citedata_in) #check format of citedata_in
    citedata_out = BibDatabase()
    cite_dummy = {}
    for cite_in in citedata_in.entries:
        for i, n in enumerate(list_data):
            try:
                cite_dummy.update({list_data[i] : cite_in[n]})
            except KeyError:
                pass
#replace unformated name with formated name, if not found journal name, skip this step.
        try:
            cite_dummy['journal'] = journal_name_format(cite_dummy['journal'], cite_dummy['title'])
        except KeyError:
            pass
        try:
            cite_dummy.update({'abstract' : cite_in['abstractnote']})
        except KeyError:
            pass
        try:
            if re.search(r'[a-zA-Z]+\.',cite_in['school']) is None:
                cite_dummy.update({'school' : (cite_in['school']+'.')})
        except KeyError:
            pass
        citedata_out.entries.append(cite_dummy)
        cite_dummy = {}
    return citedata_out

def cite_filter(citedata_in,filterpara='title'):
#remove duplicate citation from bibdata object, do so through different filter, default filter is 'title'
    namecheck = list()
    list_data = [
    'title','author','ID'
        ]
    if filterpara not in list_data:
        sys.exit('Incorrect filter parameter')
    citedata_out = BibDatabase()
    for inputentry in citedata_in.entries:
        if inputentry['title'] not in namecheck:
            citedata_out.entries.append(inputentry)
            namecheck.append(inputentry[filterpara])
    return citedata_out

def cite_add(cite_data1, cite_data2):
# add two bibdata object together, double check for possible duplicates and format the final file output with cite_sort and cite_filter.    
    for entry in cite_data2.entries:
        cite_data1.entries.append(entry)
    cite_out = cite_sort(cite_filter(cite_data1))
    return cite_out

def cite_request(input_doi):
#request a citation list from crossref api, using input doi
    list_entrytype = {
        'journal-article' : 'article',
        'book' : 'book',
        'book-chapter' : 'inbook',
        'proceedings-article' : 'inproceedings',
        'proceedings' : 'proceedings',
        'report' : 'techreport',
        'dataset' : 'misc',
        'posted-content' : 'misc',
        'monograph' : 'book'
    }
 #   list_data = [
 #   'title','author','journal','year','number','pages','volume','ID','ENTRYTYPE','doi','month','abstract','publisher', 'institution' 
 #   ]
    cite_out = BibDatabase()
    cite_dummy = {}
#based on doi look for the journal online and retrive its citation, formated, as an output bibtex object.
    try:
        url = f'https://api.crossref.org/works/{input_doi}'
        response = requests.get(url)
        cite_item = response.json()['message']
        #print(cite_item)
        cite_dummy.update({'title' : cite_item['title'][0]})
        author_name = cite_item['author']
        authorf_name = ''
        for name in author_name:
            authorf_name = authorf_name + name['given'] + name['family'] + ' and ' 
        cite_dummy.update({'author' : name_process(authorf_name[:-5])})
        cite_dummy.update({'volume' : cite_item['volume']})
        try:
            cite_dummy.update({'journal' : journal_name_format(cite_item['short-container-title'][0],cite_item['title'][0])})  
        except IndexError:
            cite_dummy.update({'journal' : journal_name_format(cite_item['container-title'][0],cite_item['title'][0])})  
        try: 
            cite_dummy.update({'pages' : cite_item['page']})
        except KeyError:
            cite_dummy.update({'pages' : cite_item['article-number']})
        cite_dummy.update({'doi' : cite_item['DOI']})
        try:
            cite_dummy.update({'year' : str(cite_item['published-print']['date-parts'][0][0])})
        except KeyError:
            cite_dummy.update({'year' : str(cite_item['published']['date-parts'][0][0])})
        try:
            cite_dummy.update({'month' : cite_item['month']})
        except KeyError:
            pass
        try:
            cite_dummy.update({'ENTRYTYPE' : list_entrytype[cite_item['type']]})
        except KeyError:
            sys.exit('entry type not found')
        if cite_item.get('abstract') is not None:
            new_abstract = re.sub(r"<[^>]+>",'',cite_item.get('abstract'))
            cite_dummy.update({'abstract' : new_abstract})
        cite_dummy.update({'ID' : cite_item['DOI']})
        cite_out.entries.append(cite_dummy)
        return cite_out
    except requests.exceptions.JSONDecodeError:
        print('No data found')
        cite_out = None

def main():
 #   create_bib_file('test.bib')
    input_file = read_bib_file(input('Read citation from file: '))
    output_name = input('Write citation to file: ')
    if '.bib' not in output_name:
        output_name = output_name + '.bib'
    create_bib_file(output_name)
    output_file = read_bib_file(output_name)
    writer = BibTexWriter()
    cite_output = cite_add(input_file,output_file)
    with open(output_name,'w') as f:
        f.write(writer.write(cite_output))
        print(f'Finished write citation to file',output_name)
    
if __name__ == "__main__":
    main()