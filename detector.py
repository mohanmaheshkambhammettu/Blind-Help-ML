
import torch
import cv2
from PIL import Image
import numpy as np

class ObstacleDetector:
    def __init__(self, model_name='yolov5n'):
        self.model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)

    def detect(self, image_path):
        results = self.model(image_path)
        results.print()
        results.save()
        return results
