import cv2
import numpy as np
from HandTracker import HandDetector
import os




# Load YOLO
net = cv2.dnn.readNet("6. Real anti text\yolov3.weights", "6. Real anti text\yolov3.cfg")
classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis','snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']


# Set up output layers
layer_names = net.getLayerNames()
unconnected_layers = net.getUnconnectedOutLayers()

# Validate and map indices to layer names
output_layers = []
for layer_index in unconnected_layers:
    layer_index -= 1  # Adjust the index to match the range of layer_names
    if 0 <= layer_index < len(layer_names):
        output_layers.append(layer_names[layer_index])
print(layer_names)
print(output_layers)

# Load image



handdetector = HandDetector()
cap = cv2.VideoCapture(0)
while 1:
    success, image = cap.read()
    handdetector.findHands(image)
    leftlandmarks = handdetector.find_Landmarks(image)
    #rightlandmarks = handdetector.find_Landmarks(image, 1)
    


    # Resize and normalize image
    height, width, channels = image.shape
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Pass the blob through the network
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Initialization
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4
    phones = 0
    # Process outputs
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > conf_threshold and (class_id == 67 or class_id == 2):  # Class ID 67 represents the phone
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    # Apply non-maximum suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    # Draw bounding boxes and labels
    for i in indices:
        phones += 1
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(image, f"phones: {phones}", (100, 100), cv2.FONT_HERSHEY_COMPLEX,1, (0, 255, 0), 2)


    if phones > 0:
        os.system("6. Real anti text\inject.bin")
        os.system("6. Real anti text\duckypayload.txt")

    # Display the output
    cv2.imshow("Phone Detection", image)
    cv2.waitKey(1)
