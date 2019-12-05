# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


# # 去除干扰点
# def clrImg(img,pointArr):
#  # 获取周围黑点的个数
#  def getN(p):
#   count = 0
#   x = [p[0]-1,p[0],p[0]+1]
#   y = [p[1]-1,p[1],p[1]+1]
#   for i in itertools.product(x,y): # 笛卡尔积
#    try:
#     if img.getpixel(i) == 0:
#      count +=1
#    except:
#     print 'out of'
#     continue
#   print count
#   return count
 
#  for p in pointArr:
#   if getN(p)<5: # 周围黑点个数 <5 的黑点认为是干扰点,置为白点
#    img.putpixel(p,255)

def clipping(img, width):
    w, h = img.size
    pixdata = img.load()
    for x in range(width):
        for y in range(0, h):
            pixdata[x, y] = 255
    for x in range(w - width, w):
        for y in range(0, h):
            pixdata[x, y] = 255
    for x in range(0, w):
        for y in range(0, width):
            pixdata[x, y] = 255
    for x in range(0, w):
        for y in range(h - width, h):
            pixdata[x, y] = 255
    return img

def addTransparency(img, factor = 0.7 ):
    img = img.convert('RGBA')
    img_blender = Image.new('RGBA', img.size, (0,0,0,0))
    img = Image.blend(img_blender, img, factor)
    return img

def getPngPix(img_src, pixelX = 1, pixelY = 1):
    img_src = img_src.convert('RGBA')
    str_strlist = img_src.load()
    data = str_strlist[pixelX,pixelY]
    img_src.close()
    return data

def a_handle(img):
    img = img.convert('RGBA')
    for w in range(0, img.size[0]):
        for h in range(0, img.size[1]):
            r,g,b,a = img.getpixel((w, h))
            if (r==g and g==b and b==0 and a!=0):
                img.putpixel((w, h),(255,255,255,a))
            else:
                img.putpixel((w, h),(r,g,b,0))
    return img

def b_handle(img):
    p1 = (0,0,315,360)
    p2 = (224,0,740,291)
    p3 = (646,0,960,360)
    p4 = (0,261,407,562)
    p5 = (313,202,648,562)
    p6 = (556,260,960,562)
    img = img.crop(p6)
    return img

def c_handle(img,x1,y1,x2,y2):
    img = img.convert('RGBA')
    arr = []
    for w in range(x1, x2):
        for h in range(y1, y2):
            r,g,b,a = img.getpixel((w, h))
            if (r==g and g==b and b==0 and a!=0):
                arr.append([w,h])
                print (w,h)
                break
    return arr

img_path = './zm.png'
img1_path = './new.png1.png'
img = Image.open(img_path)
img1 = Image.open(img1_path)
c_handle(img1,0,255,310,370)
# w,h = img.size
# print (w,h)
# print (img1.size)

# img2 = Image.open('./out.png')
# img2 = b_handle(img2)
# img2.show()

# img = a_handle(img1)
# img.save(img_path+'2.png')

# layer=Image.new('RGBA', img.size, (0,0,0,0))
# layer.paste(img1, (0, 0))
# out=Image.composite(layer,img,layer)
# out.show()
# out.save('out.png')

# data = getPngPix(img,1,1)
# print (data)
# img = addTransparency(img, 0.7)
# img.show()

# img = img.convert('RGBA')
# r, g, b, alpha = img.split()
# alpha = alpha.point(0)
# img.putalpha(alpha)
# img.show()


# 缩放
# img_resize = img.resize((960,562))
# img = img_resize
#img = clipping(img, 22)
#img.save('./new.jpe','jpeg')

#轮廓滤波
# img_contour = img.filter(ImageFilter.CONTOUR)
# img_contour.show()

#细节滤波
# img_detail = img.filter(ImageFilter.DETAIL)
# img_detail.show()

#模糊滤波
#img_blur = img.filter(ImageFilter.BLUR)
# img_blur.show()

#边缘滤波
# img_edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)
# img_edge_enhance.show()

#锐化滤波
# img_sharp = img.filter(ImageFilter.SHARPEN)
# img_sharp.show()

#高斯模糊滤波
# img_gauss = img.filter(ImageFilter.GaussianBlur(radius=2))  # radius指定平滑半径，也就是模糊的程度。
# img_gauss.show()
# img = img_gauss

#对比度增强
# img_contrast = ImageEnhance.Contrast(img)
# contrast = 9
# image_contrasted = img_contrast.enhance(contrast)
# image_contrasted.show()
# image_contrasted.save('./new1.jpe','png')

#锐度增强
# img_sharp = ImageEnhance.Sharpness(img)
# sharpness = 2
# image_sharped = img_sharp.enhance(sharpness)
# image_sharped.show()

# box = (10, 10, 700, 70)
# region = img.crop(box) 
# region.show()

# mask = '1'
# im.paste(im_crop, (400,400,500,500),mask)
# im.show()

# new_size = (cut_size[0]*3, cut_size[1]*2)
 
# new_image = Image.new('RGB', new_size)
# for i in range(0, 3):
#     im = image.resize(cut_size, resample=resmaple_list[i])
#     new_image.paste(im, (i*cut_size[0], 0))
 
# for i in range(3, 6):
#     im = image.resize(cut_size, resample=resmaple_list[i])
#     new_image.paste(im, ((i-3)*cut_size[0], cut_size[1]))
