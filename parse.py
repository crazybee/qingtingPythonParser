import sys
import json
import codecs 
import os
from pathlib import Path
import shutil



datafile = 'D://QTDownloadRadio/download.dat'
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

with codecs.open(datafile, 'r', 'utf-8-sig') as data_file:
    input=data_file.read().replace(' ', '').replace('\n', '')
inputobjects=input.split('{')[1:]

for dataitem in inputobjects:
    filename=find_between(dataitem,'uniqueId":',',')
    newfilename1=find_between(dataitem,'"channelName":"','",').replace(',','').replace('.','-').replace('/','').replace(':','').replace('：','').replace(' ','').replace('，','')
    newfilename2=find_between(dataitem,'"programName":"','",').replace(',','').replace('.','-').replace('/','').replace(':','').replace('：','').replace(' ','').replace('，','')
    newname=newfilename1+newfilename2
    newname= (newname[:15]) if len(newname) > 15 else newname
    print(filename)
    tempfilename='D://QTDownloadRadio/'+filename
    outputfolder='D://QTDownloadRadio/output/'
    if(not os.path.isdir(outputfolder)):
        os.makedirs(outputfolder)
    newfilename=('D://QTDownloadRadio/output/'+newname+'.m4a')
    if (os.path.isfile(tempfilename) and (not os.path.isfile(newfilename))): 
         shutil.copy(tempfilename, newfilename)
     
     

