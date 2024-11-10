import ast
from PIL import Image
import torchvision.transforms as transforms
import torch
from torch.autograd import Variable
import torchvision.models as models

# Load pre-trained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

# Dictionary of available models
available_models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load ImageNet class labels from file
with open('imagenet1000_clsid_to_human.txt') as file:
    imagenet_classes = ast.literal_eval(file.read())

def classifier(img_path, model_name):
    """
    Classifies the image at img_path using the specified pre-trained model.
    
    Args:
        img_path (str): Path to the image file to be classified.
        model_name (str): Name of the model to use ('resnet', 'alexnet', or 'vgg').

    Returns:
        str: Human-readable label for the predicted class.
    """
    # Load and preprocess the image
    image = Image.open(img_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    img_tensor = preprocess(image).unsqueeze(0)

    # Disable gradients for inference
    pytorch_version = torch.__version__.split('.')
    if int(pytorch_version[0]) > 0 or int(pytorch_version[1]) >= 4:
        img_tensor.requires_grad_(False)
    else:
        img_tensor = Variable(img_tensor, volatile=True)

    # Set the model to evaluation mode
    model = available_models[model_name]
    model.eval()

    # Perform the forward pass
    with torch.no_grad():
        output = model(img_tensor)

    # Extract predicted class index
    predicted_idx = output.data.numpy().argmax()

    # Return human-readable label for the predicted class
    return imagenet_classes[predicted_idx]
