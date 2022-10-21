# FindContours 寻找轮廓
    Point[][] contours;
    HierarchyIndex[] hierarchyA;
    Cv2.FindContours(matDilateAnti, out contours, out hierarchyA, RetrievalModes.Tree, ContourApproximationModes.ApproxSimple);
寻找轮廓找的是连通域的轮廓，一般是图像二极化之后对该区域的白色区域求连通域。
## 参数
第一个是输入图像，第二个是 输出的轮廓Point[][] contours，第三个是轮廓的拓扑信息，暂时不用管。
第四个 RetrievalModes 寻找轮廓的方式，其中Tree。
第五个是轮廓近似方法，

## 轮廓信息
#### area
    double area = Cv2.ContourArea(cnt);
    轮廓的面积信息
#### 轮廓质心
    
    center.X = M.M10 / M.M00;
    center.Y = M.M01 / M.M00;
#### 轮廓外接圆

#### 轮廓外接矩形

#### 判断点是否在轮廓中（点到轮廓的距离）