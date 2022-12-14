# Mat Rect Size Point Vec
    OpenCv中数据的一般格式，Mat、Rect、Size均是二维矩阵，矩阵上的元素可以是多个维度的，比如Vec4i这种。
    Point是OpenCV中的点位，根据位置的不同，可以是不同类型的例如Point2d等。
    OpenCV中不同格式的图片都可以读为Mat类型。bmp、png、jpeg等。
---
## Mat
#### Mat的构造函数
        Mat mat = new Mat(rows:4,cols: 3, MatType.CV_16SC4);
    Mat本质上是一个至少二维（2dim)的数组。第一个值是行数，既第一个维度的数值，第二个是列数，既每一行的值。
    第三个是Mat的元素类型，其定义为 16为16bit存储；S为有符号的，或者是U无符号的，或者是F浮点数；
    第三个C表示Channels，频道数，1-4表示该位置是几维向量。如1，则是单通道，如果是3则是 Vec3i，这种。
    其余的构造函数还有：（主要是在rows和cols上不同，类型基本是固定的）
        ---利用Size类
        Size size = new Size(width: 5, height: 3);
        Mat mat = new Mat(size, MatType.CV_32FC1);

        ---利用Rect类，进行图形切割
        Rect(int x, int y, int width, int height);
        Rect rect = new Rect(cX - 120, cY - 120, 240, 240);
        Mat matCut = new Mat(mat3, rect);
#### MatType
    MatType.CV_16SC4，如此。
    其数据类型为严格对应基本数据类型和Vec


#### Mat值操作 At  unsafe
    不安全的获取某个位置元素值的方法。内部的参数是元素所在位置的维度，i0 demension 0 既第几行,i1 demension 1 表示第几列，i2，表示的是第几个channel；
    T是返回值类型，注意要和Mat的MatType匹配，T可以是基本数据类型，也可以是Vec元组。
    如果使用 Point读取该位置的数据，那么注意Point.X表示的是第几列，应该是i1位置；Point.Y表示的是第几行，应该是i0位置
        ref T Mat.At<T>(i0,i1,i2)
    返回的T是该位置的元素，可以更改这个数值。At方法是Get和Set都可以操作的
#### Mat值操作 Set
    安全的Set操作
        public void Set<T>(int i0,int i1,int i2,T value);
    把 （i0,i1,i2)处的值设置为value；value需要继承Struct；基本数据类型和Vec应该都可以
#### Mat值操作 Get
    安全的Get操作
        public T Get<T>(int i0,int i1,int i2);
    返回 (i0,i1,i2)处的 T value；
    
---
## Size
#### Size的定义
    在OpenCV中Size表示一个二维矩阵，width表示cols数，height表示rows数。
        Size size = new Size(width:3, height:4);


---
## Rect
#### Rect的定义
    Rect表示的是一个矩形区域，既在坐标中的一个矩形区域；构造函数中，x y 表示的是矩形区域左上角的点位，(点位index从0开始)，width和height表示矩形的宽和长。
        Rect rect = new Rect(x: 5, y: 4, width: 10, height: 12);
        Rect rect = new Rect(cX - 120, cY - 120, 240, 240);
        Mat matCut = new Mat(mat3, rect);

---
## Point
#### Point的定义和类型
    point就是一个坐标向量，表示的就是点位(x,y,x ... );
    point的类型有：
        dimension 1: Point
        dimension 2: Point2d Point2f
        dimension 3: Point3d Point3f Point3i

---
## Vec
#### Vec向量的定义
    Vec本质上就是一个元组Tuple，用于存放Mat中元素的值的类型。  
        Vec2d vec2D = new Vec2d(1.2, 3.4);
    Vec有这么多种：
        Vec2b 表示二维 byte元组 8bit //为无符号，有符号的是 sbyte
        Vec2s 表示二维 short元组 16bit
        Vec2w 表示二维 ushort元组 16bit
        Vec2i 表示二维 int元组 32bit
        Vec2f 表示二维 float单精度浮点数元组 32bit
        Vec2d 表示二维 double双精度浮点数元组 64bit
        2 表示二维(x,y)，如果是3就是(x,y,z);
    Vec 作为Mat的元素类型是，可以很方便的表示Channels。
