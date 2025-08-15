from ultralytics import YOLO
from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROCESSED_FOLDER'] = 'static/results'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# 确保文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def object_detect(input_path, output_path):
    model = YOLO('/home/zyb/百度飞桨领航团/学习项目/CV项目/第六次汇报/yolov12/runs/detect/train2/weights/best.pt')
    with Image.open(input_path) as img:
        detect_img =  model.predict(img, save=False, save_txt=False, conf=0.7, line_width=2, save_crop=False,
                                    show_labels=True, show_conf=True, classes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        im_array = detect_img[0].plot()  # 生成带检测框的图像数组
        im = Image.fromarray(im_array[..., ::-1])  # 转换BGR为RGB格式
        im.save(output_path)  # 保存处理后的图片

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            original_filename = f"original_{timestamp}.{file.filename.rsplit('.', 1)[1].lower()}"
            processed_filename = f"processed_{timestamp}.jpg"
    
            original_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
            file.save(original_path)
    
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
            object_detect(original_path, processed_path)
            
            return render_template('result.html',
                                 original_image=url_for('static', filename=f'uploads/{original_filename}'),
                                 processed_image=url_for('static', filename=f'results/{processed_filename}'))
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)