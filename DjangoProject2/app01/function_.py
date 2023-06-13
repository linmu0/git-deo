import os
import sys
import numpy as np
import cv2
import csv


# 将默认的递归深度修改为3000
sys.setrecursionlimit(3000)

class Graphics_Processing:

    def GetImgName(self,IMG_PATHS):
        result = []
        for name in os.listdir(IMG_PATHS):
            result.append(name)
        return result

    def getImgPaths(self,IMG_PATHS):
        """
        获取文件夹下面所有图片路径
        :param IMG_PATHS:文件夹路径
        :return: 所以图片路径
        """
        result = []
        for name in os.listdir(IMG_PATHS):
            path = os.path.join(IMG_PATHS, name)
            path=path.replace("\\","/")
            result.append(path)
        return result

    def clearTmp(self,tmpPath):
        """
        清空缓存文件
        :param tmpPath: tmp文件夹路径
        :return: none
        """
        for filename in os.listdir(tmpPath):
            file_path = os.path.join(tmpPath, filename)
            if os.path.isdir(file_path):
                self.clearTmp(file_path)
                os.rmdir(file_path)
            else:
                os.remove(file_path)

    def ThresholdProcessing(self, paths, thresh, maxval):
        """
        图像二值化处理：将灰度图像转换为二值图像，使像素值只有0和255两种。
        :param paths:需要处理的图像路径列表
        :param thresh:用于对像素值进行阈值判断的参考值（参考值）
        :param maxval:用于像素值超过阈值时的最大值
        """
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (400, 400))
            if img is None:
                print(f"Failed to read image {path}")
                continue

            # 进行二值化处理
            ret, threshed = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)

            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, threshed)

    def imgFlip(self,paths,choose):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))
            if img is None:
                print(f"Failed to read image {path}")
                continue
            if choose=='1':
                # 水平翻转
                imgNew = cv2.flip(img, 1)
            elif choose=='2':
                # 垂直翻转
                imgNwq = cv2.flip(img, 0)
            else :
                # 水平垂直翻转
                imgNew = cv2.flip(img, -1)


            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, imgNew)

    def imgRevolve(self,paths,frequency):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))

            h, w = img.shape[:2]

            # 设置旋转中心点和旋转角度
            center = (w / 2, h / 2)
            angle = 45
            scale = 1.0

            # 获取旋转矩阵并应用旋转
            M_rot = cv2.getRotationMatrix2D(center, angle, scale)
            for j in range(frequency):

                img = cv2.warpAffine(img, M_rot, (w, h))

            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, img)

    def EdgeDetection(self,paths):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Canny边缘检测
            edges = cv2.Canny(gray, threshold1=50, threshold2=150)

            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, edges)

    def MorphologicalTreatment(self,paths):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 定义结构元素和操作
            kernel = np.ones((5, 5), np.uint8)
            dilated = cv2.dilate(gray, kernel, iterations=1)

            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, dilated)

    def ImageSegmentation(self,paths):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 对灰度图像进行二值化处理
            ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            # 形态学操作，去除噪点
            kernel = np.ones((3, 3), np.uint8)
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

            # 膨胀操作，使物体连在一起
            sure_bg = cv2.dilate(opening, kernel, iterations=3)

            # 距离变换，获取前景区域
            dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
            ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

            # 获取未知区域
            sure_fg = np.uint8(sure_fg)
            unknown = cv2.subtract(sure_bg, sure_fg)

            # 标记连通区域
            ret, markers = cv2.connectedComponents(sure_fg)
            markers = markers + 1
            markers[unknown == 255] = 0

            # 分水岭算法进行分割
            markers = cv2.watershed(img, markers)
            img[markers == -1] = [255, 0, 0]

            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, img)

    def histogramEqualization(self,paths):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 直方图均衡
            dst = cv2.equalizeHist(gray)
            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, dst)

    def DetectCircles(self,paths):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img,(400,600))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (400, 400))
            # 设置参数
            dp = 1
            minDist = 50
            param1 = 200
            param2 = 15
            minRadius = 0
            maxRadius = 0

            # 检测圆
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1,
                                       param2=param2, minRadius=minRadius, maxRadius=maxRadius)

            # 绘制圆
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    cv2.circle(img, (x, y), r, (0, 255, 0), 2)
            # 保存处理后的图像
            img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
            img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
            cv2.imwrite(img_output_path, img)

    def DetectLines(self,paths):
        TMP_PATH = r"F:\source file\python\DjangoProject2\app01\static\tmp"
        if not os.path.exists(TMP_PATH):
            os.makedirs(TMP_PATH)
        for i, path in enumerate(paths):
            # 读取图像
            img = cv2.imread(path)
            img = cv2.resize(img,(400,600))
            # 转换为灰度图像
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 边缘检测
            edges = cv2.Canny(gray, 50, 150, apertureSize=3)

            # 检测直线
            lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

            # 绘制直线
            if lines is not None:
                for line in lines:
                    rho, theta = line[0]
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    x1 = int(x0 + 1000 * (-b))
                    y1 = int(y0 + 1000 * (a))
                    x2 = int(x0 - 1000 * (-b))
                    y2 = int(y0 - 1000 * (a))
                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    # 保存处理后的图像
                    img_file_name = os.path.basename(path).split(".")[0]  # 获取文件名（不包含扩展名）
                    img_output_path = os.path.join(TMP_PATH, f"{img_file_name}.jpg")
                    cv2.imwrite(img_output_path, img)


if __name__ == '__main__':
    # pass
    p = Graphics_Processing()
    # p.clearTmp(r"F:\source file\python\DjangoProject2\app01\static\tmp")
    # p.clearTmp(r"F:\source file\python\DjangoProject2\app01\static\tmp2")
    # img_paths = p.getImgPaths(r"F:\source file\python\DjangoProject2\app01\static\imgs")
    # p.ThresholdProcessing(img_paths,127,255)
    # p.imgFlip(img_paths,1)
    # p.imgRevolve(img_paths,2)
    # p.EdgeDetection(img_paths)
    # p.MorphologicalTreatment()
    # p.ImageSegmentation(img_paths)
    # p.DetectLines(img_paths)
    # print(img_paths)
    # i=p.GetImgName(r"F:\source file\python\DjangoProject2\app01\static\tmp")
    # print(i)
