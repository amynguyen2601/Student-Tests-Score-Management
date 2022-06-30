#xử lý logic lien quann tới đốii tượng Student
from dbprovider import writeStudent, writeStudents, readStudents, getStudentByCode, checkExistsStudent

def bswriteStudent(st:dict):
    writeStudent(st)

def bswriteStudents(sts: list):
    writeStudents(sts)

def bsreadStudents():
    return readStudents()

def bsCheckExistsStudent(code:str):
    return checkExistsStudent(code)

def bsgetStudentbyCode(code:str):
    return getStudentByCode(code)

