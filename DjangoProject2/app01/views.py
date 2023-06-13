import os
import time
from unittest import result

from django.shortcuts import render, redirect
import pymysql
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from app01 import function_
import base64
import cv2
import numpy as np
from django.http import JsonResponse

from django.http import HttpResponse, JsonResponse

tmp2=r"F:\source file\python\DjangoProject2\app01\static\tmp2"
tmp=r"F:\source file\python\DjangoProject2\app01\static\tmp"

m = function_.Graphics_Processing()

def my_view(request):
        m.clearTmp(r"F:\source file\python\DjangoProject2\app01\static\tmp")
        m.clearTmp(r"F:\source file\python\DjangoProject2\app01\static\tmp2")
        if request.method == 'POST':
            global name,thresh,maxval,choose,frequency
            thresh = request.POST.get('thresh')
            maxval = request.POST.get('maxval')
            choose = request.POST.get('choose')
            frequency = request.POST.get('frequency')
            name = request.POST.get('choose')
            files = request.FILES.getlist("folder")
            if files:
                for i in range(len(files)):
                    folder_path = files[i].name
                    # 通过在文件名前添加一个特定路径名来指定目录路径
                    folder_path = os.path.join(r"F:\source file\python\DjangoProject2\app01\static\tmp2", folder_path)

                    # 存储上传的文件到指定路径中
                    with open(folder_path, 'wb+') as destination:
                        for chunk in files[i].chunks():
                            destination.write(chunk)

                # 在这里编写其他处理代码

                return render(request,"view.html")
        return render(request,"main.html")

def view(request):
    img_paths = m.getImgPaths(tmp2)
    print("fasda",name)
    if name=='1':
        m.ThresholdProcessing(img_paths, thresh, maxval)
    elif name=='2':
        m.imgFlip(img_paths,choose)
    elif name=='3':
        m.imgRevolve(img_paths,frequency)
    elif name=='4':
        m.EdgeDetection(img_paths)
    elif name=='5':
        m.MorphologicalTreatment(img_paths)
    elif name=='6':
        m.ImageSegmentation(img_paths)
    elif name=='7':
        m.histogramEqualization(img_paths)
    elif name=='8':
        m.DetectCircles(img_paths)
    else :
        m.DetectLines(img_paths)
    oldPaths = m.GetImgName(tmp2)
    newPaths = m.GetImgName(tmp)
    return  render(request,"view.html",{"oldPath":oldPaths, "newPath":newPaths})


from django.http import JsonResponse

def index(request):
    return  render(request,"pto.html")

def capture_image(request):
    if request.method == 'POST':
# 从请求的 body 中获取图片数据
        image_data = request.POST.get('image')
# 对图片数据进行处理，例如保存到本地或者进行人脸识别等操作
# ...
        return JsonResponse({'message': '图片已处理'})
    else:
        return JsonResponse({'message': '请求方法不支持'})
