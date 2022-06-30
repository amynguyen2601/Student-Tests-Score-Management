# màn hình cho module quản lý học viên
from utils import printHeader, printMenu, clearScreen
from business import bswriteStudent, bsCheckExistsStudent, bsgetStudentbyCode, bsreadStudents, bswriteStudents
import re
from datetime import datetime

#màn hình hiển thị menu của module QL học viên
def studentMenuScreen():
    clearScreen()
    printHeader('Student Managing')

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
        addStudentScreen()
        studentMenuScreen()     #Quay lai man hinh QL hoc vien

    elif cmd == '2':
        #chuyển sang màn hình sửa học viên
        editStudentScreen()
        studentMenuScreen()
        pass
    elif cmd == '3':
        #Chuyen sang man hinh xoá học viên
        deleteStudentScreen()
        studentMenuScreen()
        
    elif cmd == '4': 
        searchStudentsScreen()
        studentMenuScreen()
        
    elif cmd == '0':    #Quay lai man hinh truoc do
        pass

#Màn hình nhập thông tin học viên
def addStudentScreen():
    clearScreen()
    print('Add Student')

#Nhap du lieu tu ban phim 
    code        = input('Student Code: ')               #TODO bat loi: khong dc bo trong, 6 ky tu, chi bao gom so, 
    fullName    = input('Full Name: ')                  #TODO khong duoc bo trong
    birthDay    = input('Birth Day (dd/MM/YYYY): ')     #TODO dinh dang dd/MM/YYYY ->%d/%m/%y
    sex         = input('Gender (0-Nu| 1-Nam): ')       #TODO chi la 0/1
    address     = input('Address: ')                
    phone       = input('Phone: ')                      #TODO co the trong nhwng neu da nhap thi chi bao gom so dai 11 ky tu
    email       = input('Email: ')                      #TODO co the trong nhhung neuy da nhap thi theo dinh dang: email (dung regex)

    #Do du lieu nhan duoc tu ban phim vao dictionary
    st = {
        'Code': code,
        'FullName': fullName,
        'Birthday': birthDay,
        'Sex': sex,
        'Address': address,
        'Phone': phone,
        'Email': email
    }
    bswriteStudent(st)
    print(f'Add student with code {code} successfully')

    ans = input('Enter Y to continue: ')
    if ans.lower() == 'y':
        addStudentScreen()
    else:
        studentMenuScreen()

#Chỉnh sửa thông tin học viên
def editStudentScreen():
    clearScreen()
    printHeader('Edit Student Information')

    while True:
        code = input('Student Code: ')
        if len(code) !=6:
            print('Have to be 6 digits.')
            continue
            
        isExists = bsCheckExistsStudent(code)
        #neu code khong ton tai
        if isExists == False:
            print(f'Student with code {code} does not exist' )
            continue
        break

    #Lay thong tin hhoc vien theo code 
    st = bsgetStudentbyCode(code)

    fullName=st['FullName']
    print('Full Name: ', fullName)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        while True:
            fullName = input('New Full Name: ')
            if fullName=='':
                print('Cannot leave blank')
                continue 
            break

    birthDay=st['Birthday']
    print('Birthday: ', birthDay)
    ans = input('Enter Y/t to edit: ')
    if ans.lower() == 'y':
        birthDay = input('New Birthday: ')

    sex=st['Sex']
    print('Gender: ', sex)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        sex = input('New Gender (0-nam/1-nu): ')
  
    address = st['Address']
    print('Address: ', address)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        address = input('New Address (0-nam/1-nu): ')

    phone=st['Phone']
    print('Phone: ', phone)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        phone = input('New phone number: ')    
    #email
    email=st['Email']
    print('Email: ', email)
    ans = input('Enter Y/y to edit: ')
    if ans.lower() == 'y':
        email = input('New Email: ')  

    #Sua thong tin
    sts= bsreadStudents()                       #lay ra tat ca hoc vien sau do tiem toi hoc vien can sua va update lai thong tin
    for st in sts:
        if st['Code'] == code:
            st['FullName'] = fullName
            st['Birthday']=birthDay
            st['Sex'] = sex
            st['Address'] = address
            st['Phone']= phone
            st['Email']=email
            break   

    #sts la list chua hoc vien da dc chinh sua thong tin
    #ghi list sts vao trong student.txt
    bswriteStudents(sts)
    print('Edit Successfully')

    ans = input('Enter Y to edit another student: ')
    if ans.lower() == 'y':
        editStudentScreen()
    
# Xoá học viên theo mã
def deleteStudentScreen():
    clearScreen()
    printHeader('Delete Student')

    while True:
        code = input('Student Code: ')
        if len(code) !=6:
            print('Have to be 6 digits.')
            continue
            
        isExists = bsCheckExistsStudent(code)
        #neu code khong ton tai
        if isExists == False:
            print(f'Student with code {code} does not exist' )
            continue
        break
    #xoa thong tin
    #lay ra tat ca hoc viên sau do tim toi hoc vien can xoa và xoa thong tin
    sts = bsreadStudents()
    idx = None
    for i, st in enumerate(sts):
        if st['Code'] == code:
            idx = i 
            break

    #idx laf chi so cua phan tu can xoa
    sts.pop(idx)

    #sts la list da dc xoa
    #ghi list sts vao trong studen.txt
    bswriteStudents(sts)
    print('Deleted Successfullt')

    ans = input('Enter Y to delete another student: ')
    if ans.lower() == 'y':
        deleteStudentScreen()
    else:
        studentMenuScreen()

#Tìm kiếm học viên
def searchStudentsScreen():
    sts=bsreadStudents()
    printStudents(sts)

    content = input('Search')
    if content != '':
        stsFiltered = []
        for st in sts:
            #dieu kien tim kiem
            #Code tim kiem tuyet doi
            #fullName tim kiem gan dung
            if st['Code'] == content\
                or content.lower() in st['FullName'].lower()\
                    or content.lower() in st['Address'].lower():
                stsFiltered.append(st)
        #da cos list hoc vien da dc loc ra
        printStudents(stsFiltered)

    ans = input('Enter Y to input another student: ')
    if ans.lower() == 'y':
        searchStudentsScreen()
    else:
        studentMenuScreen()


def printStudents(sts: list):
    clearScreen()
    printHeader('Student List')

    print("Student Code/\tFull Name\tBirth Day\tGender\t\tAddress\tPhone\tEmail")
    for st in sts:
        sexAlias = 'Nam' if st['Sex'] == '1' else 'Nu'if st['Sex'] == '0' else '-'
        print(f"{st['Code']}\t{st['FullName']}\t{st['Birthday']}\t{sexAlias}\t\t{st['Address']}\t\t{st['Phone']}\t{st['Email']}")