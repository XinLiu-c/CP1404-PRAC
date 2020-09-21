import os
import shutil

def main():
    os.getcwd()
    os.chdir('FilesToSort')
    os.getcwd()

    dir_xlsx=[]
    dir_xls=[]
    dir_txt=[]
    dir_png=[]
    dir_jpg=[]
    dir_gif=[]
    dir_docx=[]
    dir_doc=[]
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            src = filename.split('.')
            print(src)

            if src[1]=='xlsx':
                dir_xlsx.append(src)
            if src[1]=='xls':
                dir_xls.append(src)
            if src[1]=='txt':
                dir_txt.append(src)
            if src[1]=='png':
                dir_png.append(src)
            if src[1]=='jpg':
                dir_jpg.append(src)
            if src[1]=='gif':
                dir_gif.append(src)
            if src[1]=='docx':
                dir_docx.append(src)
            if src[1]=='doc':
                dir_doc.append(src)
        else:
            pass
    print(dir_xlsx)


    os.mkdir('xlsx')
    os.mkdir('xls')
    os.mkdir('txt')
    os.mkdir('png')
    os.mkdir('jpg')
    os.mkdir('gif')
    os.mkdir('docx')
    os.mkdir('doc')
    move('xlsx',dir_xlsx)
    move('xls', dir_xls)
    move('txt', dir_txt)
    move('png', dir_png)
    move('jpg', dir_jpg)
    move('gif', dir_gif)
    move('docx', dir_docx)
    move('doc', dir_doc)

def move(type,x):
    Dir = ''
    for i in x:
        Dir = i[0] + '.' + i[1]
        a = os.path.join(os.getcwd(), Dir)
        b = os.path.join(os.getcwd(), type)
        shutil.move(a, b)

main()
