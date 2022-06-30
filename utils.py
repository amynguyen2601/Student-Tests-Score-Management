#hộp công cụ
import os 

#in tieu de man hinh 
def printHeader(title: str):
    header = f'***** {title} *****'
    print(header)
    print('-' * len(header))

def printMenu(funcs:list):
    print('\n'.join(funcs))

#Xoa sach noi dung tren terminal / command prompt 
def clearScreen():
    os.system('clear||cls')