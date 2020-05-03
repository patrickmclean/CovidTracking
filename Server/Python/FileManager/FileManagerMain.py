import FileManager

run=1
while(run==1):     #Running the program again
    os.system('cls')        #Used to clear the screen after running again the program
    print('LiteKnight File Manager')
    dec=int(input('''1.Read a file
2.Write in a File
3.Append text in a File
4.Delete a file
5.List Files in a directory
6.Check file existence
7.Move a file
8.Copy a file
9.Create a Directory
10.Delete A Directory
11.Open a program
12.Exit
Choose the option number:
'''))
    if dec==1:
        Read()
    if dec==2:
        Write()
    if dec==3:
        Add()
    if dec==4:
        Delete()
    if dec==5:
        Dirlist()
    if dec==6:
        Check()
    if dec==7:
        Move()
    if dec==8:
        Copy()
    if dec==9:
        Makedir()
    if dec==10:
        Removedir()
    if dec==11:
        Openfile()
    if dec==12:
        exit()
    run=int(input("1.Run again \n2.Exit \nChoose the option number: \n"))
    if run==2:
        exit()
