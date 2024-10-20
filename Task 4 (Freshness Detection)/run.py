import cv2
import torch
from ultralytics import YOLO
from PIL import Image
import torch.nn as nn
from torchvision import models, transforms

# Load your custom YOLOv8 model weights
yolo_model = YOLO("best.pt")  # Specify the path to your YOLO weights file

# Load the saved AlexNet model
alexnet = models.alexnet(pretrained=True)
alexnet.classifier[6] = nn.Linear(4096, 1)  # Modify the final layer
alexnet.load_state_dict(torch.load('alexnet_model.pth', map_location=torch.device('cpu')))
alexnet.eval()  # Set the model in evaluation mode

# Define the same transformations used during training for AlexNet
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to 224x224 (AlexNet input size)
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize using ImageNet stats
])

# Open camera
cap = cv2.VideoCapture(2)  # Use 0 for the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Perform detection using YOLOv8
    results = yolo_model(frame)  # Perform detection on the current frame

    # Step 2: Access the results from YOLOv8
    detections = results[0].boxes  # Get bounding boxes from results

    # Loop over each detection
    for box in detections:
        print(box.cls[0])
        # Step 3: Check if the detection is a banana (assuming class index 0 is for banana)
        if int(box.cls[0]) != 2:  # Change '0' to the correct index for bananas if different
            
            # Step 4: Get the bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].int().tolist()  # Convert to integers

            # Step 5: Crop the detected object from the frame
            cropped_img = frame[y1:y2, x1:x2]

            # Convert the cropped image from OpenCV format (BGR) to PIL format (RGB)
            cropped_img_pil = Image.fromarray(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))

            # Step 6: Preprocess the cropped image for AlexNet
            input_tensor = transform(cropped_img_pil)
            input_tensor = input_tensor.unsqueeze(0)  # Add batch dimension

            # Step 7: Perform inference using the AlexNet model to get the credibility score
            with torch.no_grad():
                credibility_score = alexnet(input_tensor).item()

            # Step 8: Draw the bounding box and display the credibility score on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"Credibility: {credibility_score:.2f}"
            # print(label)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Step 9: Display the frame with detections and credibility scores
    cv2.imshow("YOLOv8 + AlexNet Credibility Score", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
