from PIL import Image
import hashlib
import time
import math
import os

# 用 Python 类实现向量空间
class VectorCompare:
    # 计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量之间的 cos 值
    def relation(self,concordance1,concordance2):
        revelance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

# 将图片转换为矢量
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

v = VectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 加载训练集
imagest = []    # 存 {letter:temp}

for letter in iconset:   # 从0开始循环找文件夹
    for img in os.listdir('./iconset/%s/'%(letter)):    # 文件夹里有多个文件，循环找到 0.gif
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
        imagest.append({letter:temp})

im = Image.open("captcha.gif")
im.convert("P")    # 将图片转换为8位像素模式
im2 = Image.new("P",im.size,255)    # 提取文本图片，先新建一个同大小的空白im2，再逐行加入颜色

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227:
            im2.putpixel((y,x), 0)


# 提取单个字符图片，进行纵向切割
inletter = False
foundletter = False
start = 0
end = 0

letters = []    #存放每个字符开始和结束的列序号 (start,end)

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if inletter == True and foundletter == False:
        foundletter = True
        start = y    # start 就是每个字符的最左列
    if foundletter == True and inletter == False:
        foundletter = False
        end = y    # end 就是每个字符的最右列
        letters.append((start,end))

    inletter = False

count = 0
# 对验证码图片进行切割，一个字符一个图片
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0], 0, letter[1], im2.size[1] ))

    guess = []    # 存(cos, letter)

    # 将切割得到的验证码小片段与每个训练片段进行比较
    for image in imagest:    # imagest是列表，里面存的元素是{letter:temp}
        for x,y in image.items():    # x 是letter,即0...; y 是temp，即矢量图
            if len(y) != 0:
                # y[0] 是训练集的矢量图,buildvector(im3)是验证码的矢量图
                guess.append( ( v.relation(y[0],buildvector(im3)),x))    # 计算他俩的 cos 值,(cos, letter) 放到guess里

    guess.sort(reverse=True)
    print(guess[0])    # 输出最接近的那一个
    count += 1


