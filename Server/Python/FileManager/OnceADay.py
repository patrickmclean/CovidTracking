from FileManager import *
import datetime
import time

# Program to
# List files in a directory
# Choose one of the files meeting a timestamp
# Copy that file to a new directory

# Constants
inpath = '/Users/patrickmclean/Pictures/MaynardCamPics/Source/'
outpath = '/Users/patrickmclean/Pictures/MaynardCamPics/Sequence/'
start_date = datetime.date(2017,1,1)
end_date = datetime.date(2017,8,5)
timebox = '_11.5'
k=0

filelist = Dirlist(inpath)
#i=0
#while(i<len(filelist)):
#    print(filelist[i]+'\n')
#    i+=1

# cycle through each day from start to end
delta = (end_date - start_date).days
for i in range(delta):
    i_date = (start_date + datetime.timedelta(i))
    i_date_string = i_date.strftime("%Y-%m-%d")
    valid_time = i_date_string + timebox   # the specific hour/minute
    #print(valid_time)
    # Programmers will kill me for the inefficiency in the next section
    j=0
    while(j<len(filelist)):
        #print(filelist[j])
        if valid_time in filelist[j]:
            print (filelist[j]+' '+str(j)+' '+str(k))
            Copy((inpath+filelist[j]),(outpath+'img'+format(k,'04d')+'.jpg'))
            k+=1
        j+=1
