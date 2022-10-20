# ImWrite   ImRead ImShow
## ImWrite
    string filePath="";
    mat.ImWrite(filePath);
    Cv2.ImWrite(filePath,mat);
    两种方法都可以。
---
## ImRead
    string filePath="";
    Mat mat=new Mat(filePath,ImreadModes:);
    Mat mat= Cv2.ImRead(filePath,ImreadModes:);
    读取图像第一个参数就是文件路径，第二个参数是读取模式。
    读取灰度图(Channels=1)： Grayscale ReducedGrayscale2(读取1/2的灰度图)等
    读取彩图（Channels=3)： Color ReducedColor2(读取1/2的彩图)等
需要注意的是，系统可能默认读取为三通道的彩图。使用前最好还是对图片类型进行确认      

---
## ImShow
    Cv2.ImShow("showWindowName",mat);
显示图片