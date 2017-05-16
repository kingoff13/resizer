from PIL import Image #import Image library
from os import listdir,path,chdir,getcwd

def ResizeIt(imgname,t):
    img = Image.open(imgname)
    img=img.resize((1280, int(1280/(img.size[0]/img.size[1]))), Image.NEAREST)
    img.save(str(t)+'.JPG')


userdir=''
while userdir!='exit' :
    userdir=input('Now: ' + getcwd() +'; For exit use "exit". Choose dir: > ')
    if path.isdir(userdir) :
        progressbar=0;
        chdir(userdir)
        images = listdir(userdir)
        count = int(100/len(images))
        t=0
        for each in images:
            if (path.splitext(each)[1]=='.jpg' or
                path.splitext(each)[1]=='.JPG' or
                path.splitext(each)[1]=='.jpeg'):
                ResizeIt(each,t)
                print(str(progressbar)+'%')
                progressbar+=count
                t+=1
        print('Complete')
    elif userdir=='':
        print('Need dir')
    else :
        print('Wrong path')



#os.getcwd() # текущая рабочая директория.
#os.listdir(path=".") # список файлов и директорий в папке.
#os.chdir(path) # смена текущей директории.
#os.mkdir(path, mode=0o777, *, dir_fd=None) # создаёт директорию. OSError, если директория существует.
