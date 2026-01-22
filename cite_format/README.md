# CITATION FORMATTING 
#### Video demo: <https://youtu.be/XmSh6BJde6w>
#### Description:
I wrote this program to reduce the time i spent on looking and correcting citations manual for my thesis, since i will be handling hundreds of citations. There are two main part to my program. The 1st part is to process a citation file, and then either add it to an existing file, or create a new file for it. the 2nd part is to create citation from a doi, which is provided by all journals and publications. The 2nd part only selects important information from the json response based of the doi, and save it in a separate file. the format output from both programs are very similar and can be handled by standard bibbliography function in latex.

The program read and format citation using the bibtextparser package, which format all the bib file and turn it into a bib object, which can be easily formated, merged, and saved.

the first part of the program contains basic functions, such as: create_bib_file, read_bib_file, to read information from a file, save information to file.

The next program is journal_name_format. This program is used to reformat journal name, since not all bib file provided online has the correct journal name abbreviation. To solve that, I downloaded a data base of name and abbreviation, 'journals-json' and 'customize_journal.json', that contains thousands of journal names and their respective abbreviation. Based on these data bases, i can match any journal names to their respective abbreviations to easily format the journal name to the common citation format. The way the program check if each journal name needs formating is by using a regex check. in addition, i also flag journal name that happens to not in the data base, so i can manually add their abbreviation later. 

the next small program is the name_process program. This is to reformat author name slightly. This is just for json response collected directly from doi request, since the author name format in the response is a bit different from bibliography file. 

the 1st big program is cite_sort. The purpose of this program is to read data from a bib file, and reformat all the citations if needed, based on a list of relavent information, such as author name, journal, paper name, date of publication, etc... It makes use of the program journal_name_format to reformat some of the journal names to match with the standard citation format in a publication.

The next program is cite_filter. the purpose of this program is to remove redundant citations, by scanning certain parameters and find matching results. The set of parameter i used is title, author, and ID, and the default parameter used is title. The journal name is often unique afterall, same for ID. The author parameter can be a bit inaccurate, since sometimes bibbiography files of the same paper from different website can be written a bit differently, make it more difficult to recognize the same paper. 

The cite_add file makes use of all the program mentioned above, basically merges two bib objects from two different input file together, reformat and filter them if needed, and output 1 big bib object. This object will be saved later on.

In the main program, the 1st name requested is the name of the file that has citations you want to save and format, the 2nd name requested is the file that you wish to save to. This file can also be the file that already contains citation. Both file will be processed and the data will be saved to the 2nd file. If the 2nd file is not existed yet, it will be created and data will be save to that file. I also placed some error checks to notify if the name of the 1st file is provided incorrectly, or not provided at all.

the 2nd big program is the cite_request program. The purpose is to use a doi of a particular publication, and request a json response with that doi, containing all the necessary information to create a bibbiography for the corresponding publication. Overall, a lot of reformating is needed, since the information requested this way can be different from the standard citation format, and different from websites to websites. I placed an error check for no json response. The output file is a completely formatted bibiography, which can be used readily in latex, pasted directly into another bib file, or as input for the 1st program cite_add. 
