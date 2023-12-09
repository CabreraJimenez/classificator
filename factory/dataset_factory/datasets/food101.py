from torchvision.datasets import Food101
from config.read_config import read_config
import torchvision.transforms as transforms

class CustomFood101:
    def __init__(self, root=None, transforms=transforms.Compose):
        if root is None:
            root = read_config()["data_path"]
        self.train_dataset = Food101(root = root, download = True, split = "train", transform = transforms)
        self.test_dataset = Food101(root = root, download = True, split = "test", transform=transforms)
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        return self.dataset[idx]
    
    def __repr__(self):
        return "Food101 Dataset"
