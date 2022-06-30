from dbprovider import writeScore, writeScores, readScore, getScoreByCode, checkExistsScore

def bsWriteScore(sc:dict):
    writeScore(sc)

def bsWriteScores(scs: list):
    writeScore(scs)

def bsReadScores():
    return readScore()

def bsGetScoreByCode(studentCode:str, subjectCode: str):
    return getScoreByCode(studentCode, subjectCode)

def bsCheckExistsScore(studentCode:str, subjectCode: str):
    return checkExistsScore(studentCode, subjectCode)
