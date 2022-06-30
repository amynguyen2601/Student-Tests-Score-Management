#Giao tiếp (vào/ra) dữ liệu với các tệp .txt

studentPath = 'database/student.txt'
subjectPath = 'database/subject.txt'
scorePath = 'database/score.txt'

## STUDENT
def writeStudent(st:dict):
    '''Ghi object st vao trong file student.txt
    {
        'Code': 'PY0301'
        'FullName: 'Vu Thanh Van',
        'Birthday':'01/02/2000',
        'Sex': 0,
        'Address':'Ha Noi',
        'Phone': 0977999777,
        'Email':'vvu@gmail.com
    }
    '''
    with open(studentPath,'a',encoding = 'utf-8') as f:
        line: str = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
        f.write(line)

def writeStudents(sts: list):
    '''Ghi object sts vao trong file student.txt
    [{
        'Code': 'PY0301'
        'FullName: 'Vu Thanh Van',
        'Birthday':'01/02/2000',
        'Sex': 0,
        'Address':'Ha Noi',
        'Phone': 0977999777,
        'Email':'vvu@gmail.com
    }, ...]
    '''
    with open(studentPath,'w',encoding = 'utf-8') as f:
        for st in sts:
            line: str = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
            f.write(line)

def readStudents():
    ''' Doc list[dict] tu file Student.txt'''
    sts = []
    with open(studentPath,'r',encoding = 'utf-8') as f:
        for line in f:
            if line is None: 
                break

            value = line.strip().split('|')
            st = {
                'Code':     value[0],
                'FullName': value[1],
                'Birthday': value[2],
                'Sex':      value[3],
                'Address':  value[4],
                'Phone':    value[5],
                'Email':    value[6]
            }
            sts.append(st)
    return sts

def getStudentByCode(code:str):
    result = None       #ban đầu set trạng thái là không tìm thấy
    with open(studentPath, 'r',encoding= 'utf-8') as f:
        for line in f:
            if line is None:
                break

            value = line.strip().split('|')
            if value[0] == code:    #nếu dòng nào có code == code đầu vào thì lấy giá trị của dòng đó và dừng lại việc tìm kiếm\
                result = {
                    'Code':     value[0],
                    'FullName': value[1],
                    'Birthday': value[2],
                    'Sex':      value[3],
                    'Address':  value[4],
                    'Phone':    value[5],
                    'Email':    value[6]
                }
                break
    return result

def checkExistsStudent(code:str):
    result = False
    with open(studentPath,'r',encoding='utf-8') as f:
        for line in f:
            if line is None:
                break
            value = line.strip().split('|')
            if value[0] == code: #nếu dòng nào có code == code đầu vào thì lấy giá trị của dòng đó và dừng lại việc tìm kiếm
                result = True
                break
    return result

## SUBJECT
def writeSubject(st:dict):
    '''Ghi object st vao trong file subject.txt
    {
        'Subject Code': '1101'
        'Subject Name': 'Python'
    }
    '''
    with open(subjectPath,'a',encoding = 'utf-8') as f:
        line: str = f"{st['Subject Code']}|{st['Subject Name']}\n"
        f.write(line)

def writeSubjects(sts: list):
    '''Ghi object sts vao trong file subject.txt
    [{
        'Subject Code': '1101'
        'Subject Name': 'Python'
    }, ...]
    '''
    with open(subjectPath,'w',encoding = 'utf-8') as f:
        for st in sts:
            line: str = f"{st['Subject Code']}|{st['Subject Name']}\n"
            f.write(line)

def readSubject():
    ''' Doc list[dict] tu file subject.txt'''
    sts = []
    with open(subjectPath,'r',encoding = 'utf-8') as f:
        for line in f:
            if line is None: 
                break

            value = line.strip().split('|')
            st = {
                'Subject Code': value[0],
                'Subject Name': value[1],
                }
            sts.append(st)
    return sts

def getSubjectByCode(code:str):
    result = None       #ban đầu set trạng thái là không tìm thấy
    with open(subjectPath, 'r',encoding= 'utf-8') as f:
        for line in f:
            if line is None:
                break

            value = line.strip().split('|')
            if value[0] == code:    #nếu dòng nào có code == code đầu vào thì lấy giá trị của dòng đó và dừng lại việc tìm kiếm\
                result = {
                    'Subject Code': value[0],
                    'Subject Name': value[1],
                }
                break
    return result

def checkExistsSubject(code:str):
    result = False
    with open(subjectPath,'r',encoding='utf-8') as f:
        for line in f:
            if line is None:
                break
            value = line.strip().split('|')
            if value[0] == code: #nếu dòng nào có code == code đầu vào thì lấy giá trị của dòng đó và dừng lại việc tìm kiếm
                result = True
                break
    return result

#def getScoreByCode(stCode: str, subCode: str):
#SCORE
def writeScore(sc:dict):
    '''Ghi object st vao trong file subject.txt
    {
        'Student Code': '123456'
        'Subject Code': '1101'
        'Diem Qua Trinh': '9'
        'Diem Ket Thuc': '8'
    }
    '''
    with open(scorePath,'a',encoding = 'utf-8') as f:
        line: str = f"{sc['Student Code']}|{sc['Subject Code']}|{sc['Diem Qua Trinh']}|{sc['Diem Ket Thuc']}\n"
        f.write(line)

def writeScores(scs: list):
    '''Ghi object sts vao trong file score.txt
    [{
        'Student Code': '123456'
        'Subject Code': '1101'
        'Diem Qua Trinh': '9'
        'Diem Ket Thuc': '8'
    }, ...]
    '''
    with open(scorePath,'w',encoding = 'utf-8') as f:
        for sc in scs:
            line: str = f"{sc['Student Code']}|{sc['Subject Code']|{sc['Diem Qua Trinh']}|{sc['Diem Ket Thuc']}}\n"
            f.write(line)

def readScore():
    ''' Doc list[dict] tu file subject.txt'''
    scs = []
    with open(scorePath,'r',encoding = 'utf-8') as f:
        for line in f:
            if line is None: 
                break

            value = line.strip().split('|')
            sc = {
                'Student Code': value[0],
                'Subject Code': value[1],
                'Diem Qua Trinh': value[2],
                'Diem Ket Thuc': value[3]
                }
            scs.append(sc)
    return scs

def getScoreByCode(studentCode:str, subjectCode:str):
    result = None       
    with open(scorePath, 'r',encoding= 'utf-8') as f:
        for line in f:
            if line is None:
                break

            value = line.strip().split('|')
            if (value[0] == studentCode) and (value[1] == subjectCode):    #nếu dòng nào có code == code đầu vào thì lấy giá trị của dòng đó và dừng lại việc tìm kiếm\
                result = {
                    'Student Code': value[0],
                    'Subject Code': value[1],
                    'Diem Qua Trinh': value[2],
                    'Diem Ket Thuc': value[3]
                }
                break
    return result

def checkExistsScore(studentCode: str, subjectCode: str):
    result = False
    with open(scorePath, 'r', encoding='utf-8') as f:
        for line in f: 
            if line is None: 
                break
            value = line.strip().Split('|')
            if (value[0] == studentCode) and (value[1] == subjectCode): 
                result = True
                break
    return result