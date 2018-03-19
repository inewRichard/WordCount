#this is the test!

#字符数
def f_c(filename):
    f=open(filename,'r')
    count=f.read()
    count=list(count)
    num=len(count)
    return num

#单词总数
def f_w():
    f=open(filename,'r')
    count=f.read()
    count=list(count)
    word=''
    wordlist=[]
    for i in count:
        if(i==' '):
            wordlist.append(word)
            word=''
        elif(i==','):
            wordlist.append(word)
            word=''
        else:
            word=word+str(i)
    num=len(wordlist)
    return num


#总行数
def f_l(filename):
    f=open(filename,'r')
    num=0
    s=f.readline()
    while(s!=''):
        num=num+1
        s=f.readline()
    return num

#将结果输出到指定文件
def f_o(outputFile,command):
    f=open(outputFile,'w')
    f.write(' ')
    f.close()
    f=open(outputFile,'a')
    if '-c' in command:
        char=f_c(command[-3])
        f.write("字符数:"+char)
    if '-w' in command:
        word=f_w(command[-3])
        f.write("单词数:"+word)
    if '-l' in command:
        row=f_l(command[-3])
        f.write("行数"+row)
    f.close()
                
        
    
    

import sys
commandlist=str(sys.argv)


#commandlist=list(commandlist)
commandword=''
command=[]
for i in commandlist:
    if(i==' '):
        command.append(commandword)
        commandword=''
    else:
        commandword=commandword+str(i)

if(command[-2]=='-o'):
    f_o(command[-1],command)
else:
    if '-c' in command:
        char=f_c(command[-1])
        print("字符数:"+char)
    if '-w' in command:
        word=f_w(command[-1])
        print("单词数:"+word)
    if '-l' in command:
        row=f_l(command[-1])
        print("行数:"+row)
    
    

