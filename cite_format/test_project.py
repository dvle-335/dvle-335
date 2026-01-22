from cite_format.project import journal_name_format
from cite_format.project import name_process
from cite_format.project import cite_request

def test_journal_name1():
    assert journal_name_format('Journal of Chemical Physics') == 'J. Chem. Phys.'
def test_journal_name2():
    assert journal_name_format('Journal of Physical Chemistry') == 'J. Phys. Chem.'

def test_name_process1():
    assert name_process('JohnSmith') == 'Smith,John'
def test_name_process2():
    assert name_process('John,Smith') == 'John,Smith'
def test_name_process3():
    assert name_process('John, Smith') == 'John, Smith'

def test_cite_request():
    cite_request('nodoi') == None