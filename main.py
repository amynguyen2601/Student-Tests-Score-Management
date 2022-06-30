# Main module cua ung dung
from screen import subjectMenuScreen
from screen.scorescreen import scoreMenuScreen
from utils import printHeader, printMenu, clearScreen
from screen import studentMenuScreen

# Màn hình menu chính của ứng dụng
def mainMenuScreen():
    clearScreen()
    printHeader('SCORE MANAGEMENT PROGRAM')

    funcs = [
        '1. Student Managing',
        '2. Subject Managing',
        '3. Score Managing',
        '0.Exit'
    ]
    printMenu(funcs)     #phan cach cac du lieu trong list bang \n

    cmd = None
    while cmd not in ['1','2','3','0']:
        cmd = input('Choose function: ')

    if cmd == '1':
        #Chuyển sang màn hình QL học viên
        studentMenuScreen() 
        # Mở lại màn hình menu chính
        mainMenuScreen()
    elif cmd == '2':
        #chuyen sang man hinh QL mon hoc
        subjectMenuScreen()
        mainMenuScreen()
        
    elif cmd == '3':
        scoreMenuScreen()
        mainMenuScreen()
        
    elif cmd == '0':
        #Thoat ung dung
        print('End')
        exit()

if __name__ == '__main__':
    mainMenuScreen()