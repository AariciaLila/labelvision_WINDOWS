from ultralytics import YOLO
import os
import torch
#import mlflow
#import mlflow.pytorch

#   mlflow.pytorch.autolog()


def train_yolo(data_yaml: str, img_size: int, epochs: int, model_path: str, gpu_id: int = 0):
    # Assurez-vous que CUDA est disponible et sélectionnez le GPU
    if torch.cuda.is_available():
        device = torch.device(f'cuda:{gpu_id}')
        print(f"Using GPU: {torch.cuda.get_device_name(gpu_id)}")
    else:
        device = torch.device('cpu')
        print("CUDA not available. Using CPU.")

    model = YOLO("yolov5n.pt").to(device)
    result = model.train(data=os.path.join(os.getcwd(), data_yaml), epochs=epochs, imgsz=img_size, device=device)
    model.save(model_path)

    print("------------------------------------------------")
    print(type(result))
    print("------------------------------------------------")

     # Afficher les métriques après l'entraînement
    print("Training completed. Here are the metrics:")

  
    # Afficher toutes les métriques disponibles dans result
    print("\nDetailed metrics:")
    for key, value in vars(result).items():
        print(f"{key}: {value}")


   