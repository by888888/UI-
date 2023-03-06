p = [[], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'],
     ['分析完成'], ['分析完成'], [], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成'], ['分析完成']]


def func(x):
     ret = []
     for b in x:
          if isinstance(b, list):
               for a in func(b):
                    ret.append(a)
          else:
               ret.append(b)
     return ret


ret = func(list1)
print(ret)


#递归实现剥离列表的嵌套
def striplist(l):
    res=[]
    for i in l:
        if not isinstance(i,list):
            res+=[i]
        else:
            res+=striplist(i)
    return res
