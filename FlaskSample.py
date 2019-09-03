from flask import Flask, request, Response
import numpy as np
import io
import cv2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/FlaskTest', methods=['POST'])
def FlaskTest():
    """ post image and return the response """
    resultTxt = ""
    if request.files['img_file']:
        file = request.files['img_file']
        if file:
            photo = request.files['img_file']
            in_memory_file = io.BytesIO()
            photo.save(in_memory_file)
            data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            color_image_flag = 1
            img = cv2.imdecode(data, color_image_flag)
            cv2.imwrite('test.jpg', img)
            print(img)
            #img 파일 여기서 알아서 처리 하면 됨
            resultTxt = "OK"
    else:
        resultTxt = "이미지가 없습니다."
    return resultTxt

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8787, debug='True')