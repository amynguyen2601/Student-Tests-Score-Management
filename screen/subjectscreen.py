# Màn hình quan ly mon hoc
from utils import printHeader, printMenu, clearScreen
from business import bswriteSubject, bswriteSubjects, bsgetSubjectByCode, bsCheckExistsSubject, bsreadSubject

#màn hình hiển thị menu của module QL học viên
def subjectMenuScreen():
    clearScreen()
    printHeader('Subject Managing')

    funcs = [
        '1. Add',
        '2. Edit',
        '3. Delete',
        '4. List',
        '0. Back'
    ]
    printMenu(funcs)     #phan cach cac du lieu trong list bang \n

    cmd = None
    while cmd not in ['1','2','3','4','0']:
        cmd = input('Choose function: ')

    if cmd == '1':
        addSubjectScreen()
        subjectMenuScreen()     #Quay lai man hinh QL mon hoc

    elif cmd == '2':
        #chuyển sang màn hình sửa mon hoc
        editSubjectScreen()
        subjectMenuScreen()
        
    elif cmd == '3':
        #Chuyen sang man hinh xoá Mon Hoc
        deleteSubjectScreen()
        subjectMenuScreen()
    elif cmd == '4':
        #chuyển sang màn hình danh sách Mon Hoc
        searchSubjectsScreen()
        subjectMenuScreen()
    elif cmd == '0':    #Back to previous screen
        pass

#Màn hình nhập thông tin mon hoc
def addSubjectScreen():
    clearScreen()
    printHeader('Add Subject')

#Nhap du lieu tu ban phim 
    subjectCode = input ('Subject Code ')
    subjectName = input ('Subject Name ')
    
    #Do du lieu nhan duoc tu ban phim vao dictionary
    st = {
        'Subject Code': subjectCode,
        'Subject Name': subjectName
    }
    bswriteSubject(st)
    print(f'Add subject with code {subjectCode} successfully')

    ans = input('Enter Y to continue: ')
    if ans.lower() == 'y':
        addSubjectScreen()
    else:
        subjectMenuScreen()

#Chỉnh sửa thông tin mon hoc
def editSubjectScreen():
    clearScreen()
    printHeader('Edit Subject')

    while True:
        code = input('Subject Code: ')
        if len(code) !=4:
            print('Have to be 4 digits.')
            continue
        
        isExists = bsCheckExistsSubject(code)
        #neu code khong ton tai
        if isExists == False:
            print(f'Subject with code {code} does not exist' )
            continue
        break

    #Lay thong tin mon hoc theo cod
    st = bsgetSubjectByCode(code)

    subjectName = st['Subject Name']
    print('Subject Name: ', subjectName)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        while True:
            subjectName = input('New subject name: ')
            if subjectName == '':
                print('Cannot be blank')
                continue
            break

    sts=bsreadSubject()
    for st in sts:
        if st['Subject Code'] == code:
            st['Subject Name'] == subjectName
    
    bswriteSubjects(sts)
    print('Edit successfully')

    ans = input('Enter Y to process another subject: ')
    if ans.lower() == 'y':
        editSubjectScreen()

# Xoá mon hoc theo mã
def deleteSubjectScreen():
    clearScreen()
    printHeader('Delete Subject')

    while True:
        code = input('Subject Code: ')
        if len(code) !=4:
            print('Have to be 4 digits.')
            continue
            
        isExists = bsCheckExistsSubject(code)
        #neu code khong ton tai
        if isExists == False:
            print(f'Subject with code {code} does not exist' )
            continue
        break
    #xoa thong tin
    #lay ra tat ca hoc viên sau do tim toi hoc vien can xoa và xoa thong tin
    sts = bsreadSubject()
    idx = None
    for i, st in enumerate(sts):
        if st['Code'] == code:
            idx = i 
            break

    #idx laf chi so cua phan tu can xoa
    sts.pop(idx)

    #sts la list da dc xoa
    #ghi list sts vao trong studen.txt
    bswriteSubjects(sts)
    print('Deleted Successfully')

    ans = input('Enter Y to insert another subject: ')
    if ans.lower() == 'y':
        deleteSubjectScreen()
    else:
        subjectMenuScreen()

#Tìm kiếm mon hoc
def searchSubjectsScreen():
    sts = bsreadSubject()
    printSubjects(sts)

    content = input('Search: ')
    if content != '':
        stsFiltered = []
        for st in sts:
            #dieu kien tim kiem
            #Code tim kiem tuyet doi
            #fullName tim kiem gan dung
            if st['Subject Code'] == content\
                or content.lower() in st['Subject Name'].lower():
                stsFiltered.append(st)
        #da cos list hoc vien da dc loc ra
        printSubjects(stsFiltered)

    ans = input('Enter Y to input another student: ')
    if ans.lower() == 'y':
        searchSubjectsScreen()
    else:
        subjectMenuScreen()

def printSubjects(sts: list):
    clearScreen()
    printHeader('Subject List')

    print("Subject Code/\tSubject Name")
    for st in sts:
        # sexAlias = 'Nam' if st['Sex'] == '1' else 'Nu'if st['Sex'] == '0' else '-'
        print(f"{st['Subject Code']}\t{st['Subject Name']}")



