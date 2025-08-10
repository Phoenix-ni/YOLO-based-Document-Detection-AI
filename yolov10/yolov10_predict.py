from ultralytics import YOLO
import argparse
parser = argparse.ArgumentParser(description='Predict YOLOv10: 设置预测参数')
parser.add_argument('--model', type=str, default='best.pt', help='预训练模型路径')
parser.add_argument('--source', type=str, default='dataset/测试', help='预测数据源路径')
args = parser.parse_args()
model = YOLO(args.model)
model.predict(source=args.source,show=False,conf=0.7,save=True,save_txt=True,save_conf=True,line_width=2,show_labels=True,show_conf=True,classes=[0,1,2,3,4,5,6,7,8,9,10,11,12])
