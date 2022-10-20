# Threshold 二极化
    Cv2.Threshold(matGray, matBinary, 125, 255, ThresholdTypes.Binary);//进行二极化
    Cv2.Threshold(matGray, matBinary, 125, 255, ThresholdTypes.BinaryInv);//进行二极化反转
前两个参数为输入图片，输出图片，第三个参数是二极化阈值，第四个参数是高于阈值的像素设置的值，第五个参数是二极化类型；
##### ThresholdTypes
    Binary 二极化 高于阈值设置为maxValue既255，低于设置为0
    BinaryInv 二极化反转
    OTsu 大津法，动态阈值，会更具不同区域求出一个阈值进行二极化