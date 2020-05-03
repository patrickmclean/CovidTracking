from FileManager import *
import datetime
import time

# Program to
# List files in a directory
# Choose one of the files meeting a timestamp
# Copy that file to a new directory

# Constants
path = '/Users/patrickmclean/Pictures/MaynardCamPics/Originals/Spring/'
subpath = 'Seq/'
step=4


filelist = Dirlist(path)
i=0
j=0
while(i<len(filelist)):
    # print(filelist[i]+'\n')
    i+=step
    j+=1
    Copy((path+filelist[i]),(path+subpath+'img'+'{:0>4}'.format(j))+'.jpg')
