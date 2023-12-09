from torch import nn
from factory.model_factory import Model
import torchvision

class EffnetB0(nn.Module,Model):
    def __init__(self):
        super().__init__()
        self.model = self.load_model()
        self.transforms = self.load_default_transfroms()

    def load_model(self) -> (nn.Module):
        return torchvision.models.efficientnet_b0(torchvision.models.efficientnet.EfficientNet_B0_Weights.DEFAULT)
    
    def load_default_transfroms(self) -> torchvision.transforms.Compose:
        return torchvision.models.EfficientNet_B0_Weights.DEFAULT.transforms()
    
    def modify_classifer(self, num_classes):
        self.model.classifier = nn.Linear(1280, num_classes)
    
    def forward(self, x):
        return self.model(x)