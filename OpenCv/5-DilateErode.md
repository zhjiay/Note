# Dilate 膨胀  Erode 腐蚀
膨胀和腐蚀是同一种操作两个反方向的实现

## 基本实现原理
- 设置一个卷积核ElementMat      

        Mat elementMat = Cv2.GetStructuringElement(MorphShapes.Rect, new Size(41, 41));//膨胀block
    第一个参数是卷积核的形状，第二个参数是卷积核的Size
- （暂时对于二极化的图像)用ElementMat去便利原图的每一个区域，如果ElemetMat覆盖的区域中会有0或1（maxValue）两个值。
- 对于膨胀Dilate，应该是白色区域更大，则其如果区域内有一个1，则该区域全部变为1。

        Cv2.Dilate(matBinary, matDilate, elementMat);
- 对于腐蚀Erode，目的是白色区域更小，如果区域内有一个0，则该区域全部变为0。
    
        Cv2.Erode(matBinary, matErode, elementMat);
