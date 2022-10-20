# Mat Rect Size Point
    OpenCv中数据的一般格式，Mat、Rect、Size均是二维矩阵，矩阵上的元素可以是多个维度的，比如Vec4i这种。
    Point是OpenCV中的点位，根据位置的不同，可以是不同类型的例如Point2d等。
    OpenCV中不同格式的图片都可以读为Mat类型。bmp、png、jpeg等。
### Mat
##### Mat的构造函数
        Mat tempMat = new Mat(rows:4,cols: 3, MatType.CV_16SC4);
    Mat本质上是一个至少二维（2dim)的数组。第一个值是行数，既第一个维度的数值，第二个是列数，既每一行的值。第三个是Mat的元素类型，其定义为 16为16bit存储；S为有符号的，或者是U无符号的，或者是F浮点数；第三个C表示Channels，频道数，1-4表示该位置是几维向量。如1，则是单通道，如果是3则是 Vec3i，这种。
    