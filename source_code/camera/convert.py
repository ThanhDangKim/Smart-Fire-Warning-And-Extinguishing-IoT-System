from ultralytics import YOLO

# Load a model
model = YOLO('../trained_model/train23/weights/best.pt')  # load an official model

# Export the model
model.export(format='onnx')