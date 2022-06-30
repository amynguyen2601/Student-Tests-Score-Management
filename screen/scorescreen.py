# màn hình cho module quản lý diem thi
from business.studentbusiness import bsCheckExistsStudent
from business.subjectbusiness import bsCheckExistsSubject
from utils import printHeader, printMenu, clearScreen
from business import bsWriteScore, bsWriteScores, bsCheckExistsScore, bsGetScoreByCode, bsReadScores, bsreadStudents, bsgetStudentbyCode

#màn hình hiển thị menu của module QL diem thi
def scoreMenuScreen():
    clearScreen()
    printHeader('Score Managing')

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
        addScoreScreen()
        scoreMenuScreen()     #Quay lai man hinh QL hoc vien

    elif cmd == '2':
        #chuyển sang màn hình sửa học viên
        editScoreScreen()
        scoreMenuScreen()
        pass
    elif cmd == '3':
        #Chuyen sang man hinh xoá học viên
        deleteScoreScreen()
        scoreMenuScreen()
        
    elif cmd == '4': 
        searchScoresScreen()
        scoreMenuScreen()
        
    elif cmd == '0':    #Quay lai man hinh truoc do
        pass

#Màn hình nhập diem thi
def addScoreScreen():
    clearScreen()
    print('Enter Score')

    # studentCode = input('Student Code: ')

    while True:
        studentCode = input('Student Code: ')   
        if len(studentCode) != 6:
            print('Have to be 6 digits.')
            continue

        isExists = bsCheckExistsStudent(studentCode)
        #Neu Code khong ton tai
        if isExists == False:
            print(f'Student does not exist')
            continue
        break

    subjectCode = input('Subject Code: ') 
    diemQuaTrinh = input('Diem Qua Trinh: ')
    diemKetThuc = input('Diem Ket Thuc: ')
    sc = {
        'StudentCode' : studentCode,
        'SubjectCode' : subjectCode,
        'DiemQuaTrinh': diemQuaTrinh,
        'DiemKetThuc': diemKetThuc
    }
    bsWriteScore(st)
    print(f'Enter Score Successfully')

    ans = input('Enter Y to continue: ')
    if ans.lower() == 'y':
        addScoreScreen()
    else:
        scoreMenuScreen()

#Chỉnh sửa diem thi
def editScoreScreen():
    clearScreen()
    printHeader('Edit Score')

    while True:
        studentCode = input('Student Code: ')
        if len(studentCode) !=6:
            print('Have to be 6 digits.')
            continue
            
        isExists = bsCheckExistsStudent(studentCode)
        #neu code khong ton tai
        if isExists == False:
            print(f'Student does not exist' )
            continue
        break

    #Lay thong tin hhoc vien theo subjcode #TODO
    while True:
        subjectCode = input('Subject Code: ')
        if len(subjectCode) != 4:
            print('Havr to be 4 digits.')
            continue
        isExists = bsCheckExistsSubject(subjectCode)
        if isExists == False:
            print(f'Subject does not exist')
            continue
        break

    sc = bsGetScoreByCode(studentCode, subjectCode)

    # subjectCode = st['SubjectCode']
    # print('Subject Code', subjectCode)
    # ans = input('Enter Y/y to edit: ')
    # if ans.lower() == 'y':
    #     while True:
    #         subjectCode = input('New Full Name: ')
    #         if subjectCode=='':
    #             print('Cannot leave blank')
    #             continue 
    #         break

    diemQuaTrinh = sc['Diem Qua Trinh']
    print('Diem Qua Trinh', diemQuaTrinh)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        while True:
            diemQuaTrinh = input('Diem Qua Trinh Moi: ')
            if diemQuaTrinh=='':
                print('Cannot leave blank')
                continue 
            break

    diemKetThuc = sc['Diem Ket Thuc']
    print('Diem Ket Thuc', diemKetThuc)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        while True:
            diemKetThuc = input('Diem Ket Thuc Moi: ')
            if diemKetThuc=='':
                print('Cannot leave blank')
                continue 
            break

    #Sua thong tin
    scs= bsReadScores()                       
    for sc in scs:
        if sc['Student Code'] == studentCode:
            sc['Subject Code'] == subjectCode
            sc['Diem Qua Trinh'] == diemQuaTrinh
            sc['Diem Ket Thuc'] == diemKetThuc
            break   

    #sts la list da dc chinh sua thong tin
    #ghi list sts vao trong score.txt
    bsWriteScores(scs)
    print('Edited Successfully')

    ans = input('Enter Y to edit another student\'s score: ')
    if ans.lower() == 'y':
        editScoreScreen()
    
# Xoá diem thi theo mã
def deleteScoreScreen():
    clearScreen()
    printHeader('Delete Score')

    while True:
        studentCode = input('Student Code: ')
        if len(studentCode) !=6:
            print('Have to be 6 digits.')
            continue
            
        isExists = bsCheckExistsScore(studentCode)
        #neu code khong ton tai
        if isExists == False:
            print(f'Student does not exist' )
            continue
        break
    #xoa thong tin
    #lay ra tat ca hoc viên sau do tim toi hoc vien can xoa và xoa thong tin
    scs = bsReadScores()
    idx = None
    for i, sc in enumerate(sts):
        if sc['Student Code'] == studentCode:
            idx = i 
            break

    #idx laf chi so cua phan tu can xoa
    scs.pop(idx)

    #sts la list da dc xoa
    #ghi list sts vao trong studen.txt
    bsWriteScores(scs)
    print('Deleted Successfullt')

    ans = input('Enter Y to delete another student: ')
    if ans.lower() == 'y':
        deleteScoreScreen()
    else:
        scoreMenuScreen()


#Tìm kiếm diem thi
def searchScoresScreen():
    scs=bsReadScores()
    printScores(scs)

    content = input('Search')
    if content != '':
        stsFiltered = []
        for sc in scs:
            #dieu kien tim kiem
            #Code tim kiem tuyet doi
           
            if sc['Student Code'] == content\
                    or content.lower() in sc['Subject Code'].lower()\
                    or content.lower() in sc['Diem Qua Trinh'].lower()\
                    or content.lower() in sc['Diem Ket Thuc'].lower:
                scsFiltered.append(sc)
        #da cos list hoc vien da dc loc ra
        printScores(scsFiltered)

    ans = input('Enter Y to input another student: ')
    if ans.lower() == 'y':
        searchScoresScreen()
    else:
        scoreMenuScreen()


def printScores(scs: list):
    clearScreen()
    printHeader('Search Score ')

    print("Student Code\tSubject Code\tDiem Qua Trin\tDiem Ket Thuc\tDiem Tong Ket")
    for sc in scs:
        diemTongKet = ((int(st['Diem Qua Trinh'])+int(st['Diem Ket Thuc']*2)/3))
        letterGrade =    'A' if diemTongKet >= 90 and diemTongKet <=100 else 'B' if diemTongKet >=70 and diemTongKet <90 else 'C' if diemTongKet >=50 and diemTongKet < 70 else 'D' if diemTongKet < 50 else '_'
        # lay ra Student by student code
        # s = bsgetStudentbyCode(sc['Student Code'])

        print(f"{sc['Student Code']}\t{sc['Subject Code']}\t{sc['Diem Qua Trinh']}\t{sc['Diem Ket Thuc']}\t\t{letterGrade}")