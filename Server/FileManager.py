import shutil         #Contains functions for operating files
import os         #imports the os

def Read(filename):        #For reading files
    file=open(filename)
    content = file.read()
    file.close() 
    return content


def Write():    #For writing or creating files
    path=input("Enter the location of file to write or create:")
    if os.path.isfile(path):
        print('Rebuilding Existing file') #For existing file
    else:
        print('Creating new file') #For new file
    text=input("Enter the text to write:")
    file=open(path,"w")
    file.write(text)

def Add():      # Adding text to a file
    path=input("Enter the file location:")
    text=input("Enter the text to write:")
    file=open(path,"a")
    file.write('\n'+text)


def Delete():          #Deleting a File
    path=input("Enter the location of file to be write or create:")
    if os.path.exists(path):      # checks if the file exists
        print('File Found')     #For existing file
        os.remove(path)          #os.remove(file path) is used to delete
        print('File has been deleted')
    else:
        print('File Does\'nt exist')    #Is no file exist



def Dirlist(path):      #Listing files in a directory
    sortlist=sorted(os.listdir(os.path.expanduser(path)))       #Sorting and listing files
    return sortlist
#    i=0
#    while(i<len(sortlist)):
#        print(sortlist[i]+'\n')
#        i+=1


def Check():       #Checking file or directory presence
    fp=int(input('Check the presence of \n1.File \n2.Directry \n'))
    if fp==1:
        path=input("Enter the file location:")
        os.path.isfile(path)
        if os.path.isfile(path)==True:
            print('File Found')
        else:
            print('File not Found')
    if fp==2:
        path=input("Enter the Directory location:")
        os.path.isdir(path)
        if os.path.isdir(path)==False:
            print('Directory Found')
        else:
            print('Directory Not Found')



def Move():        #For moving or renameing file
    path1=input('Enter the location of File to move or rename:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the resulting location with resulting file name:')
        shutil.move(path1,path2)
        print('File renamed')
    if mr==2:
        path2=input('Enter the location to move:')
        shutil.move(path1,path2)
        print('File moved')


def Copy(path1,path2):       #For copying
    shutil.copy(path1,path2)
    #print('File copied %s %s \n',path1,path2)


def Makedir():            #For creating directory
    path=input("Enter the directory name with location to make \neg. C:\\Hello\\Newdir \nWhere newdir is new directory:")
    os.makedirs(path) 
    print('Directory Created')


def Removedir():             #For removing Directory
    path=input('Enter the location of Directory:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()


def Openfile():
    path=input('Enter the location of Program:')
    try:
        os.startfile(path)
    except:
        print('File not found')




 
 


