# CvtColor 图片格式转换
    if (inMat.Channels() == 3)
    {
        Cv2.CvtColor(inMat, matGray, ColorConversionCodes.BGR2GRAY，dstCn: 0);
    }    
    else
    {
        matGray = inMat;
    }
输入参数为 in Mat需要转换的图片，out Mat 转换的结果图。转换格式 ColorConversionCodes，和dstCn目标通道数，默认0为原始图像自动生成，一般不用管。

#### ColorConversionCodes
    颜色转换代码，非常多，列举几个比较常用的
    BGR2GRAY  BGR转灰度图（既单通道）
    GRAY2RGB  灰度图转RGB彩图
    
