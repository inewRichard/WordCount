#this is the test!
import sys
import os

#递归得到所有符合条件的文件
def file_name(file_dir):
    filename=[]
    for root, dirs, files in os.walk(file_dir):
        #print(root) #当前目录路径
        #print(dirs) #当前路径下所有子目录
        #print(files)
        filename.append(files)
    return filename


#获取停用词
def getword(filename):
    f=open(filename,'r')
    count=f.read()
    count=list(count)
    word=''
    wordlist=[]
    for i in count:
        if(i==' '):
            wordlist.append(word)
            word=''
        else:
            word=word+str(i)
    wordlist.append(word)
    
    return wordlist




    
    
#字符数
def f_c(filename):
    f=open(filename,'r')
    count=f.read()
    count=list(count)
    num=len(count)
    return num

#单词总数
def f_w(filename,signlist):
    f=open(filename,'r')
    count=f.read()
    count=list(count)
    word=''
    wordlist=[]
    for i in count:
        if(i==' '):
            if word in signlist:
                word=''
            else:
                wordlist.append(word)
                word=''
        elif(i==','):
            if word in signlist:
                word=''
            else:
                wordlist.append(word)
                word='' 
        else:
            word=word+str(i)
    wordlist.append(word)
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
def f_o(outputFile,command,signlist):
    f=open(outputFile,'w')
    f.write(' ')
    f.close()
    f=open(outputFile,'a')
    if '-c' in command:
        char=f_c(command[-3])
        f.write("字符数:"+str(char)+'\n')
    if '-w' in command:
        word=f_w(command[-3],signlist)
        f.write("单词数:"+str(word)+'\n')
    if '-l' in command:
        row=f_l(command[-3])
        f.write("行数"+str(row)+'\n')
    f.close()
                
        
    
    

fileway=os.getcwd()
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


        
#command=['wc.exe','-c','-w','test1.txt','-o','output.txt']#测试参数示例





if '-s' in command:
    if '-o' in command:
        if '-e' in command:
            filekind=command[-5]
            filename=file_name(fileway)
            filetail='.'
            info=0
            for i in filekind:
                if(i=='.'):
                    info=1
                if(info==1):
                    filetail=filetail+str(i)
            for f in filename:
                if filetail in f:
                    signlist=getword(command[-3])
                    f_o(command[-1],command,signlist)
        else:
            filekind=command[-3]
            filename=file_name(fileway)
            filetail='.'
            info=0
            for i in filekind:
                if(i=='.'):
                    info=1
                if(info==1):
                    filetail=filetail+str(i)
            for f in filename:
                if filetail in f:
                    signlist=[]
                    f_o(command[-1],command,signlist)
    else:
        if '-e' in command:
            filekind=command[-3]
            filename=file_name(fileway)
            filetail='.'
            info=0
            for i in filekind:
                if(i=='.'):
                    info=1
                if(info==1):
                    filetail=filetail+str(i)
            for f in filename:
                if filetail in f:
                    signlist=getword(command[-1])
                    f=open("result.txt",'w')
                    f.write(' ')
                    f.close()
                    f=open("result.txt",'a')
                    if '-c' in command:
                        char=f_c(command[-1])
                        f.write("字符数:"+str(char)+'\n')
                        print("字符数:"+str(char))
                    if '-w' in command:
                        word=f_w(command[-1],signlist)
                        f.write("单词数"+str(word)+'\n')
                        print("单词数:"+str(word))
                    if '-l' in command:
                        row=f_l(command[-1])
                        f.write("行数"+str(row)+'\n')
                        print("行数:"+str(row))
                    f.close()
        else:
            filekind=command[-1]
            filename=file_name(fileway)
            filetail='.'
            info=0
            for i in filekind:
                if(i=='.'):
                    info=1
                if(info==1):
                    filetail=filetail+str(i)
            for f in filename:
                if filetail in f:
                    signlist=[]
                    f=open("result.txt",'w')
                    f.write(' ')
                    f.close()
                    f=open("result.txt",'a')
                    if '-c' in command:
                        char=f_c(command[-1])
                        f.write("字符数:"+str(char)+'\n')
                        print("字符数:"+str(char))
                    if '-w' in command:
                        word=f_w(command[-1],signlist)
                        f.write("单词数"+str(word)+'\n')
                        print("单词数:"+str(word))
                    if '-l' in command:
                        row=f_l(command[-1])
                        f.write("行数"+str(row)+'\n')
                        print("行数:"+str(row))
                    f.close()
else:#没有'-s'
    if '-o' in command:
        if '-e' in command:
            signlist=getword(command[-3])
            f_o(command[-1],command,signlist)
        else:
            signlist=[]
            f_o(command[-1],command,signlist)
    else:
        if '-e' in command:
            signlist=getword(command[-1])
            f=open("result.txt",'w')
            f.write(' ')
            f.close()
            f=open("result.txt",'a')
            if '-c' in command:
                char=f_c(command[-1])
                f.write("字符数:"+str(char)+'\n')
                print("字符数:"+str(char))
            if '-w' in command:
                word=f_w(command[-1],signlist)
                f.write("单词数"+str(word)+'\n')
                print("单词数:"+str(word))
            if '-l' in command:
                row=f_l(command[-1])
                f.write("行数"+str(row)+'\n')
                print("行数:"+str(row))
            f.close()
        else:
            signlist=[]
            f=open("result.txt",'w')
            f.write(' ')
            f.close()
            f=open("result.txt",'a')
            if '-c' in command:
                char=f_c(command[-1])
                f.write("字符数:"+str(char)+'\n')
                print("字符数:"+str(char))
            if '-w' in command:
                word=f_w(command[-1],signlist)
                f.write("单词数"+str(word)+'\n')
                print("单词数:"+str(word))
            if '-l' in command:
                row=f_l(command[-1])
                f.write("行数"+str(row)+'\n')
                print("行数:"+str(row))
            f.close()
    
        
            
                    

    

