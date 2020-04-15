import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}    # 姓名字典,{ 人物名称 ：该人物在全文中出现的次数 }
relationships = {}    # 关系字典,{有向边的起点 : edge { 有向边的终点 : 有向边的权值 }},代表两个人物之间联系的紧密程度
lineNames = []    # 每段内人物关系,缓存变量，保存对每一段分词得到当前段中出现的人物名称
                  # lineName[i]是一个列表，列表中存储第i段中出现过的人物。

# 做分词（判断该词的词性是不是“人名”[词性编码：nr]，如果该词的词性不为nr，则认为该词不是人名)
jieba.load_userdict("dict.txt")    # 加载字典
with codecs.open("busan.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)    # 分词并返回该词词性
        lineNames.append([])    # 为新读入的一段添加人物名称列表
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue     # 当分词长度小于2或该词词性不为nr时认为该词不为人名
            lineNames[-1].append(w.word)    # 为当前段的环境增加一个人物
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1    # 该人物出现次数加 1

# 根据识别结果构建网络
for line in lineNames:    # 对于每一段
    for name1 in line:
        for name2 in line:    # 每段中的任意两个人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:    # 若两人尚未同时出现则新建项
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] += 1    # 两人共同出现次数加 1

# 过滤冗余边并输出结果
# 假设共同出现次数少于 3 次的是冗余边，则在输出时跳过这样的边。
# 输出的节点集合保存为 busan_node.txt ，边集合保存为 busan_edge.txt 
with codecs.open("busan_node.txt", "w", "gbk") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("busan_edge.txt", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")

