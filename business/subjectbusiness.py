#xử lý logic lien quann tới đốii tượng Subject
from dbprovider import checkExistsSubject, writeSubject, writeSubjects, readSubject, getSubjectByCode

def bswriteSubject(st:dict):
    writeSubject(st)

def bswriteSubjects(sts: list):
    writeSubjects(sts)

def bsreadSubject():
    return readSubject()

def bsCheckExistsSubject(subjectCode:str):
    return checkExistsSubject(subjectCode)

def bsgetSubjectByCode(code:str):
    return getSubjectByCode(code)

