from label_studio_ml.model import LabelStudioMLBase
import os
import cv2
from ultralytics import YOLO

class YOLOv10Model(LabelStudioMLBase):
    def __init__(self, **kwargs):
        super(YOLOv10Model, self).__init__(**kwargs)

        model_path = '/home/zyb/百度飞桨领航团/学习项目/CV项目/第六次汇报/yolov12/runs/detect/train2/weights/best.pt'
        self.model = YOLO(model_path)
        self.labels = self.model.names

    def predict(self, tasks, **kwargs):
        predictions = []

        for task in tasks:
            image_path = self.get_local_path(task['data']['image'])
            image = cv2.imread(image_path)

            result = self.model(image_path, verbose=False)[0]
            boxes = result.boxes

            results = []

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                label = self.labels[int(box.cls[0])]
                w = x2 - x1
                h = y2 - y1

                results.append({
                    "from_name": "label",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "x": x1 / image.shape[1] * 100,
                        "y": y1 / image.shape[0] * 100,
                        "width": w / image.shape[1] * 100,
                        "height": h / image.shape[0] * 100,
                        "rectanglelabels": [label]
                    }
                })

            predictions.append({
                "result": results,
                "score": 0.95  # 可选置信度
            })

        return predictions
