import cv2
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering
import torch

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

cap =cv2.videoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

ret,frame = cap.read()
if not ret:
    raise IOError("Failed to capture image")

cap.release()
cv2.destroyAllWindows()