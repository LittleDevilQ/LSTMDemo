#coding=utf-8
import csv
import random
# 地址转delta，取delta至少出现10次的值，对PC和delta相同的值进行降重
def file_delta():
    newfile = open(r'D:\VSCode\CodeWorkplace\.vscode\pc-add.txt', 'r')
    f_delta = open(r'D:\VSCode\CodeWorkplace\.vscode\pc-delta.txt', 'a')
    lines = newfile.readlines()
    str0 = lines[0].split(' ')
    add0 = int(str0[1], 16)
    for i in range(1, len(lines)):
        str_object = lines[i].split(' ')
        addi = int(str_object[1], 16)
        delta = addi - add0
        new_object = str_object[0] + ' ' + str(delta) + '\n'
        f_delta.write(new_object)
        add0 = addi
    newfile.close()
    f_delta.close()


def data_process():
    dic = {}
    l = []
    f_delta = open(r'D:\VSCode\CodeWorkplace\.vscode\pc-delta.txt', 'r')
    lines = f_delta.readlines()
    for line in lines:
        data = line.split(' ')
        dic.setdefault(data[1].rstrip(), []).append(data[0])
    for i in dic:
        if len(dic[i]) >= 10:
            l.append(i)
    f1 = open(r'D:\VSCode\CodeWorkplace\.vscode\PC_dataset.txt', 'a')
    for line in lines:
        data = line.split(' ')
        if data[1].rstrip() in l:
            f1.writelines(line)
    f_delta.close()
    f1.close()

def txtToCsv():
    with open(r'D:\VSCode\CodeWorkplace\.vscode\PC_dataset.csv', 'a',newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        # 读要转换的txt文件，文件每行各词间以@@@字符分隔
        with open(r'D:\VSCode\CodeWorkplace\.vscode\PC_dataset.txt', 'r',encoding='utf-8') as filein:
            for line in filein:
                data = line.strip('\n').split(' ')
                s = int(data[0],16)
                line_list = []
                line_list.append(str(s))
                line_list.append(data[1])
                spamwriter.writerow(line_list)

def combineFile():
    f = open(r'D:\VSCode\CodeWorkplace\.vscode\poi.txt', 'a',encoding="utf-8")
    f1 = open(r'D:\VSCode\CodeWorkplace\.vscode\娱乐.txt', 'r',encoding="utf-8")
    lines = f1.readlines()
    for line in lines:
        line = "娱乐,"+line
        f.write(line)
    f1.close()
    f.close()

def normalization():
    f = open(r'D:\VSCode\CodeWorkplace\.vscode\poi.txt', 'r',encoding="utf-8")
    f1 = open(r'D:\VSCode\CodeWorkplace\.vscode\normal.txt', 'a',encoding="utf-8")
    lines = f.readlines();
    for line in lines:
        data = line.strip('\n').split(',')
        line1 = data[0]
        s = ""
        if len(data) == 5:
            f1.write(line)
        elif len(data) > 5:
            pos = 0
            for i in range(1, len(data)):
                if isDouble(data[i]):
                    break
                s += data[i]
                pos = pos + 1
            line1 += "," + s
            for j in range(pos+1, len(data)):
                line1 += "," +data[j]
            f1.write(line1)     
    f.close()
    f1.close()
            
    
def isDouble(s):
    try:
        float(s) # is a number(either integer or real)
        return not s.isnumeric()
    except:
        return False

def randomCenter():
    f = open(r'D:\VSCode\CodeWorkplace\.vscode\normal.txt', 'r',encoding="utf-8")
    f1 = open(r'D:\VSCode\CodeWorkplace\.vscode\center.txt', 'a',encoding="utf-8")
    lines = f.readlines();
    h = set()
    while(len(h) < 100):
        h.add(random.randint(0, len(lines)))
    for i in h:
        data = lines[i].strip('\n').split(',')
        line =  data[2] + ',' +data[3] +'\n'
        f1.write(line)
    f.close()
    f1.close()


if __name__ == "__main__":
    #combineFile()
    #normalization()
    randomCenter()
