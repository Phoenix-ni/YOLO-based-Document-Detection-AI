# YOLO-based-Document-Detection-AI
专注于YOLOv10,v11和v12在文档检测中的用途,以及成果分析
# 使用教程
## 版本配置
本项目中采用python3.11.11,cuda12.6版本激活GPU
## Windows教程
### 创建虚拟环境
```bash
conda create -n yolo python=3.11
conda activate yolo
```
### 1. 下载依赖包
```bash
pip install ultralytics
```
**注:** 到这一步,你的GPU并没有被激活
```bash
python
import torch
torch.cuda.is_available()
exit()
```
**注:** 若输出为Ture则激活成功,若激活为False则激活不成功
### 2. 打开Pytorch官网
[Pytorch官网地址](https://pytorch.org/)
![[markdown/pytorch.png]]
根据自己环境修改配置获取到相应指令
例如:
```bash
pip3 install -U torch torchvision --index-url https://download.pytorch.org/whl/cu126
```
到这里,不出意外的话,你的GPU此时会被激活
### 3. 图片标注
```bash
# 安装标注平台
pip install label-studio
# 启动标注平台
label-studio
```
这一部分自己可以尝试标注自己的图片训练,也可以直接使用当前仓库中已经标好并且导出的文件
夹(训练文件夹,里面标注数字的文件夹标注图片张数,表示会训练出不同效果的模型)
### 4. 训练代码
#### 基本数据准备
在训练之前,需要先准备data.yaml文件,以便读取到要训练的数据
```yaml
train: train # 训练集
val: val # 验证集

nc: number # 标注的类别个数

names: [] # 具体类别
```
这部分可以在源代码中参考查看
#### 开始训练
```bash
python yolov11_train.py --data data.yaml --epochs 100 --model yolov11n.pt
```
这部分参数同样可以查看,然后自己设置
### 5. 目标检测
```bash
python yolov11_predict.py --model best.pt --source 要检测的图片的文件夹
```
## Linux教程

**注:** ***大体和Windows一致,唯一需要区别的就是在激活GPU的时候选择linux而不是Windows***

## 图片标注部分
在训练模型当中,需要大量标注好的数据集,手动标注将会是意见很痛苦的事情,这时候就需要搭建后端,利用小模型帮助标注
### 标注流程 
![[markdown/标注流程.png]]
### 启用教程
```bash
pip install label-studio label-studio-ml ultralytics opencv-python
```
```bash
label-studio-ml init my_backend --script back.py --force
label-studio-ml start yolov11_polygon_backend
```
之后打开label studio,点击setting--->model--->connect--->输入你的网页地址(在终端可以看到),如果连接成功,可以看到上面有个小绿点,表示连接成功
**注:**
- ***在标注过程中,网络不可变更,连接热点打开的终端,换成无线之后会断掉连接***
- ***你的后端程序所用的标注类型必须和你标注时设置的类型一致***