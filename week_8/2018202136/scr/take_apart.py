#encoding=utf-8
import jieba
import jieba.posseg as pseg
filename = "text.txt"
database = "data.txt"
f = open(filename,"r")
fn = open(database,"w+")    
line = f.read()
words = pseg.cut(line)
for word in words:
    print >>fn,str(word)
f.close()
fn.close()