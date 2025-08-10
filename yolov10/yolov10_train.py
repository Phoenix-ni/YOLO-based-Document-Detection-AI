import torch
from ultralytics import YOLO
import argparse
parser = argparse.ArgumentParser(description='Train YOLOv10: 设置训练参数')
parser.add_argument('--data', type=str, default='data.yaml', help='数据集配置文件路径')
parser.add_argument('--epochs', type=int, default=100, help='训练轮数')
parser.add_argument('--imgsz', type=int, default=640, help='输入图像大小')
parser.add_argument('--device', type=str, default='0', help='训练设备')
parser.add_argument('--batch', type=int, default=8, help='批次大小')
parser.add_argument('--workers', type=int, default=0, help='工作线程数')
parser.add_argument('--model', type=str, default='yolov10n.pt', help='预训练模型路径')
args = parser.parse_args()
torch.cuda.empty_cache()
model = YOLO(args.model)
model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz, device=args.device, batch=args.batch, workers=args.workers)
