# Operating On Python Code
from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/tiny-yolo-voc.cfg", "load": "bin/tiny-yolo-voc.weights", "threshold": 0.1}

tfnet = TFNet(options)

imgcv = cv2.imread("./testHyunah/H3.jpg")
result = tfnet.return_predict(imgcv)
print(result)