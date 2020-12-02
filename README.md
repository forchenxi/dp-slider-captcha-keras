本项目是基于[keras-yolov3](https://github.com/qqwweee/keras-yolo3)的，实际运用于检测滑动验证码的滑块位置，包含一些我的改动。

权重文件[yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)没有放到`GitHub`中，因为文件比较大,同样的model_data中也没有`h5`文件。

model_data中相比原项目，`voc_classes`和`yolo_anchors`有所改动，分别改成了自己的目标类别和滑块的大小值。

`VOCdevkit`中是我自己的训练集，有305张图片以及标注好的`xml`文件。

`yolo3中的model.py`也有所修改，去掉了所有的`num_layer`下面的//3，另外anchor_mask改为：

```python
anchor_mask = [[2], [1], [0]] if num_layers==3 else [[3,4,5], [1,2,3]]
```

`kmeans`作了部分改动用于生成自己数据集的`anchors`;

以及`train.py、voc_annotation.py、yolo.py、yolo_video、yolov3.cfg`都有不同程度的改动，具体参考我的博客：[深度学习目标检测破解滑动验证码](https://forchenxi.github.io/2020/11/22/dl-slider-captcha/#more)

训练得到的模型文件也比较大，放百度云了，链接: https://pan.baidu.com/s/1bR9BCGqWw-sA6Ag3V4Zcxw 提取码: dwf2 。