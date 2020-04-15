from darkflow.net.build import TFNet
import cv2
import numpy as np
import matplotlib.pyplot as plt
options = {"pbLoad": "built_graph/tiny-yolo-voc-h.pb",
            "threshold": 0.1,
           "metaLoad": "built_graph/tiny-yolo-voc-h.meta" 

           }        

           tfnet = TFNet(options)


def boxing(original_img, predictions):
    newImage = np.copy(original_img)

    for result in predictions:
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        confidence = result['confidence']
        label = result['label'] + " " + str(round(confidence, 2))

        if confidence > 0.1:
            newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_SIMPLEX ,1, (0, 255, 0), 1, cv2.LINE_AA)
            newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)
            
            
    return newImage





img="XXXX.jpg"
imgcv = cv2.imread(img)
result = tfnet.return_predict(imgcv)
print(result)

if len(result)!=0:
    _, ax = plt.subplots(figsize=(20, 10))
    ax.imshow(boxing(imgcv, result))
else:
    print("Nothing detected")